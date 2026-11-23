# GitHub to Hugging Face dataset sync

Source: https://github.com/Double-FW/Inclusive_and_Effective_Design  
Destination: https://huggingface.co/datasets/GarethFW/Inclusive_and_Effective_Design

## One-time owner setup

The workflow needs a Hugging Face token with write access to this dataset. Do not share the token in chat or put it in a file.

1. In Hugging Face token settings, create a fine-grained token for only GarethFW/Inclusive_and_Effective_Design and grant read and write access.
2. In the GitHub source repository, open Settings → Secrets and variables → Actions → New repository secret.
3. Name the secret HF_TOKEN, paste the token into the secret value and save.
4. Confirm this sync setup is on the default main branch.
5. Open the Hugging Face sync workflow, select Run workflow on main and inspect the result.
6. Confirm it succeeds and check the dataset Files and versions page for the new source revision.

The destination is fixed in the reviewed export configuration. No HF_DATASET_ID variable is needed, and a different destination stops before publication.

## Ongoing behaviour

- A push to main that changes an approved source document, exporter, configuration, README, AGENTS file, licence or workflow triggers a sync.
- A scheduled sync also runs every Monday at 07:23 UTC. GitHub may delay scheduled runs.
- A manual workflow run is available.
- Pull requests do not publish; publication is restricted to the default branch.
- If no managed files changed, the workflow creates no Hugging Face commit.
- One commit updates the dataset README, MIT licence copy, documents and section JSONL files, provenance, schema and export manifest. Other destination files such as .gitattributes and dataset visibility are preserved.
- The curated export includes README and AGENTS as context plus six active guidance documents. Migration notices, superseded guidance and specialist-owned content are excluded. The two dataset configurations overlap by design: complete documents and heading-level sections.
- The GitHub source must remain public. GitHub's read-only token checks that status; HF_TOKEN is available only to the publishing step.

If a run fails, read its workflow log. Common causes include a missing or incorrectly scoped token, an uninitialised destination, a changed source allowlist or changed MIT licence bytes. Never paste credentials into an issue, commit, log or chat.
