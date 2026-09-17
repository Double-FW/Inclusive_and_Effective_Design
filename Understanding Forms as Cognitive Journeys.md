# Understanding Forms as Cognitive Journeys

## Explainer

Forms are not simply data collection mechanisms; they are structured
conversations between a system and a human. When accessibility is not
considered, forms create cognitive load, uncertainty, and exclusion,
particularly for people with sensory, cognitive, mobility, or language
differences. Poorly designed forms can prevent users from completing
essential tasks such as registration, purchasing, or communication,
which directly impacts both user trust and organisational outcomes.
Accessible design reduces friction, increases confidence, and improves
completion rates for all users, not only those with disabilities.

## Design Approach

Design forms as progressive understanding journeys rather than static
interfaces. Each step should clarify intent, reinforce context, and
support user memory.

A strong methodology includes: - Defining the purpose of the form before
designing fields. - Mapping user mental models rather than system data
structures. - Minimising cognitive effort through clarity,
predictability, and consistency. - Designing for interruption and
recovery.

## LLM Prompt Design Guidance

Generate outputs that: - Explain task purpose clearly. - Include
step‑by‑step journeys. - Provide persistent context cues. - Describe
multimodal accessibility.

------------------------------------------------------------------------

# Labels and Meaning: Communicating Intent Clearly

## Explainer

Labels provide meaning. Without clear labels, users cannot determine
what information is required or how to interact with a control. This is
especially critical for people using assistive technology or those with
memory or language processing differences.

## Design Approach

Labels must be: - Persistent - Close to the control - Written in plain
language - Consistent across modalities

Treat labels as micro‑conversations guiding users safely through tasks.

## LLM Prompt Design Guidance

Ensure prompts request: - Persistent visible labels - Matching spoken
and visual wording - Plain language suitable for diverse literacy levels

------------------------------------------------------------------------

# Accessible Names and Multimodal Interpretation

## Explainer

Interactive elements have both visual and machine‑interpretable
identities. When these differ, barriers emerge for users relying on
speech or screen reading.

## Design Approach

Design with semantic equivalence: - Match visible and spoken wording -
Provide text alternatives for icons - Ensure meaning is clear out of
context

## LLM Prompt Design Guidance

Request descriptions of: - Visual meaning - Assistive interpretation -
Interaction semantics

------------------------------------------------------------------------

# Layout and Spatial Relationships

## Explainer

Spatial relationships communicate structure. Poor placement increases
cognitive effort, especially for people using magnification or small
screens.

## Design Approach

Follow predictable patterns: - Labels before inputs - Logical vertical
flow - Consistent alignment - Clear grouping through proximity

## LLM Prompt Design Guidance

Prompts should request: - Layout hierarchy descriptions - Zoom and
reflow considerations - Spatial relationship explanations

------------------------------------------------------------------------

# Grouping Related Inputs

## Explainer

Users understand information through grouping. Disconnected fields
increase mental effort and confusion.

## Design Approach

Treat related inputs as single conceptual questions: - Identify logical
clusters - Provide concise group titles - Avoid mixing unrelated
concepts

## LLM Prompt Design Guidance

Explain: - Group logic - Conceptual purpose - Assistive perception of
grouping

------------------------------------------------------------------------

# Instructions and Supporting Information

## Explainer

Some inputs require explanation. Without guidance, users may guess
incorrectly or abandon tasks.

## Design Approach

Provide instructions only when necessary: - Place near the input - Keep
concise - Use examples when possible

## LLM Prompt Design Guidance

Request: - Contextual help text - Plain language examples - Relationship
to inputs

------------------------------------------------------------------------

# Required and Optional Fields

## Explainer

Users must understand what is mandatory. Confusion causes frustration
and abandonment.

## Design Approach

Prefer marking optional fields: - Include only necessary inputs -
Communicate requirements consistently - Avoid symbol‑only indicators

## LLM Prompt Design Guidance

Explain how requirements are communicated across modalities.

------------------------------------------------------------------------

# Input Types and Interaction Controls

## Explainer

Choosing appropriate controls reduces effort and errors, particularly
for users with motor or cognitive differences.

## Design Approach

Use familiar patterns: - Match control to intent - Prefer simplicity -
Ensure predictability

## LLM Prompt Design Guidance

Explain why controls minimise user effort for diverse abilities.

------------------------------------------------------------------------

# Validation and Error Prevention

## Explainer

Errors are inevitable. Supportive validation determines whether users
recover or abandon tasks.

## Design Approach

Design validation as support: - Prevent errors - Preserve input - Avoid
disruptive timing

## LLM Prompt Design Guidance

Generate feedback that is supportive, specific, and actionable.

------------------------------------------------------------------------

# Error Messages and Recovery

## Explainer

Users need clear guidance to recover from errors. Vague messages
increase abandonment.

## Design Approach

Effective errors are: - Specific - Polite - Actionable - Positioned near
inputs

## LLM Prompt Design Guidance

Provide messages that explain problems and solutions clearly.

------------------------------------------------------------------------

# Submission Behaviour and Predictability

## Explainer

Unexpected changes disorient users. Predictable interaction builds
confidence.

## Design Approach

Ensure: - Explicit user actions trigger changes - Clear completion
controls - Predictable outcomes

## LLM Prompt Design Guidance

Describe interaction responses across modalities.

------------------------------------------------------------------------

# Feedback After Submission

## Explainer

Users need confirmation and next steps after submission to avoid
uncertainty.

## Design Approach

Provide: - Clear confirmation - Next actions - Explicit success or
failure communication

## LLM Prompt Design Guidance

Explain how outcomes are communicated visually and through assistive
technologies.

------------------------------------------------------------------------

# Buttons and Calls to Action

## Explainer

Buttons are commitment points. If unclear or hidden, users lose
confidence.

## Design Approach

Design clear decision points: - Descriptive language - High visibility -
Avoid unexplained disabled states

## LLM Prompt Design Guidance

Explain recognition and activation across abilities.

------------------------------------------------------------------------

# Progressive Enhancement and Resilience

## Explainer

Design must remain usable across devices and technologies to ensure
inclusion.

## Design Approach

Design from core functionality outward: - Prioritise essential
interactions - Add enhancements safely - Maintain usability everywhere

## LLM Prompt Design Guidance

Describe the core experience independent of technology.

------------------------------------------------------------------------

# Multimodal Design Principles for AI‑Generated Interfaces

## Explainer

Generative systems often default to visual outputs unless instructed
otherwise, creating accessibility barriers.

## Design Approach

Design for multiple sensory channels: - Semantic descriptions - Reading
order - Interaction states - Alternative representations

## Universal Prompt Pattern

1.  Purpose
2.  User journey
3.  Visual hierarchy
4.  Semantic meaning
5.  Assistive interpretation
6.  Feedback behaviour
7.  Interaction predictability
8.  Multimodal considerations

------------------------------------------------------------------------

# Designer Mindset: Accessibility as Quality

## Explainer

Accessibility is an indicator of design maturity. Inclusive design
improves clarity, trust, and success rates for everyone.

## Design Approach

Adopt an inclusion‑first mindset: - Assume diversity of ability - Design
for clarity - Validate against user needs

------------------------------------------------------------------------
