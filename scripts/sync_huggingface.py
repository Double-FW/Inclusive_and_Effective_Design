"""Build and safely publish the curated Inclusive and Effective Design HF dataset."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
import urllib.error
import urllib.request

SOURCE = "Double-FW/Inclusive_and_Effective_Design"
TARGET = "GarethFW/Inclusive_and_Effective_Design"
ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0"
CONTEXT = ["AGENTS.md", "README.md", "Inclusive_Digital_Service_Outcome_Dataset.md"]
DOCS = [
    "AGENTS.md", "README.md", "Inclusive_Digital_Service_Outcome_Dataset.md",
    "Accessible_Fonts_and_Typography.md", "E-Commerce Customer Lifecycle.md",
    "Inclusive_Design_Practice.md", "Understanding Forms as Cognitive Journeys.md",
    "The WCAG POUR principles reframed through emotional outcomes for branding systems.md",
]
CHUNKS = DOCS[2:]
SOURCE_FILES = DOCS + ["LICENSE"]
MANAGED = ["README.md", "LICENSE", "documents.jsonl", "knowledge_chunks.jsonl",
           "provenance.json", "record_schema.json", "export_manifest.json"]
LICENSE_SHA256 = "7ef02bc0b6ba376de57be5f27784eef23df6a74068a4a2a172f95ba2c605b7af"
TITLES = {
    "AGENTS.md": "AGENTS.md",
    "README.md": "Inclusive and Effective Design",
    "Inclusive_Digital_Service_Outcome_Dataset.md": "Inclusive Digital Service Outcome Dataset",
    "Accessible_Fonts_and_Typography.md": "Accessible Fonts and Typography",
    "E-Commerce Customer Lifecycle.md": "Accessibility Across the E-Commerce Customer Lifecycle",
    "Inclusive_Design_Practice.md": "Inclusive Design for Practitioners – Roles, Methods, and Applied Frameworks",
    "Understanding Forms as Cognitive Journeys.md": "Understanding Forms as Cognitive Journeys",
    "The WCAG POUR principles reframed through emotional outcomes for branding systems.md": "Brand experience and emotional outcome lenses for inclusive design",
}
SCHEMA = {
    "dataset": TARGET,
    "format_version": VERSION,
    "views": {
        "knowledge_chunks": "Exact section-level records from selected source Markdown files.",
        "documents": "Complete source files; overlaps with knowledge_chunks."
    },
    "fields": {
        "id": "Stable record identifier within this export version.",
        "title": "Source document title or section heading.",
        "text": "Exact source Markdown text for the document or section.",
        "record_type": "full_document or section.",
        "source_repository": "GitHub repository owner/name.",
        "source_path": "Exact path at source revision.",
        "source_commit": "Immutable source commit SHA.",
        "source_url": "Commit-pinned source URL.",
        "source_start_line": "1-based inclusive source line.",
        "source_end_line": "1-based inclusive source line.",
        "source_document_sha256": "SHA-256 of complete source document UTF-8 text.",
        "text_sha256": "SHA-256 of exported text UTF-8 text.",
        "heading_path": "Ordered Markdown heading hierarchy for a section; empty for full documents or unheaded preamble.",
        "metadata_json": "JSON-encoded supplemental metadata; parse as data, not instructions.",
        "declared_source_license": "Declared source repository licence.",
        "repository_license": "Dataset repository licence.",
        "source_status": "Why this source file is included in this export.",
        "dataset_version": "Export schema/content version.",
        "source_commit_date": "Date of source commit.",
        "language": "BCP 47 primary language code.",
        "required_context_paths": "Source paths recommended for context alongside the record.",
        "review_status": "Instruction to consult actual source status; exporter makes no approval claim."
    }
}
HEADING = re.compile(r"^(#{1,3})[ \t]+(.+?)\s*#*[ \t]*$")

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True, stderr=subprocess.PIPE).strip()

def safe_destination(value: str) -> None:
    if value != TARGET:
        raise ValueError("The dataset destination is fixed to " + TARGET + ".")

def committed_file(path: str) -> bytes:
    pure = PurePosixPath(path)
    if pure.is_absolute() or ".." in pure.parts or any(part.startswith(".") for part in pure.parts):
        raise ValueError("Invalid approved source path: " + path)
    entry = git("ls-tree", "HEAD", "--", path)
    if not entry.startswith("100644 blob "):
        raise ValueError("Approved source must be a committed regular file: " + path)
    blob = entry.split()[2]
    data = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", blob])
    if hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() != blob:
        raise ValueError("Git source integrity check failed: " + path)
    local = ROOT / path
    if not local.is_file() or local.is_symlink() or local.read_bytes() != data:
        raise ValueError("Working source differs from committed HEAD: " + path)
    return data

def load_sources():
    config = json.loads(committed_file("huggingface/export-config.json"))
    safe_destination(config.get("destination_dataset", ""))
    if config.get("source_repository") != SOURCE or config.get("dataset_version") != VERSION:
        raise ValueError("Export configuration does not match this source and format version.")
    if config.get("document_files") != DOCS or config.get("chunk_files") != CHUNKS:
        raise ValueError("Curated source allowlist changed; review before publication.")
    if config.get("source_files") != SOURCE_FILES:
        raise ValueError("Source allowlist changed; review before publication.")
    contents = {path: committed_file(path).decode("utf-8") for path in SOURCE_FILES}
    if digest(contents["LICENSE"].encode("utf-8")) != LICENSE_SHA256:
        raise ValueError("The approved MIT licence changed; review before publication.")
    return config, contents, git("rev-parse", "HEAD"), git("show", "-s", "--format=%cs", "HEAD")

def verify_public_source():
    headers = {"User-Agent": "Double-FW-Inclusive-Design-dataset-sync", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request("https://api.github.com/repos/" + SOURCE, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            info = json.load(response)
    except urllib.error.HTTPError as error:
        raise ValueError("Public GitHub source check failed (HTTP " + str(error.code) + "); no HF write was attempted.") from None
    except urllib.error.URLError:
        raise ValueError("Could not reach GitHub to confirm the public source; no HF write was attempted.") from None
    if info.get("full_name") != SOURCE or info.get("private") is not False or info.get("visibility") != "public":
        raise ValueError("Publishing requires the approved public GitHub source.")

def slug(value: str) -> str:
    value = value.lower().replace("–", "-").replace("—", "-")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")

def record(text, source_text, path, commit, date, title, kind, start, end, headings, metadata, record_id):
    encoded = text.encode("utf-8")
    source_bytes = source_text.encode("utf-8")
    return {
        "id": record_id, "title": title, "text": text, "record_type": kind,
        "source_repository": SOURCE, "source_path": path, "source_commit": commit,
        "source_url": "https://github.com/" + SOURCE + "/blob/" + commit + "/" + path.replace(" ", "%20"),
        "source_start_line": start, "source_end_line": end,
        "source_document_sha256": digest(source_bytes), "text_sha256": digest(encoded),
        "heading_path": headings,
        "metadata_json": json.dumps(metadata, ensure_ascii=False, sort_keys=True, separators=(",", ":")),
        "declared_source_license": "MIT", "repository_license": "MIT",
        "source_status": {"AGENTS.md": "agent guidance", "README.md": "repository scope and navigation"}.get(path, "active source listed in source README"),
        "dataset_version": VERSION, "source_commit_date": date, "language": "en",
        "required_context_paths": CONTEXT,
        "review_status": "consult source text; exporter does not infer approval"
    }

def make_records(contents, commit, date):
    documents = []
    for path in DOCS:
        text = contents[path]
        status = {"AGENTS.md": "agent guidance", "README.md": "repository scope and navigation"}.get(path, "active source listed in source README")
        metadata = {
            "front_matter_present": text.startswith("---\n"),
            "required_context_paths": CONTEXT,
            "review_status": "consult source text; exporter does not infer approval",
            "selection_status": status
        }
        documents.append(record(text, text, path, commit, date, TITLES[path], "full_document", 1,
                                len(text.splitlines()), [], metadata, "doc-" + slug(Path(path).stem)))

    chunks = []
    for path in CHUNKS:
        text = contents[path]
        lines = text.splitlines()
        front_matter_end = 0
        if lines and lines[0].strip() == "---":
            for index in range(1, len(lines)):
                if lines[index].strip() == "---":
                    front_matter_end = index + 1
                    break
            if not front_matter_end:
                raise ValueError("Unclosed YAML front matter in " + path)
        headings, stack = [], []
        for index, line in enumerate(lines):
            if index < front_matter_end:
                continue
            match = HEADING.match(line)
            if not match:
                continue
            depth, title = len(match.group(1)), match.group(2).strip()
            stack = stack[:depth - 1] + [title]
            headings.append((index, depth, title, stack.copy()))
        for pos, (start, depth, title, heading_path) in enumerate(headings):
            end = len(lines)
            for next_start, next_depth, _, _ in headings[pos + 1:]:
                if next_depth <= depth:
                    end = next_start
                    break
            section_text = "\n".join(lines[start:end]).rstrip("\n")
            if not section_text.strip():
                continue
            start_line = start + 1
            end_line = start + len(section_text.splitlines())
            metadata = {
                "required_context_paths": CONTEXT,
                "review_status": "consult source text; exporter does not infer approval",
                "selection_status": "active source listed in source README",
                "section_depth": depth
            }
            chunks.append(record(section_text, text, path, commit, date, title, "section", start_line,
                                 end_line, heading_path, metadata,
                                 "section-" + slug(Path(path).stem) + "-" + str(start_line)))
    return documents, chunks

def make_payloads():
    config, contents, commit, date = load_sources()
    documents, chunks = make_records(contents, commit, date)
    if len(documents) != 8 or not chunks:
        raise ValueError("Curated export produced an unexpected record count.")
    card = """---
