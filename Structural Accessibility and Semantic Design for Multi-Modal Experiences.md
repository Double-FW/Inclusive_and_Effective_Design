# Structural Accessibility and Semantic Design for Multi-Modal Experiences

## Knowledge Base for Generative Design Systems and LLM-Supported Workflows

------------------------------------------------------------------------

# Foundations of Structural Accessibility

## Explainer

Digital experiences are interpreted differently by different users
depending on how they perceive, navigate, and interact with information.
People using assistive technologies often rely on structural cues rather
than visual layout to understand content. When structure is unclear or
inconsistent, users may become disoriented, unable to find information,
or unable to complete tasks. Structural clarity benefits everyone
because it improves comprehension, scanning, memory, and confidence in
navigation.

Accessible structure is therefore not a technical requirement but a
design principle concerned with meaning, hierarchy, and orientation.
Designers shape structure through grouping, sequencing, and emphasis,
and those decisions directly affect whether a product feels
understandable and usable.

## Core Design Principle

Structure should communicate:

-   What the experience is about
-   Where the user is
-   What parts exist
-   How those parts relate to each other
-   What can be done next

Structure must be perceivable both visually and non-visually.

## Design Approaches and Methodologies

Designers should approach structure as an information architecture
problem before visual styling begins. This involves mapping content into
logical groupings and identifying the primary purpose of each screen or
page. A useful methodology is to begin with a conceptual outline,
similar to a document table of contents, and then translate that outline
into interface components. Designers should also consider progressive
disclosure, ensuring that complexity is introduced gradually rather than
overwhelming users.

Another effective approach is structural mirroring, where visual
groupings correspond directly to semantic groupings. When the visual
hierarchy matches the underlying meaning, cognitive effort is reduced.
Designers should also validate structure by asking whether someone
unfamiliar with the interface could predict where information should be
located.

## Prompt Design Guidance for LLM Use

When asking an LLM to generate or refine designs, prompts should
explicitly request:

-   Clear structural hierarchy
-   Multi-modal interpretation support
-   Compatibility with assistive technologies
-   Logical grouping of content

Example prompt guidance:

"Design this interface with a clear hierarchical structure that can be
understood by both visual users and assistive technology users. Ensure
sections are grouped logically, labelled clearly, and navigable in
multiple ways including sequential navigation."

------------------------------------------------------------------------

# Hierarchical Headings and Content Organisation

## Explainer

Headings function as the primary navigational framework for many users,
especially those who cannot visually scan content. Without a logical
hierarchy, users may struggle to understand relationships between topics
or locate information efficiently. Poor heading structure can create
confusion, increase cognitive load, and reduce trust in the interface. A
well-designed heading hierarchy acts as both a map and a summary of the
experience.

Headings also support users with cognitive differences by breaking
information into manageable chunks and providing predictable structure.
For people using assistive technologies, headings can form a navigable
outline that enables rapid movement between sections.

## Design Approaches and Methodologies

Designers should treat headings as structural labels rather than visual
decoration. Each heading should introduce a meaningful section and
describe its purpose clearly. The hierarchy should reflect relationships
between ideas rather than visual size preferences.

A useful method is hierarchical decomposition, where the main topic is
divided into major sections, and each section is then divided further
into subtopics. Designers should avoid skipping levels because doing so
disrupts mental models of structure. Headings should also be concise and
informative, prioritising clarity over creativity.

Another methodology is outline testing, where designers remove all body
text and evaluate whether the remaining headings alone communicate the
full structure of the experience. If the structure is unclear, the
hierarchy needs refinement.

## Prompt Design Guidance for LLM Use

Prompts should include explicit instructions about hierarchical clarity
and descriptive labelling.

Example prompt guidance:

"Generate content with a clear hierarchy of headings that accurately
describe each section. Ensure the structure forms a logical outline that
can be navigated independently of the body text and remains
understandable when read sequentially or non-sequentially."

------------------------------------------------------------------------

# Containers, Regions, and Grouping

## Explainer

