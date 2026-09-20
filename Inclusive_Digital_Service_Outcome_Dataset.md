---
title: "Inclusive Digital Service Outcome Dataset"
subtitle: "A canonical Layer 2 dataset for defining and evaluating functional, equitable, and experiential outcomes"
version: "1.0"
date: "2026-09-20"
status: "Canonical inclusive-outcome framework"
canonical_layer: "Layer 2"
authority_type: "Organisational design and research framework"
legal_status: "Not legislation, a technical standard, a conformity statement, or legal advice"
repository: "https://github.com/Double-FW/Inclusive_and_Effective_Design"
scope: "Digital products, services, websites, applications, platforms, content, transactions, support channels, and connected customer journeys"
relationship_to_governance_layers:
  layer_1: "EAA Scope and Applicability Gate determines whether and how the European Accessibility Act applies."
  layer_2: "This dataset defines functional and experiential outcomes and the evidence used to understand them."
  layer_3: "EAA Evidence and Conformity Record Model governs requirement conclusions and claims."
retrieval_unit: "Each IDSO outcome record and governance section is intended to be independently retrievable with its definitions and limits."
ai_ingestion_guidance:
  - "Treat this as an organisational design and research dataset, not a list of statutory EAA requirements."
  - "Do not convert a positive outcome finding into WCAG conformance or EAA conformity."
  - "Do not convert a WCAG pass into proof of task success, autonomy, equivalence, satisfaction, or enjoyment."
  - "Preserve differences between user groups, tasks, environments, technologies, releases, and service channels; do not rely on an average alone."
  - "Treat WCAG and other applicable standards as strong baselines, while recognising that they do not measure every service or experience outcome."
  - "Do not approve a legal exception, baseline departure, alternative solution, conformity conclusion, or public claim."
  - "When evidence is missing or conflicting, return 'insufficient evidence' and identify the next decision-relevant evidence."
  - "Never convert a Layer 2 outcome finding automatically into a Layer 1 scope outcome or Layer 3 legal-requirement conclusion."
---

# Inclusive Digital Service Outcome Dataset

## Purpose

This dataset defines the outcomes an inclusive digital service should seek to deliver and the evidence that can be used to evaluate them. It extends beyond technical accessibility to include whether people can complete their goals with reasonable effort, autonomy, privacy, dignity, equivalent service quality, confidence, satisfaction, and—where it is part of the service purpose—enjoyment.

The dataset is designed for requirements, design, research, testing, procurement, release, monitoring, and AI-assisted governance. It supports services ranging from simple content journeys to specialist and highly interactive systems such as trading platforms, CAD tools, collaborative workspaces, games, and professional applications.