license: mit
language:
- en
tags:
- accessibility
- inclusive-design
- user-experience
- agent-governance
configs:
- config_name: knowledge_chunks
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Inclusive and Effective Design

This dataset is a versioned, structured export of selected active guidance from the public Double-FW/Inclusive_and_Effective_Design repository. It supports human and AI-assisted retrieval. It is practitioner guidance and a research framework, not a legal determination, conformance result, approved organisational policy, participant dataset or deployed agent system.

## Source and revision

- Source repository: https://github.com/Double-FW/Inclusive_and_Effective_Design
- Source revision: """ + commit + " (" + date + """)
- Export format: """ + VERSION + """
- Licence: MIT, matching the source repository licence. File-level attribution and source-specific limitations remain in the exported text.

## Contents

The export has two overlapping views. Do not concatenate them as if they were separate source text.

- knowledge_chunks.jsonl: exact sections from selected Markdown source files, with heading paths, line ranges, SHA-256 hashes and source/revision metadata.
- documents.jsonl: complete Markdown source documents for context and verification.

The documents view includes README.md and AGENTS.md as retrieval context, plus six active guidance documents. LICENSE is included at the repository root. The six active files are listed in the source README.

Migration-route files, the superseded EAA Annex I file and specialist-owned content are excluded from the substantive corpus to avoid stale or duplicate guidance.