Containers define meaningful groupings of content and help users
understand how information is organised. Without clear grouping,
interfaces can feel chaotic, overwhelming, or difficult to interpret.
Users who rely on assistive technologies particularly benefit from
containers because they provide shortcuts for navigating between major
regions of content.

Grouping also supports cognitive processing by reducing complexity and
clarifying relationships between elements. When containers are poorly
defined or inconsistent, users may struggle to understand boundaries
between sections or identify where tasks begin and end.

## Design Approaches and Methodologies

Designers should think of containers as conceptual regions rather than
purely visual boxes. Each container should represent a meaningful
purpose, such as navigation, main content, supporting information, or
actions. A consistent layout pattern across screens helps users build
familiarity and predictability.

One effective methodology is structural zoning, where the interface is
divided into distinct functional areas before detailed design begins.
Designers should also apply proximity principles, ensuring related items
appear close together and unrelated items are visually separated.

Designers should also consider progressive grouping, where complex
interfaces are broken into nested layers of containers that reflect task
flow.

## Prompt Design Guidance for LLM Use

Prompts should explicitly request logical grouping and region
identification.

Example prompt guidance:

"Create a layout that groups related elements into clearly defined
regions. Each region should have a distinct purpose and be
understandable to users navigating with assistive technologies as well
as visually."

------------------------------------------------------------------------

# Landmarks and Orientation

## Explainer

Landmarks provide orientation points within an experience, allowing
users to quickly move between major areas. For users who cannot rely on
visual scanning, landmarks function like signposts that indicate where
important sections begin. Without landmarks, navigation can become
inefficient and disorienting.

Landmarks also help users skip repetitive content and focus on what
matters most. This is particularly important for people who navigate
sequentially using keyboards or assistive technologies.

## Design Approaches and Methodologies

Designers should establish consistent landmark patterns across the
entire experience. Major areas such as primary content, navigation, and
supporting information should appear in predictable locations.
Consistency enables users to build spatial memory and reduces effort
when moving between screens.

A useful approach is orientation mapping, where designers define the
purpose and position of each major region early in the design process.
Designers should also ensure that only one primary content area exists
per screen to avoid ambiguity.

## Prompt Design Guidance for LLM Use

Prompts should request orientation clarity and predictable layout
regions.

Example prompt guidance:

"Design the interface with clearly identifiable regions that help users
understand where they are and move between sections efficiently. Ensure
the main content area is distinct and consistently positioned across
screens."

------------------------------------------------------------------------

# Navigation and Route Changes

## Explainer

When users move between screens or sections, they need clear
confirmation that something has changed. Without feedback, users may
become confused, uncertain, or lost. This is particularly challenging
for people using assistive technologies because visual transitions may
not be perceivable.

Navigation should communicate location, context, and progression.
Changes should feel predictable and understandable regardless of how the
user navigates.

## Design Approaches and Methodologies

Designers should consider navigation as a continuity experience rather
than isolated screens. Each transition should reinforce orientation by
clearly indicating the new location and maintaining consistent
structural elements. Navigation indicators should show current position
and available options.

One effective methodology is state continuity design, where designers
ensure that transitions preserve user context and expectations. Another
approach is feedback layering, where visual, textual, and structural
cues all communicate the same change.

## Prompt Design Guidance for LLM Use

Prompts should explicitly request navigation clarity and orientation
cues.

Example prompt guidance:

"Design transitions between screens so that users always know when a new
section has loaded, where they are now, and how to return. Ensure
changes are communicated through multiple sensory channels including
text and structure."

------------------------------------------------------------------------

# Roles, Meaning, and Interaction Semantics

## Explainer

Users need to understand what interface elements are and how to interact
with them. When meaning is unclear, people may hesitate, make errors, or
abandon tasks. Assistive technology users depend heavily on semantic
meaning to interpret controls and actions.

Clear roles and states help users predict outcomes and feel confident in
interaction. This is particularly important for people with cognitive
differences who benefit from consistent patterns and predictable
behaviour.

## Design Approaches and Methodologies