It does not decide whether the European Accessibility Act applies and does not establish legal conformity. Those decisions belong to the [EAA Scope and Applicability Gate](https://github.com/Double-FW/Articles_and_other_LLM_Training_Resources/blob/main/EAA_Scope_and_Applicability_Gate.md) and the [EAA Evidence and Conformity Record Model](https://github.com/Double-FW/Articles_and_other_LLM_Training_Resources/blob/main/EAA_Evidence_and_Conformity_Record_Model.md).

## Core proposition

> An inclusive service is not demonstrated by a checklist total. It is demonstrated by evidence that relevant people can perceive, understand, operate, complete, recover, choose, and participate in the service without avoidable disadvantage—and that unresolved differences remain visible.

Technical conformance, functional access, usability, equality of outcome, and experience quality are related but not interchangeable:

| Dimension | Question answered | Example evidence | It does not establish alone |
|---|---|---|---|
| Legal applicability | Which obligations apply to this subject? | Applicable law, facts, operator role, jurisdiction, dates, and approved Layer 1 decision. | Whether people succeed in practice. |
| Standards conformance | Does the defined implementation meet the selected standard in the tested scope? | Clause-level technical evaluation and governed test results. | Complete service quality, satisfaction, or legal conformity. |
| Functional access | Can a person obtain information and operate the necessary functions using their chosen access approach? | Manual and assistive-technology evaluation, task observation, and implementation evidence. | Reasonable effort, equivalent treatment, or a satisfactory experience. |
| Task and service outcome | Can the person achieve the intended goal across the complete journey? | Task success, accuracy, time, errors, recovery, support, and operational data. | How the experience felt or whether every legal duty was met. |
| Experiential outcome | Does the service support autonomy, privacy, dignity, confidence, satisfaction, and relevant enjoyment? | Qualitative research, validated measures, behavioural evidence, complaints, and longitudinal evidence. | Legal permission to disregard an applicable requirement. |

## Governing principles

1. **Standards are strong baselines.** WCAG and other applicable technical standards provide structured, testable protections. They are not optional merely because a different outcome measure is available.
2. **Outcomes extend the baseline.** User expectation, effort, autonomy, privacy, dignity, equivalence, satisfaction, and enjoyment may expose important service quality that standards do not fully measure.
3. **Averages do not erase exclusion.** Report material differences between groups, tasks, environments, and technologies. A strong average can coexist with a severe barrier.
4. **A pass cannot cancel a poor outcome.** Technical success and poor user evidence must both remain visible and trigger investigation where they conflict.
5. **A positive outcome cannot rewrite a failure.** User success, preference, or satisfaction does not convert a failed applicable test into conformance.
6. **Complexity is contextual.** Specialist services may require information density, precision, speed, customisation, or expert workflows. Evaluate whether complexity is necessary, learnable, controllable, and supported—not whether every interface is simple.
7. **Evidence must fit the decision.** Statistical significance may strengthen some population claims but is neither required for every finding nor sufficient for every decision.
8. **People are not test instruments.** Research with disabled people must be ethical, accessible, fairly compensated where appropriate, and clear about how evidence will influence decisions.
9. **No group carries the organisation's risk.** Participants provide evidence; they do not approve legal conformity, exceptions, risk acceptance, or release.
10. **Outcomes require monitoring.** A conclusion can change with content, users, technology, suppliers, environments, service policy, or evidence.

## How to use the dataset

For each product, service, feature, or journey:

1. identify the decision and the precise service scope;
2. select the applicable outcome records rather than assuming every outcome has equal relevance;
3. identify populations, access approaches, tasks, environments, and consequences of failure;
4. translate selected outcomes into measurable acceptance conditions;
5. map the relevant standards, policies, and legal requirements without merging their authority;
6. plan complementary technical, behavioural, qualitative, quantitative, and operational evidence;
7. record findings, differences, contradictions, uncertainty, and missing evidence;
8. take corrective action or use the appropriate governed decision route; and
9. pass the evidence to Layer 3 where an EAA requirement or claim decision is needed.

Selection must be justified. An outcome marked `not relevant` needs a rationale tied to the service purpose, affected people, and decision—not convenience or lack of current data.

## Outcome record structure

Each canonical outcome below contains:

- a stable ID and title;
- the desired service outcome;
- design and evaluation questions;
- example indicators;
- evidence considerations; and
- a misuse warning.

Indicators are examples, not universal thresholds. Teams must set thresholds proportionate to the service, task criticality, affected population, legal and policy baseline, and consequence of failure.

## Functional access outcomes

### [IDSO-01] Information can be perceived

**Outcome:** People can detect and obtain the information needed for the task through an access approach appropriate to them.

**Design and evaluation questions:**

- Is essential information available without reliance on a single sensory characteristic?
- Can content adapt to relevant display, text, audio, magnification, contrast, and personalisation needs?
- Do state changes, warnings, status, and feedback remain available through the person's access approach?

**Example indicators:** availability of equivalent alternatives; successful identification of essential information; missed-information rate; reading or listening accuracy; operation under relevant display and environmental conditions.

**Evidence considerations:** combine relevant standards checks with manual evaluation and task evidence. An alternative must communicate the purpose and material information, not merely exist.

**Misuse warning:** Multiple formats do not automatically provide equivalent information, and one user's successful access does not prove universal perceivability.

### [IDSO-02] Meaning and relationships are preserved

**Outcome:** People can determine the meaning, structure, sequence, status, and relationships necessary to understand and use the service.

**Design and evaluation questions:**

- Do headings, labels, groupings, instructions, data relationships, and reading order convey the intended structure?
- Are visual, auditory, spatial, and programmatic meanings consistent?
- Can people distinguish current state, available action, and consequence?

**Example indicators:** comprehension accuracy; correct navigation of structure; identification of relationships; mismatch between visual and non-visual representations; errors attributable to unclear state.

**Evidence considerations:** evaluate complex tables, diagrams, canvases, dashboards, timelines, and collaborative state with the technologies and strategies used in context.

**Misuse warning:** Linearisation is not always an equivalent representation of spatial or multidimensional information; the service may need an alternative interaction model.

### [IDSO-03] Functions can be operated and controlled

**Outcome:** People can initiate, adjust, pause, stop, and complete relevant functions using compatible input and interaction approaches.

**Design and evaluation questions:**

- Is any action unnecessarily restricted to one input method, gesture, precision level, posture, strength, reach, or vocal capability?
- Can people discover controls, understand their state, and receive confirmation?
- Can time limits, motion, animation, media, and automatic change be controlled where needed?

**Example indicators:** operation through declared input methods; target error rate; unintended activation; task interruption; control discovery; ability to pause or adjust time-dependent activity.

**Evidence considerations:** test full workflows and transient states, not only individual controls. Include keyboard, touch, pointer, voice, switch, and other methods when relevant.

**Misuse warning:** The presence of keyboard support does not by itself establish efficient or understandable operation.

### [IDSO-04] People can orient and navigate

**Outcome:** People can determine where they are, what is available, where an action will lead, and how to move or return within the service.

**Design and evaluation questions:**

- Are navigation, focus, location, progress, ownership, and collaborative presence understandable?
- Are repeated patterns sufficiently consistent while allowing task-appropriate flexibility?
- Can people resume after interruption or move between channels without losing essential context?

**Example indicators:** route-finding success; wrong-turn frequency; time to locate a function; loss of context; successful return or resumption; focus and navigation errors.

**Evidence considerations:** include long journeys, deep information structures, modal and canvas interfaces, multiple windows, real-time collaboration, and cross-channel hand-offs where relevant.

**Misuse warning:** Consistency should reduce uncertainty, not prohibit necessary differences between distinct functions.

### [IDSO-05] Information and actions can be understood

**Outcome:** People can understand content, choices, instructions, consequences, and system responses well enough to make informed decisions.

**Design and evaluation questions:**

- Is language appropriate to the audience, domain, and consequence of misunderstanding?
- Are unfamiliar concepts, specialist terms, abbreviations, data, and risk explained at the point of need?
- Does the interface reveal what happened and what to do next?

**Example indicators:** comprehension accuracy; decision confidence; requests for clarification; abandonment attributable to uncertainty; incorrect choices; successful explanation in the participant's own words.

**Evidence considerations:** plain language is valuable but not synonymous with removing necessary professional terminology. Specialist tools may need progressive disclosure, definitions, training, examples, and consistent expert vocabulary.

**Misuse warning:** Reading-age scores do not measure the accuracy, usefulness, tone, or contextual clarity of content.

### [IDSO-06] The service works with user-selected technology and settings

**Outcome:** People can use relevant browsers, devices, assistive technologies, input methods, display settings, and personal preferences without avoidable loss of information or function.

**Design and evaluation questions:**

- Does the service expose reliable semantics, states, names, values, and events?
- Does it tolerate relevant changes in text size, spacing, orientation, zoom, contrast, motion, and platform preferences?
- Are compatibility limits disclosed and supported by a reasonable route to resolution?

**Example indicators:** successful use across the declared environment matrix; regression frequency; preference retention; failures caused by unsupported configurations; availability and quality of alternatives.

**Evidence considerations:** define a risk-based environment matrix. Universal compatibility is rarely demonstrable, but arbitrary restriction to one configuration is not acceptable.

**Misuse warning:** `Works with a screen reader` is too broad unless the technology, version, browser, platform, task, and evidence are stated.

### [IDSO-07] Use does not introduce avoidable health or safety risk

**Outcome:** People can use or leave the service without avoidable exposure to seizure triggers, vestibular effects, physical strain, distress, dangerous error, or loss of critical information.

**Design and evaluation questions:**

- Are flashing, motion, sound, time pressure, repeated action, and sensory load controlled?
- Can a person stop, reduce, defer, or avoid non-essential effects?
- Do critical services fail safely and provide accessible warnings and recovery?

**Example indicators:** exposure against relevant thresholds; ability to disable effects; physical effort; dangerous-error rate; successful recognition of warnings; safe exit and recovery.

**Evidence considerations:** combine standards-based measurement with contextual assessment. High-consequence services require stronger assurance than low-consequence presentation effects.

**Misuse warning:** Do not rely on participants to test exposure that may be unsafe when technical inspection or safer simulation can answer the question.

### [IDSO-08] Communication and support remain accessible

**Outcome:** People can request, receive, understand, and act on help through an appropriate communication route without losing privacy, status, or service entitlement.

**Design and evaluation questions:**

- Are support and complaints available without dependence on speech, hearing, vision, fine movement, or one synchronous channel?
- Can support staff understand and maintain accessibility adjustments?
- Does escalation preserve context and avoid repeatedly requiring disclosure?

**Example indicators:** successful support contact; wait and resolution time by channel; repeat-contact rate; abandoned support; accessible complaint completion; quality and consistency of resolution.

**Evidence considerations:** evaluate the human and operational service, not only the contact interface.

**Misuse warning:** An accessible website does not compensate for an inaccessible support or complaints process.

## Task and service-quality outcomes

### [IDSO-09] Intended tasks can be completed accurately

**Outcome:** People can achieve the intended goal, including consequential actions such as authentication, consent, configuration, creation, purchase, payment, submission, communication, and cancellation.

**Design and evaluation questions:**

- Can the complete task be finished in its realistic state and context?
- Is success equivalent in substance, rather than merely technically possible?
- Are dependencies, third-party components, and channel changes included?

**Example indicators:** completion rate; accuracy; verified end state; abandonment; assistance required; blocked dependencies; outcome quality.

**Evidence considerations:** define success before testing and distinguish independent completion, completion with ordinary support, and completion only through an exceptional workaround.

**Misuse warning:** Reaching the final screen does not establish that the intended transaction or outcome was correct.

### [IDSO-10] Time and effort are reasonable

**Outcome:** People can complete the service without disproportionate cognitive, physical, sensory, or administrative effort.

**Design and evaluation questions:**

- Are unnecessary steps, repetition, precision, memory, attention switching, waiting, and re-entry removed?
- Does the service support efficient expert use as well as learnable first-time use where both matter?
- Are additional demands imposed on disabled people or users of alternative approaches?

**Example indicators:** task time; steps and interactions; repeated input; focus movement; physical actions; help requests; perceived effort; fatigue; difference between relevant groups or access approaches.

**Evidence considerations:** compare like with like and interpret speed alongside accuracy, confidence, learning, and user preference. A slower method may still be preferred or safer.

**Misuse warning:** Speed alone is not usability, and a statistically significant time difference may be practically trivial—or conceal a severe barrier for a smaller group.

### [IDSO-11] Errors can be prevented, understood, and recovered from

**Outcome:** People can avoid foreseeable mistakes, recognise what went wrong, preserve valid work, correct the problem, and continue without disproportionate penalty.

**Design and evaluation questions:**

- Are constraints and consequences apparent before commitment?
- Are errors identified in an accessible, specific, and non-blaming way?
- Can consequential actions be reviewed, corrected, cancelled, or reversed where appropriate?

**Example indicators:** error rate and severity; error recognition; recovery success and time; data loss; repeat error; support dependency; confidence after recovery.

**Evidence considerations:** include interruptions, expired sessions, validation, destructive actions, concurrent edits, network failure, and authentication failure where relevant.

**Misuse warning:** Preventing all error is neither possible nor always desirable; the objective is proportionate prevention and effective recovery.

### [IDSO-12] People can act autonomously

**Outcome:** People can make choices and complete private or personal tasks without unnecessary reliance on another person.

**Design and evaluation questions:**

- Does the service create avoidable dependence on a colleague, carer, family member, support agent, or sighted person?
- Can people independently inspect, verify, authorise, and reverse consequential actions?
- Are supported and delegated use available where chosen, without making dependence the default?

**Example indicators:** independent completion; unchosen assistance; hand-off to another person; ability to verify state; control over delegation; reported agency.

**Evidence considerations:** distinguish chosen collaboration or support from forced dependence.

**Misuse warning:** Successful completion with another person's help is not evidence of autonomous access.

### [IDSO-13] Privacy, security, and consent are equivalent

**Outcome:** People can understand and control personal information, identity, security, and consent without having to sacrifice accessibility or disclose more than others.

**Design and evaluation questions:**

- Can authentication, verification, consent, and privacy controls be completed through accessible methods?
- Does an accessibility route expose information to another person or create weaker security?
- Can people understand what is collected, shared, retained, and changed?

**Example indicators:** independent secure completion; unnecessary disclosure; consent comprehension; use of weaker alternatives; privacy incidents; ability to review or withdraw consent.

**Evidence considerations:** involve security, privacy, accessibility, and affected users. Avoid treating one discipline as permission to ignore another.

**Misuse warning:** A nominally secure process is not equivalent if it routinely forces disabled people to disclose credentials or personal information to obtain help.

### [IDSO-14] The service outcome is equivalent

**Outcome:** People receive a materially comparable outcome in availability, choice, quality, accuracy, timeliness, cost, status, and recourse.

**Design and evaluation questions:**

- Does the accessible route provide the same material products, features, prices, deadlines, information, and protections?
- Is an alternative channel slower, more expensive, less private, restricted to shorter hours, or lower in quality?
- Do delays or workarounds change the real opportunity available?

**Example indicators:** outcome parity; feature and choice availability; completion time including queues; price or fee differences; hours of access; resolution and remedy; missed opportunity.

**Evidence considerations:** equivalence does not always mean an identical interface. A different route can be equivalent when it delivers a comparable material outcome without additional disadvantage.

**Misuse warning:** `Alternative available` is insufficient unless the alternative's quality and consequences are evaluated.

### [IDSO-15] Service continuity and change are manageable

**Outcome:** People can rely on the service, retain necessary settings and work, and adapt to changes without sudden loss of access or disproportionate relearning.

**Design and evaluation questions:**

- Are accessibility settings, saved work, context, and known workflows preserved where appropriate?
- Are material changes communicated accessibly and introduced with support?
- Can people recover from outages, updates, supplier changes, and discontinued channels?

**Example indicators:** regression rate; setting persistence; data or context loss; successful migration; relearning effort; support demand after change; accessible fallback availability.

**Evidence considerations:** monitor over time. A one-off pre-release study cannot establish continuing reliability.

**Misuse warning:** Technical uptime alone does not show that a service remains accessible after change.

## Experiential and relationship outcomes

### [IDSO-16] People feel confident and in control

**Outcome:** People can form an accurate expectation of what will happen, recognise progress, make informed choices, and trust their ability to complete or stop the interaction.

**Design and evaluation questions:**

- Does the service reduce justified uncertainty without providing false reassurance?
- Are risks, commitments, progress, and consequences visible at the right time?
- Can people confirm, reconsider, and exit?

**Example indicators:** confidence before and after action; prediction accuracy; hesitation; repeated checking; abandonment attributable to uncertainty; perceived control.

**Evidence considerations:** self-report should be interpreted alongside behaviour and outcome accuracy. High confidence with incorrect results is a warning, not success.

**Misuse warning:** Confidence is not a substitute for actual task success or reliable system behaviour.

### [IDSO-17] People are treated with dignity and respect

**Outcome:** The service avoids unnecessary stigma, blame, infantilisation, exposure, or other treatment that diminishes the person, their identity, or their role.

**Design and evaluation questions:**

- Are language, imagery, defaults, error messages, assistance, and disability-related choices respectful?
- Does the service make an individual publicly identify an access need unnecessarily?
- Are people represented as participants and customers rather than problems to be managed?

**Example indicators:** reported respect and belonging; unwanted disclosure; stigmatising content or process; tone findings; avoidance attributable to treatment; complaint themes.

**Evidence considerations:** meanings vary by context and community. Co-design and qualitative research can identify problems that generic sentiment measures miss.

**Misuse warning:** Positive brand language cannot compensate for inaccessible or unequal service delivery.

### [IDSO-18] People are satisfied with the experience

**Outcome:** People judge the service as acceptably useful, usable, reliable, and appropriate to their goals and expectations.

**Design and evaluation questions:**

- Are satisfaction differences associated with access approach, disability, task, environment, or service outcome?
- Do expectations reflect prior exclusion, low alternatives, or fear of losing access?
- Does satisfaction remain stable after repeated or consequential use?

**Example indicators:** task-level satisfaction; service satisfaction; recommendation or reuse intention; expectation gap; qualitative reasons; change over time; differences between relevant groups.

**Evidence considerations:** satisfaction is a valuable outcome and risk signal. Use accessible measures and interpret ratings alongside success, effort, autonomy, equivalence, and qualitative explanation.

**Misuse warning:** Satisfaction alone neither proves accessibility nor excuses a failed requirement. People may report satisfaction despite barriers, limited alternatives, or adapted expectations.

### [IDSO-19] People can participate and collaborate equitably

**Outcome:** People can contribute, create, communicate, review, coordinate, and influence shared work with comparable visibility, agency, and timeliness.

**Design and evaluation questions:**

- Can people perceive collaborators, authorship, changes, comments, conflicts, presence, and shared state?
- Can they contribute through appropriate modes without being excluded from real-time or asynchronous decisions?
- Are accessible outputs retained when content moves between tools or formats?

**Example indicators:** contribution and review success; missed updates; turn-taking; conflict resolution; attribution accuracy; participation latency; exclusion from shared artefacts or meetings.

**Evidence considerations:** test multi-user conditions. Individual task testing cannot reveal every collaborative barrier.

**Misuse warning:** Access to the same workspace does not establish equal participation or influence.

### [IDSO-20] Enjoyment and expressive value are available where material

**Outcome:** When play, creativity, exploration, aesthetic experience, storytelling, or social connection is part of the service purpose, disabled people can experience and shape that value rather than receive only functional access.

**Design and evaluation questions:**

- Does the accessible experience retain challenge, discovery, humour, atmosphere, expression, and social connection where relevant?
- Are alternatives equivalent in purpose and creative value rather than reduced to information delivery?
- Can people personalise the experience without losing its essential character?

**Example indicators:** enjoyment; engagement; return; creative expression; perceived equivalence of experience; social participation; reasons for preference or exclusion.

**Evidence considerations:** qualitative evidence may be central because enjoyment is contextual and multidimensional. Use behavioural measures cautiously; time spent can indicate delight, difficulty, or inability to exit.

**Misuse warning:** Enjoyment is not a universal legal criterion, but excluding it from an entertainment, cultural, creative, or social service can make the evaluation meaningless.

## Population and context lenses

Outcome selection must consider the people, capabilities, access approaches, and contexts relevant to the service. These lenses generate questions; they are not diagnoses, fixed personas, or proof of legal applicability.

Consider use:

- without vision or with limited vision;
- without colour perception or with altered contrast perception;
- without hearing or with limited hearing;
- without speech or with limited vocal capability;
- with limited manipulation, strength, reach, dexterity, mobility, or stamina;
- with limited memory, attention, comprehension, literacy, numeracy, language fluency, or executive function;
- with photosensitivity, vestibular sensitivity, sensory sensitivity, fatigue, pain, or fluctuating capacity;
- with different input, output, assistive, adaptive, and personalisation technologies;
- with multiple or intersecting access requirements;
- in noisy, bright, dark, mobile, stressful, time-pressured, low-bandwidth, shared, interrupted, or private environments; and
- as a novice, occasional user, expert, administrator, creator, reviewer, collaborator, customer, or support agent.

Some capability categories resemble functional performance criteria in Annex I of Directive (EU) 2019/882. They are legal requirements only when Layer 1 establishes the relevant legal route. Their broader use here is an inclusive-design practice.

Do not assume that one participant represents everyone who shares a diagnosis, technology, or capability. Do not infer a diagnosis from observed behaviour.

## Specialist and complex services

Complexity can be essential to the purpose of trading, CAD, data analysis, clinical, creative, engineering, collaborative, and other professional systems. The correct question is not simply `Can this be made simpler?` It is:

- Which complexity is intrinsic to the task and which results from avoidable design choices?
- Can novice, occasional, and expert routes coexist without restricting capability?
- Are dense, spatial, temporal, or rapidly changing relationships available through an effective alternative representation or interaction model?
- Can people customise views, shortcuts, notifications, density, timing, and input without losing essential information?
- Are high-speed and safety-critical actions both efficient and protected from consequential error?
- Can users learn, practise, recover, and obtain accessible expert support?
- Does collaboration preserve equivalent presence, authorship, awareness, and control?

A service is not excused from applicable obligations because it is specialised. Equally, an outcome framework should not force a specialist interface into a consumer-content pattern that destroys its purpose. Any alternative design or departure must follow the governance controls below.

## Evidence model

Use complementary evidence because no single method answers every outcome question.

| Method | Particularly useful for | Important limitation |
|---|---|---|
| Standards and clause-level evaluation | Repeatable technical baselines and known barrier prevention. | Does not measure every complete task or experiential outcome. |
| Expert review | Early identification, complex pattern analysis, and interpretation. | Reviewer judgement and coverage must be declared. |
| Manual and assistive-technology evaluation | Functional behaviour in declared states and environments. | A technology configuration or evaluator cannot represent all use. |
| Moderated task research | Success, strategy, comprehension, effort, recovery, autonomy, and qualitative explanation. | Observation effects and small samples limit some generalisations. |
| Unmoderated research | Broader task evidence in participants' own environments. | Less control and reduced ability to investigate causes in the moment. |
| Co-design and participatory work | Needs, concepts, language, alternatives, priorities, and lived context. | Participation is not validation of the final implementation or transfer of decision accountability. |
| Surveys and accessible outcome measures | Self-reported patterns, comparisons, expectations, satisfaction, and change. | Sampling, response access, adapted expectations, and question design affect validity. |
| Product analytics | Behaviour at scale, funnels, errors, latency, recurrence, and change over time. | Disability and access approach may be unknown; behaviour does not explain cause. |
| Complaints, support, and incidents | Real barriers, consequences, workarounds, and operational patterns. | Under-reporting and inaccessible channels make absence weak evidence. |
| Experiments and comparative studies | Relative performance of alternatives and some causal questions. | Ethical, practical, sampling, and external-validity limits must be stated. |
| Longitudinal monitoring | Learning, adaptation, regression, continuity, and sustained outcomes. | More time and attrition; intervening changes complicate interpretation. |

### Evidence sufficiency

Evidence is sufficient only for the decision and scope it can support. Record:

- the decision question and proposed claim;
- selected outcomes and why they matter;
- populations, access approaches, tasks, contexts, and consequences;
- method, sample rationale, environment, technology, and version;
- observed results and participant explanation;
- quantitative uncertainty, effect size, and practical importance where applicable;
- missing or under-represented people and conditions;
- contradictory evidence and negative cases;
- researcher or evaluator competence and independence;
- what the evidence supports and does not establish; and
- the next evidence or action required.

Statistical significance is appropriate only where a defined hypothesis, measure, sample, and analysis support that inference. It must not be imposed on exploratory or diagnostic qualitative research. Conversely, a vivid individual finding should not be generalised to population prevalence without suitable evidence. A single case can still be decisive where it demonstrates a reproducible severe exclusion or failure against a required outcome.

## Interpreting outcome findings

Use the following vocabulary for each selected outcome:

| Finding | Meaning |
|---|---|
| `supported` | Sufficient evidence supports the defined outcome for the stated people, tasks, contexts, version, and period. |
| `partly supported` | The outcome is supported in some defined areas but material differences or limitations remain. Split the scope where possible. |
| `not supported` | Evidence shows that the outcome is not achieved in some or all of the defined scope. |
| `insufficient evidence` | Evidence is missing, stale, contradictory, or too limited for the proposed finding. |
| `not evaluated` | The outcome was selected but evaluation has not been completed. |
| `not relevant with rationale` | The outcome does not materially relate to the defined service purpose or decision. The approved rationale is retained. |

Do not use a numerical roll-up to hide a `not supported` outcome. A dashboard may summarise status, but the underlying finding, affected population, consequence, and uncertainty must remain available.

### Relationship to legal-requirement conclusions

Layer 2 and Layer 3 use deliberately different vocabularies because they answer different questions.

| Layer 2 finding | What it means for Layer 3 |
|---|---|
| `supported` | Relevant evidence input only. It must not be converted automatically into `supported as met`. |
| `partly supported` | Split the affected scope and investigate. It may support different legal conclusions for different parts, but does not determine them. |
| `not supported` | Investigate affected legal requirements and standards. It does not by itself identify which legal requirement is `not met`. |
| `insufficient evidence` | May contribute to `cannot conclude` where the missing outcome evidence is material to the legal requirement. A human reviewer must decide. |
| `not evaluated` | Does not mean `not assessed` for every related legal requirement; check the complete Layer 3 evidence set. |
| `not relevant with rationale` | An inclusive-outcome selection decision only. It must never be converted into `not applicable by approved scope decision`; legal non-applicability requires Layer 1 approval. |

No automated crosswalk may change an outcome finding into a legal conclusion. Layer 3 must retain the finding ID, assess its relevance to the exact requirement, and record the human reasoning.

## Resolving contradictions

Contradictory evidence is information, not a data-cleaning problem. When results disagree:

1. confirm that the evidence concerns the same release, task, state, environment, population, and outcome;
2. check method validity, accessibility, sample, competence, and source authority;
3. identify whether different people or strategies produce genuinely different outcomes;
4. retain minority and negative cases, especially where consequences are severe;
5. collect targeted evidence only where it can change a decision;
6. record the unresolved contradiction and limit any claim; and
7. pass possible legal or standards implications to Layer 3 rather than resolving them through an experience score.

## Evidence-based flexibility and departures

The dataset permits contextual design judgement; it does not permit teams to declare legal or standards exceptions.

An alternative to an organisational design baseline may be considered when:

- the applicable law, regulation, contract, standard, and policy permit the decision route;
- the baseline and proposed alternative are explicit;
- affected people, tasks, contexts, and consequences are identified;
- proportionate evidence supports equal or better outcomes without concealing disadvantaged subgroups;
- standards failures remain recorded as failures unless the standard's own conformance rules say otherwise;
- alternatives and less exclusionary options have been considered;
- residual disadvantage and uncertainty are explicit;
- a competent reviewer and authorised accountable owner approve the decision;
- permitted claims are limited; and
- monitoring, review triggers, and a review date are recorded.

Where the alternative is asserted to satisfy an applicable EAA requirement, it is an `alternative technical solution` and must use the legal and evidence controls in Layer 3. Where a failure is merely accepted for a period, it is an `exception`, not a successful outcome or departure.

## Minimum outcome evidence set

For a material service decision, retain:

- the service boundary, release, tasks, channels, environments, and period;
- selected outcome IDs and selection rationale;
- relevant population and context lenses;
- legal, standards, contractual, and organisational mappings with their authority kept distinct;
- outcome-specific acceptance conditions and thresholds;
- research and evaluation plan, including accessible participation and ethics;
- raw or appropriately protected evidence and accessible research records;
- outcome findings, differences, uncertainty, and contradictions;
- issues, actions, owners, target dates, and retest or follow-up;
- approved exceptions or departures and their limits;
- Layer 3 links where legal requirements or claims are implicated; and
- monitoring signals and review triggers.

## Stop conditions

Do not describe an outcome as `supported` when:

- the people, task, context, version, or success definition is absent;
- only a proxy measure exists for a material outcome and its limitations are not stated;
- only automated evidence represents a manual, behavioural, or experiential question;
- a material subgroup difference, negative case, or contradiction has been removed by averaging;
- assistance was required but the finding is described as autonomous completion;
- an inaccessible alternative or support channel is treated as equivalent;
- satisfaction is used to conceal failure, exclusion, excessive effort, or lack of choice;
- an expert judgement or synthetic persona is presented as research with disabled people;
- missing evidence is represented as a positive finding; or
- the conclusion is being used as an EAA or WCAG claim without the appropriate Layer 1 and Layer 3 controls.

## Roles and decision rights

| Role | Responsibility |
|---|---|
| Product or service owner | Defines the service decision, funds evidence, owns corrective action, and recommends exceptions or departures. |
| Design and content | Translate selected outcomes into interaction, information, visual, non-visual, multimodal, and service requirements. |
| Engineering and architecture | Implement testable behaviour, interoperability, resilience, personalisation, and evidence capture. |
| QA and accessibility evaluation | Connect outcome requirements to valid tests, preserve result limits, and identify conflicts with standards evidence. |
| Research | Select proportionate methods, recruit relevant participants, provide accessible participation, analyse differences, and report uncertainty. |
| Disabled participants and community partners | Contribute lived expertise, needs, strategies, priorities, and evaluation evidence without inheriting organisational accountability. |
| Operations, support, and complaints teams | Supply live-service evidence, protect accessible channels, and own response and monitoring. |
| Legal or compliance | Decide legal interpretation and advise where an outcome, alternative, or claim may affect an obligation. |
| Accountable owner or escalation authority | Approves organisational departures or accepts exceptions within documented authority. |
| AI or synthetic research system | Supports scenario generation, traceability, analysis, and gap detection; never substitutes for real user evidence where that evidence is required. |

## Synthetic personas and simulated evidence

Synthetic personas, simulations, automated agents, disability emulation, and AI-generated scenarios can help teams:

- identify questions and potential failure paths;
- diversify test cases and service contexts;
- check traceability and missing states;
- rehearse research plans; and
- prioritise where real evaluation may be most valuable.

They cannot establish lived experience, prevalence, satisfaction, dignity, autonomy, or actual compatibility with a person's technology and strategy. Label generated evidence as synthetic, preserve its source and assumptions, and prevent it from being merged with participant evidence.

## Outcome finding template

```yaml
finding_id: "IDSO-F-"
version: ""
decision_question: ""
service_scope:
  product_or_service: ""
  features_tasks_and_channels: []
  release_or_period: ""
  territories: []
selected_outcome:
  outcome_id: "IDSO-"
  selection_rationale: ""
population_and_context:
  populations_and_access_approaches: []
  environments_and_conditions: []
  consequences_of_failure: ""
acceptance_conditions_and_thresholds: []
authority_mappings:
  legal_requirement_ids: []
  standards_criteria: []
  contractual_requirements: []
  organisational_policies: []
evidence:
  evidence_ids: []
  methods: []
  sample_rationale: ""
  technologies_and_environments: []
  limitations_and_missing_groups: []
results:
  observations: []
  quantitative_results: []
  qualitative_findings: []
  group_or_context_differences: []
  negative_cases: []
  contradictory_evidence: []
finding: "supported | partly supported | not supported | insufficient evidence | not evaluated | not relevant with rationale"
rationale: ""
confidence:
  level: "high | moderate | low | insufficient"
  rationale: ""
does_not_establish: []
actions_and_owners: []
related_layer_3_evidence_ids: []
related_layer_3_requirement_conclusion_ids: []
review_triggers: []
next_review_date: ""
research_or_evaluation_owner: ""
competent_reviewer: ""
decision_owner: ""
decision_date: ""
```

## AI and autonomous-system controls

An AI system using this dataset must:

1. retrieve the smallest relevant outcome records and retain their IDs, version, definitions, and warnings;
2. ask for the service purpose, task, population, context, version, and decision before proposing a finding;
3. distinguish law, standards, contracts, organisational policy, research evidence, and generated interpretation;
4. maintain separate results for technical conformance, functional access, task outcome, and experiential outcome;
5. preserve disaggregated and negative evidence rather than optimising an average score;
6. label synthetic personas, simulations, and generated findings and prevent them from impersonating participant evidence;
7. avoid diagnosis or assumptions based on impairment labels;
8. propose evidence in proportion to the decision and state what each method can and cannot establish;
9. return `insufficient evidence` where the proposed finding is not supported;
10. route possible legal implications, alternative technical solutions, and claims to Layers 1 and 3; and
11. preserve a reconstructable record of inputs, sources, transformations, limitations, recommendations, and human decisions.

## Sources and related material

- [Web Content Accessibility Guidelines (WCAG) 2.2 — W3C Recommendation](https://www.w3.org/TR/WCAG22/)
- [Directive (EU) 2019/882 — official text](https://eur-lex.europa.eu/eli/dir/2019/882/oj)
- [European Commission — European Accessibility Act overview](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/european-accessibility-act-eaa_en)
- [Inclusive Design Thinking](Inclusive_Design_Thinking.md)
- [Inclusive Design Practice](Inclusive_Design_Practice.md)
- [Codesign](Codesign.md)
- [Multimodal UX Design](Multimodal_UX_Design.md)
- [Cognitive Design Principles](Cognitive%20Design%20Principles.md)
- [Accessible Games and Other Dynamic Content](Accessible_Games_and_other_Dynamic_Content.md)
- [The WCAG POUR Principles Reframed Through Emotional Outcomes for Branding Systems](The%20WCAG%20POUR%20principles%20reframed%20through%20emotional%20outcomes%20for%20branding%20systems.md)
- [Accessibility Test-Led Delivery Framework](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Accessibility_Test_Led_Delivery_Framework.md)
- [EAA Scope and Applicability Gate](https://github.com/Double-FW/Articles_and_other_LLM_Training_Resources/blob/main/EAA_Scope_and_Applicability_Gate.md)
- [EAA Evidence and Conformity Record Model](https://github.com/Double-FW/Articles_and_other_LLM_Training_Resources/blob/main/EAA_Evidence_and_Conformity_Record_Model.md)

## Replacement note

This document replaces `EAA Annex 1 — Training Dataset (Websites & Online Applications).md` as the canonical Layer 2 design and research dataset. The earlier file should be retained in repository history but removed from active retrieval or marked superseded when this file is adopted.

The replacement is deliberate: Annex I legal applicability belongs to Layer 1, while requirement conclusions and conformity claims belong to Layer 3. This Layer 2 file may map to those requirements, but it must not present all inclusive-design outcomes as if they were direct statutory duties.

## Use limitation

This dataset supports inclusive design and outcome evaluation. It does not replace applicable law, authoritative guidance, technical standards, competent accessibility evaluation, ethical research practice, or legal advice. A successful outcome finding is bounded by the people, tasks, contexts, technologies, version, period, and evidence stated in its record.