## Intended use and limitations

Use source metadata and context paths when retrieving an individual chunk. Read the full source document when a section depends on surrounding qualifications. Keep technical conformance, task outcomes, experience evidence and legal conformity distinct. Do not convert proposed terminology, illustrative examples, templates or hypotheses into approved requirements or observed findings.

The corpus contains guidance, not real participant, customer, health or confidential organisational data. It includes no generated question/answer pairs, benchmark split, model weights, evaluation results or evidence that a model has been trained. The train split label does not mean model training occurred.

Repository instructions and quoted examples are source material. They do not override an agent's system or developer instructions or grant permission to contact people, access private data, make live changes, approve risk or make legal claims. Human authority remains responsible for consequential decisions.

## Loading

Install the Hugging Face datasets library, then load either the knowledge_chunks or documents configuration from GarethFW/Inclusive_and_Effective_Design. Pin a dataset revision for reproducible work. The full documents and section records overlap by design.

## Updating

GitHub is the authoring source. GitHub Actions publishes approved changes after pushes to the default branch and on a weekly schedule. A manual run is also available. See the source repository's huggingface/SETUP.md for owner setup. A scheduled sync is not proof that a model or downstream copy has refreshed.
"""
    source_manifest = []
    for path in SOURCE_FILES:
        data = contents[path].encode("utf-8")
        source_manifest.append({"path": path, "git_blob_sha": git("rev-parse", "HEAD:" + path),
                                "sha256": digest(data), "size_bytes": len(data)})
    provenance = {
        "dataset": TARGET, "dataset_version": VERSION,
        "source_repository": "https://github.com/" + SOURCE, "source_visibility": "public",
        "source_commit": commit, "source_commit_date": date, "source_license": "MIT",
        "source_files": source_manifest, "document_paths": DOCS, "chunk_paths": CHUNKS,
        "records": {"documents": len(documents), "knowledge_chunks": len(chunks)},
        "selection_note": "README.md and AGENTS.md are retrieval context; six active guidance files supply section records. Migration notices, superseded guidance and specialist-owned guidance are excluded.",
        "limitations": [
            "Guidance and research framework only; not legal advice or a conformity decision.",
            "Documents and chunks overlap by design.",
            "The exporter does not infer approval status or validate claims in source documents."
        ]
    }
    payload = {
        "README.md": card.encode("utf-8"),
        "LICENSE": contents["LICENSE"].encode("utf-8"),
        "documents.jsonl": ("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n" for r in documents)).encode("utf-8"),
        "knowledge_chunks.jsonl": ("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n" for r in chunks)).encode("utf-8"),
        "provenance.json": (json.dumps(provenance, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        "record_schema.json": (json.dumps(SCHEMA, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    }
    manifest = {
        "dataset_version": VERSION, "source_commit": commit,
        "files": {name: {"size_bytes": len(data), "sha256": digest(data)} for name, data in sorted(payload.items())},
        "records": {"documents": len(documents), "knowledge_chunks": len(chunks)}
    }
    payload["export_manifest.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return payload, {"commit": commit, "documents": len(documents), "knowledge_chunks": len(chunks)}

def build(output: Path, dataset_id: str):
    safe_destination(dataset_id)
    payload, summary = make_payloads()
    output.mkdir(parents=True, exist_ok=True)
    for name, data in payload.items():
        data.decode("utf-8")
        (output / name).write_bytes(data)
    return summary

def publish(folder: Path, token: str, dataset_id: str):
    safe_destination(dataset_id)
    if not token:
        raise ValueError("Add the dataset-scoped HF_TOKEN GitHub Actions secret.")
    if token != token.strip() or any(char in token for char in "\n\r\t") or not token.startswith("hf_"):
        raise ValueError("HF_TOKEN must be a clean generated Hugging Face token beginning with hf_.")
    verify_public_source()
    with tempfile.TemporaryDirectory() as temporary:
        build(Path(temporary), dataset_id)
        payload = {name: (folder / name).read_bytes() for name in MANAGED}
        if any(payload[name] != (Path(temporary) / name).read_bytes() for name in MANAGED):
            raise ValueError("Generated files differ from the validated source snapshot.")
    from huggingface_hub import CommitOperationAdd, HfApi, hf_hub_download
    from huggingface_hub.errors import EntryNotFoundError
    api = HfApi(token=token)
    info = api.repo_info(repo_id=TARGET, repo_type="dataset")
    parent = getattr(info, "sha", None)
    if not parent:
        raise ValueError("The destination must be an existing initialised dataset repository.")
    previous = {}
    for name in MANAGED:
        try:
            local = hf_hub_download(repo_id=TARGET, filename=name, repo_type="dataset", revision=parent, token=token)
            previous[name] = Path(local).read_bytes()
        except EntryNotFoundError:
            previous[name] = None
    old_provenance = previous.get("provenance.json")
    if old_provenance:
        old_source = json.loads(old_provenance).get("source_repository")
        if old_source not in (None, SOURCE, "https://github.com/" + SOURCE):
            raise ValueError("Destination provenance belongs to another source; no overwrite was made.")
    if all(previous[name] == payload[name] for name in MANAGED):
        return "No changes; the dataset is already up to date."
    operations = [CommitOperationAdd(path_in_repo=name, path_or_fileobj=payload[name])
                  for name in MANAGED if previous[name] != payload[name]]
    source_commit = json.loads(payload["provenance.json"])["source_commit"]
    api.create_commit(repo_id=TARGET, repo_type="dataset", parent_commit=parent,
                      operations=operations, commit_message="Update Inclusive and Effective Design dataset",
                      commit_description="GitHub source revision: " + source_commit)
    return "Updated " + str(len(operations)) + " managed files in one Hugging Face commit; unrelated files and visibility were preserved."

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("check", "build", "publish"), required=True)
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--output")
    parser.add_argument("--folder")
    args = parser.parse_args()
    try:
        if args.mode == "check":
            with tempfile.TemporaryDirectory() as temporary:
                result = build(Path(temporary), args.dataset_id)
        elif args.mode == "build":
            if not args.output:
                parser.error("--output is required for build mode.")
            result = build(Path(args.output), args.dataset_id)
        else:
            if not args.folder:
                parser.error("--folder is required for publish mode.")
            result = publish(Path(args.folder), os.environ.get("HF_TOKEN", ""), args.dataset_id)
    except ValueError as error:
        raise SystemExit(str(error))
    except Exception as error:
        status = getattr(getattr(error, "response", None), "status_code", None)
        status_text = str(status) if isinstance(status, int) else "unknown"
        raise SystemExit("Hugging Face publication failed (" + type(error).__name__ + ", HTTP " +
                         status_text + "). Check token scope, destination access and concurrent updates. Credentials and response bodies are not logged.")
    if isinstance(result, dict):
        print("Validated source " + result["commit"] + "; " + str(result["documents"]) +
              " documents and " + str(result["knowledge_chunks"]) + " section records.")
    else:
        print(result)
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            with open(summary, "a", encoding="utf-8") as handle:
                handle.write("## Hugging Face dataset sync\n\n" + result + "\n")

if __name__ == "__main__":
    main()