Designers should prioritise recognisable interaction patterns and
familiar behaviours. Controls should look and behave consistently with
user expectations. Designers should also ensure that changes in state,
such as selection or expansion, are clearly communicated through
multiple cues.

A useful approach is interaction affordance mapping, where designers
identify what each element allows the user to do and ensure that this is
visually and structurally communicated. Another methodology is
redundancy of cues, where information is conveyed through more than one
channel.

## Prompt Design Guidance for LLM Use

Prompts should emphasise semantic clarity and interaction meaning.

Example prompt guidance:

"Ensure all interactive elements clearly communicate their purpose,
state, and how they can be used. Design interactions so they are
understandable through visual cues, text descriptions, and structural
context."

------------------------------------------------------------------------

# Multi-Modal Accessibility Design

## Explainer

Different users perceive information through different sensory channels.
Some rely on vision, some on hearing, some on touch, and many use
combinations. Multi-modal design ensures that information is not
dependent on a single sensory mode.

When experiences rely on only one channel, barriers are created.
Multi-modal design increases resilience, inclusivity, and usability for
everyone.

## Design Approaches and Methodologies

Designers should provide redundant pathways for understanding
information. Visual information should be supported by text or
structure, and interactive feedback should be communicated through
multiple channels. Designers should also consider timing, motion, and
attention demands to avoid overload.

A useful methodology is sensory equivalence mapping, where designers
identify how each piece of information can be perceived through
different modalities. Another approach is inclusive scenario testing,
imagining how someone with different sensory abilities would experience
the design.

## Prompt Design Guidance for LLM Use

Prompts should explicitly require multi-modal outputs.

Example prompt guidance:

"Generate a design that communicates information through multiple
modalities, ensuring that content is understandable visually,
structurally, and through assistive technologies without relying on a
single sensory channel."

------------------------------------------------------------------------

# Consistency and Predictability

## Explainer

Consistency reduces cognitive effort and builds user confidence. When
patterns change unexpectedly, users must relearn behaviours, which can
be frustrating and exclusionary. Predictable experiences are especially
important for people with cognitive differences or anxiety.

Consistency also improves efficiency for assistive technology users who
rely on familiar structures to navigate quickly.

## Design Approaches and Methodologies

Designers should create reusable patterns and apply them consistently
across the experience. Layout, navigation, and interaction behaviours
should remain stable unless there is a clear reason to change them.
Designers should also consider system thinking, ensuring that components
behave consistently in different contexts.

A useful method is pattern libraries based on behaviour rather than
appearance. Another approach is cognitive walkthroughs, evaluating
whether users can predict outcomes before interacting.

## Prompt Design Guidance for LLM Use

Prompts should emphasise pattern reuse and predictability.

Example prompt guidance:

"Design using consistent patterns across screens so users can predict
how elements behave. Ensure navigation, layout, and interaction
behaviours remain stable throughout the experience."

------------------------------------------------------------------------

# Writing Effective Prompts for Accessible Design Outcomes

## Explainer

LLMs generate outputs based on instructions provided. If accessibility
is not explicitly requested, it may not be included. Designers must
therefore treat prompts as design specifications that include
accessibility intent.

Well-written prompts help ensure outputs are inclusive, multi-modal, and
structurally clear. Poor prompts risk producing inaccessible or
incomplete results.

## Prompt Methodology

Effective prompts should include:

-   Structural clarity requirements
-   Multi-modal communication expectations
-   Assistive technology compatibility
-   Inclusive interaction considerations
-   Clear hierarchy and grouping instructions

Designers should also request explanations from the LLM about how
accessibility was addressed, enabling evaluation and refinement.

------------------------------------------------------------------------

# Using This Knowledge Base in an AI agent

This knowledge base should be used to guide a generative system to:

-   Produce structurally accessible designs
-   Generate inclusive content hierarchies
-   Recommend grouping and navigation patterns
-   Evaluate accessibility risks
-   Provide prompt improvement suggestions

The system should prioritise inclusion, clarity, and user orientation
over compliance.
