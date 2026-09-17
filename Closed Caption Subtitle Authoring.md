# Closed Caption Subtitle Authoring

## 1. Foundations

### 1.1 Purpose of Subtitles

#### Provide Access to Audio Content

- Requirement: Ensure subtitles convey the full meaning of spoken audio for all viewers, including those with hearing loss.
- Rationale: Subtitles are a primary accessibility mechanism but are also widely used by general audiences.
- Conditions: Applies to all subtitle creation scenarios.
- Dependencies: Editing, Timing, Synchronisation

#### Support Broad Audience Usage

- Requirement: Design subtitles to be usable by both hearing-impaired and non-hearing-impaired viewers.
- Rationale: A significant proportion of subtitle users do not have hearing impairments.
- Conditions: Applies to all content types.
- Dependencies: Readability, Timing, Presentation

---

### 1.2 Subtitle Type Definition

#### Use Closed Subtitles

- Requirement: Provide subtitles as a separate, user-toggleable track rather than embedding them in video.
- Rationale: Allows users to control subtitle visibility and supports multiple formats.
- Conditions: Applies to all compliant subtitle delivery.
- Dependencies: File Format, Delivery Systems

---

### 1.3 Audience and Roles

#### Support Multiple Stakeholders

- Requirement: Ensure subtitle guidance supports authors, editors, developers, and quality controllers.
- Rationale: Subtitle production involves multiple roles requiring consistent standards.
- Conditions: Applies to all subtitle workflows.
- Dependencies: Governance, Quality Control

---

### 1.4 Knowledge Requirements

#### Distinguish Editorial and Technical Skills

- Requirement: Separate editorial guidance from technical implementation knowledge.
- Rationale: Editorial tasks require general understanding, while technical tasks require specialised knowledge.
- Conditions: Applies when designing workflows or training materials.
- Dependencies: File Format, Tooling

---

### 1.5 Guideline Scope

#### Apply Cross-Platform Rules by Default

- Requirement: Apply rules universally unless explicitly constrained to a specific platform.
- Rationale: Ensures consistency across delivery environments.
- Conditions: Applies unless platform-specific constraints are defined.
- Exceptions: Platform-specific rules for online or broadcast delivery.

---

### 1.6 Subtitle Quality Philosophy

#### Balance Competing Constraints

- Requirement: Balance fidelity to audio with readability, timing, and visual clarity.
- Rationale: Subtitle creation involves trade-offs that cannot be resolved by rigid rules.
- Conditions: Applies in all editing and presentation decisions.
- Dependencies: Editing, Timing, Line Breaks, Visual Context

#### Prioritise Viewer Comprehension

- Requirement: Optimise subtitles for clarity and comprehension rather than strict literal accuracy when conflicts arise.
- Rationale: Overly literal subtitles can reduce readability and usability.
- Conditions: Applies when constraints conflict.
- Dependencies: Editing Strategy

---

### 1.7 Decision-Making Framework

#### Evaluate Context Before Editing

- Requirement: Assess speech speed, visual content, and scene context before making editing decisions.
- Rationale: Context determines appropriate subtitle strategy.
- Conditions: Applies to all subtitle authoring tasks.
- Dependencies: Editing, Timing, Synchronisation

#### Adapt to Content Complexity

- Requirement: Adjust subtitle strategies for complex scenes, rapid dialogue, or high visual density.
- Rationale: High complexity reduces viewer processing capacity.
- Conditions: Applies in fast-paced or visually dense scenes.
- Dependencies: Timing, Editing

---

### 1.8 Content Inclusion Principles

#### Preserve Meaningful Audio

- Requirement: Include all meaningful spoken content unless constrained by timing or readability.
- Rationale: Subtitles provide access to the full narrative.
- Conditions: Applies when time and space allow.
- Exceptions: Omit content only when necessary for clarity or timing.

#### Avoid Unnecessary Omission

- Requirement: Do not remove words or phrases without justification.
- Rationale: Unnecessary omission reduces informational fidelity.
- Conditions: Applies during editing.
- Dependencies: Editing Rules

---

### 1.9 Non-Speech Information Handling

#### Include Essential On-Screen Text

- Requirement: Subtitle any on-screen text that is not legible but provides important context.
- Rationale: Ensures access to all relevant information.
- Conditions: Applies when visual text is unclear or inaccessible.
- Exceptions: Omit irrelevant or off-topic on-screen text.
- Dependencies: Visual Context Awareness

---

### 1.10 Consistency and Standardisation

#### Maintain Structural Consistency

- Requirement: Apply consistent formatting, structure, and rules across all subtitles.
- Rationale: Consistency improves readability and predictability.
- Conditions: Applies across entire subtitle set.
- Dependencies: All sections

#### Ensure Deterministic Output

- Requirement: Produce consistent results for identical inputs.
- Rationale: Enables automation, validation, and reuse.
- Conditions: Applies in automated or large-scale workflows.
- Dependencies: Governance, QA

---

### 1.11 Evolution and Maintenance

#### Support Incremental Updates

- Requirement: Update subtitle guidelines iteratively while maintaining backward compatibility where possible.
- Rationale: Subtitle standards evolve over time.
- Conditions: Applies to guideline management.
- Dependencies: Governance

---

### 1.12 Accessibility-First Design

#### Prioritise Accessibility Outcomes

- Requirement: Ensure all subtitle decisions improve accessibility outcomes.
- Rationale: Accessibility is the primary function of subtitles.
- Conditions: Applies to all decisions.
- Dependencies: All rules

---

## 2. Editing Text

### 2.1 Verbatim Integrity

#### Prefer Verbatim Speech

- Requirement: Use verbatim speech whenever timing and readability constraints allow.
- Rationale: Maximises access to the original audio content.
- Conditions: Applies when subtitle duration and space are sufficient.
- Exceptions: Edit only when required by timing, readability, or visual constraints.
- Dependencies: Timing, Line Length

#### Avoid Unnecessary Editing

- Requirement: Do not remove or alter words unless necessary.
- Rationale: Preserves meaning, tone, and nuance.
- Conditions: Applies to all subtitle editing decisions.
- Dependencies: Verbatim Integrity

---

### 2.2 Do Not Simplify Content

#### Preserve Linguistic Complexity

- Requirement: Retain original vocabulary and phrasing without simplification.
- Rationale: Simplification can be condescending and reduces fidelity.
- Conditions: Applies to all subtitle text.
- Dependencies: Audience Considerations

---

### 2.3 Preserve Lip-Readable Structure

#### Retain First and Last Words

- Requirement: Keep the beginning and end of spoken sentences when the speaker is visible.
- Rationale: These are most noticeable to lip-readers.
- Conditions: Applies when speakers are on screen.
- Dependencies: Synchronisation

#### Retain Lip-Readable Words

- Requirement: Preserve words that can be clearly lip-read.
- Rationale: Removing visible words creates a mismatch between audio and visual cues.
- Conditions: Applies in close-up or clearly visible speech.
- Exceptions: If unavoidable, replace with words with similar lip movement.
- Dependencies: Editing Strategy

---

### 2.4 Editing Strategy

#### Edit Evenly Across Sentences

- Requirement: Distribute edits across sentences rather than removing entire sentences.
- Rationale: Maintains continuity and meaning.
- Conditions: Applies when editing is required.
- Dependencies: Content Preservation

#### Preserve Sentence Continuity

- Requirement: Maintain logical and grammatical flow when editing.
- Rationale: Prevents confusion and misinterpretation.
- Conditions: Applies to all edited subtitles.
- Dependencies: Grammar Integrity

---

### 2.5 Preserve Meaningful Elements

#### Retain Names

- Requirement: Keep names used in dialogue.
- Rationale: Names are critical for narrative clarity.
- Conditions: Applies unless removal is unavoidable.
- Dependencies: Context Awareness

#### Retain Functional Words

- Requirement: Do not automatically remove short words that affect meaning.
- Rationale: Words such as conjunctions and qualifiers are often essential.
- Conditions: Applies during editing.
- Dependencies: Semantic Integrity

---

### 2.6 Preserve Speaker Style

#### Maintain Register and Tone

- Requirement: Reflect the speaker’s level of formality and tone.
- Rationale: Style conveys character and context.
- Conditions: Applies to all dialogue.
- Dependencies: Vocabulary Selection

#### Maintain Regional and Temporal Language

- Requirement: Preserve dialect, regional variation, and era-specific language.
- Rationale: Maintains authenticity.
- Conditions: Applies when such features are present.
- Dependencies: Context Awareness

#### Use Appropriate Contractions

- Requirement: Apply contractions only when consistent with the speaker’s style.
- Rationale: Incorrect use alters tone and meaning.
- Conditions: Applies during editing.
- Dependencies: Register Consistency

---

### 2.7 Maintain Context Across Subtitles

#### Consider Previous Subtitle

- Requirement: Ensure edits are consistent with preceding subtitles.
- Rationale: Prevents discontinuity.
- Conditions: Applies across sequential subtitles.
- Dependencies: Narrative Flow

---

### 2.8 Preserve Grammatical Integrity

#### Maintain Verb Forms

- Requirement: Avoid altering verb tense or structure unless necessary.
- Rationale: Changes can introduce grammatical errors or alter meaning.
- Conditions: Applies during editing.
- Dependencies: Grammar Integrity

---

### 2.9 Handle On-Screen Text

#### Subtitle Illegible Visual Text

- Requirement: Include important on-screen text that is not legible.
- Rationale: Ensures access to contextual information.
- Conditions: Applies when visual clarity is insufficient.
- Exceptions: Exclude irrelevant information.
- Dependencies: Visual Context Awareness

---

### 2.10 Strong Language Handling

#### Preserve Strong Language

- Requirement: Retain strong language unless removal is unavoidable, such as the content being produced for children.
- Rationale: Removing it alters tone and intent.
- Conditions: Applies unless external constraints require editing.
- Dependencies: Editorial Policy

#### Represent Masked or Altered Speech

- Requirement: Accurately represent censored, muted, or replaced words using clear textual indicators.
- Rationale: Maintains fidelity to the audio experience.
- Conditions: Applies when audio is altered.
- Dependencies: Audio Representation Rules

#### Limit Ellipsis Usage

- Requirement: Use no more than three dots to indicate missing or muted speech.
- Rationale: Prevents ambiguity and maintains consistency.
- Conditions: Applies when representing partial words or omissions.
- Dependencies: Formatting Rules

---

## 3. Line Breaks

### 3.1 Line Length Constraints

#### Limit Characters for Fixed-Width Systems

- Requirement: Restrict each subtitle line to a maximum of 37 characters in fixed-width environments.
- Rationale: Ensures compatibility with systems that have strict character limits.
- Conditions: Applies to fixed-width subtitle rendering environments.
- Dependencies: Platform Constraints

#### Constrain Width for Proportional Fonts

- Requirement: Ensure subtitle lines do not exceed the defined display region width.
- Rationale: Prevents overflow and maintains readability across variable font widths.
- Conditions: Applies to proportional font rendering systems.
- Dependencies: Typography, Display Region

#### Apply Dual Constraints for Multi-Platform Output

- Requirement: Satisfy both character count and display width constraints when targeting multiple platforms.
- Rationale: Ensures compatibility across all delivery formats.
- Conditions: Applies when subtitles are used across different systems.
- Dependencies: Platform Constraints

---

### 3.2 Sentence Structure

#### Use Single Sentence per Subtitle

- Requirement: Ensure each subtitle contains one complete sentence where possible.
- Rationale: Improves readability and comprehension.
- Conditions: Applies under normal speech pacing.
- Exceptions: May vary in live or rapid dialogue scenarios.
- Dependencies: Editing, Timing

---

### 3.3 Number of Lines

#### Limit Lines by Aspect Ratio

- Requirement: Use a maximum of two lines for standard formats and up to three lines for vertical formats.
- Rationale: Maintains readability and avoids obscuring content.
- Conditions: Applies based on video aspect ratio.
- Exceptions: Additional lines may be used if visual content is not obstructed.
- Dependencies: Visual Context

#### Optimise Line Distribution

- Requirement: Choose between one or multiple lines based on readability and visual balance.
- Rationale: Improves comprehension and reduces cognitive load.
- Conditions: Applies when formatting subtitles.
- Dependencies: Line Break Logic

---

### 3.4 Linguistic Line Breaking

#### Break at Natural Linguistic Points

- Requirement: Insert line breaks at punctuation or logical grammatical boundaries.
- Rationale: Supports natural reading patterns.
- Conditions: Applies to all multi-line subtitles.
- Dependencies: Grammar Integrity

#### Avoid Splitting Grammatical Units

- Requirement: Do not separate closely related words or phrases across lines.
- Rationale: Prevents disruption to comprehension.
- Conditions: Applies when structuring lines.
- Dependencies: Linguistic Cohesion

#### Avoid Breaking Within Words

- Requirement: Never split a word across lines.
- Rationale: Disrupts readability and comprehension.
- Conditions: Applies universally.
- Dependencies: Formatting Rules

---

### 3.5 Visual and Spatial Considerations

#### Consider Image Composition

- Requirement: Choose subtitle shape and placement to minimise obstruction of important visuals.
- Rationale: Preserves access to visual information.
- Conditions: Applies when determining line length and layout.
- Dependencies: Visual Context

#### Balance Subtitle Shape

- Requirement: Prefer layouts that minimise visual disruption while maintaining readability.
- Rationale: Subtitle shape affects how much of the image is obscured.
- Conditions: Applies when choosing between long and short lines.
- Dependencies: Visual Context

---

### 3.6 Speaker Differentiation via Layout

#### Support Speaker Identification

- Requirement: Structure lines to assist in distinguishing speakers when needed.
- Rationale: Improves clarity in multi-speaker scenarios.
- Conditions: Applies in dialogue-heavy scenes.
- Dependencies: Speaker Identification

---

### 3.7 Sentence Segmentation Across Subtitles

#### Segment Long Sentences Logically

- Requirement: Break long sentences across subtitles at natural clause boundaries.
- Rationale: Maintains coherence across segments.
- Conditions: Applies to extended dialogue.
- Dependencies: Linguistic Cohesion

#### Avoid Arbitrary Segmentation

- Requirement: Do not split sentences at random or unnatural points.
- Rationale: Reduces readability and comprehension.
- Conditions: Applies to all segmentation decisions.
- Dependencies: Grammar Integrity

---

### 3.8 Short Sentence Handling

#### Combine Short Sentences When Appropriate

- Requirement: Merge short sentences into a single subtitle when timing is limited.
- Rationale: Optimises reading efficiency.
- Conditions: Applies in fast-paced dialogue.
- Dependencies: Timing

---

### 3.9 Prioritisation of Constraints

#### Prioritise Editing and Timing Over Line Break Perfection

- Requirement: Favour accurate editing and appropriate timing over ideal line breaks when conflicts arise.
- Rationale: Content clarity and timing are more critical than formatting perfection.
- Conditions: Applies when constraints cannot all be satisfied.
- Dependencies: Editing, Timing

---

### 3.10 Manual Control of Line Breaks

#### Insert Line Breaks Manually

- Requirement: Manually define line breaks rather than relying on automated systems.
- Rationale: Automated breaks may not respect linguistic or visual rules.
- Conditions: Applies in subtitle authoring.
- Dependencies: Authoring Process

---

## 4. Timing

### 4.1 Reading Speed

#### Maintain Recommended Reading Speed

- Requirement: Keep subtitle reading speed within an optimal range aligned to natural reading ability.
- Rationale: Ensures viewers can comfortably read subtitles without cognitive overload.
- Conditions: Applies to all subtitle timing decisions.
- Dependencies: Editing, Subtitle Length

#### Align Timing with Speech Pace

- Requirement: Adjust subtitle timing to reflect the natural pace of spoken dialogue.
- Rationale: Maintains synchronisation between audio and text.
- Conditions: Applies to all dialogue.
- Dependencies: Synchronisation

---

### 4.2 Minimum Display Duration

#### Ensure Minimum Readability Time

- Requirement: Provide sufficient on-screen time for each subtitle based on its length.
- Rationale: Prevents subtitles from disappearing before they can be read.
- Conditions: Applies to all subtitles.
- Dependencies: Reading Speed

#### Avoid Overly Short Durations

- Requirement: Do not reduce subtitle duration below readability thresholds unless unavoidable.
- Rationale: Extremely short durations reduce comprehension.
- Conditions: Applies except in constrained scenarios.
- Exceptions: Shot changes, critical content constraints.
- Dependencies: Visual Timing

---

### 4.3 Conditions for Reduced Timing

#### Adjust for Shot Changes

- Requirement: Reduce subtitle duration to avoid conflicting with shot boundaries when necessary.
- Rationale: Maintains visual coherence between subtitles and edits.
- Conditions: Applies when subtitles would otherwise overlap inappropriate visual transitions.
- Dependencies: Shot Matching

#### Preserve Lip-Readable Content

- Requirement: Reduce timing rather than remove clearly visible spoken words.
- Rationale: Maintains alignment with visual speech cues.
- Conditions: Applies when lip-reading is important.
- Dependencies: Editing

#### Retain Critical Phrases

- Requirement: Allow reduced timing to preserve recognisable or essential phrases.
- Rationale: Maintains meaning and recognisability.
- Conditions: Applies when editing would distort meaning.
- Dependencies: Content Integrity

#### Preserve Humour and Impact

- Requirement: Adjust timing to maintain comedic or dramatic effect.
- Rationale: Timing is critical to narrative impact.
- Conditions: Applies to humour or dramatic moments.
- Dependencies: Narrative Context

#### Preserve Essential Information

- Requirement: Reduce timing rather than remove key informational content.
- Rationale: Ensures critical facts are retained.
- Conditions: Applies in informational or factual content.
- Dependencies: Content Priority

#### Handle Complex Content

- Requirement: Allow reduced timing when content cannot be simplified without loss of meaning.
- Rationale: Complex material may require full retention.
- Conditions: Applies to technical or dense dialogue.
- Dependencies: Editing

---

### 4.4 Conditions for Extended Timing

#### Allow Extra Time for Difficult Content

- Requirement: Increase subtitle duration for complex or unfamiliar words.
- Rationale: Supports comprehension of challenging content.
- Conditions: Applies to technical or uncommon language.
- Dependencies: Readability

#### Allow Extra Time for Multiple Speakers

- Requirement: Extend duration when subtitles contain dialogue from multiple speakers.
- Rationale: Increases cognitive load for the viewer.
- Conditions: Applies in multi-speaker subtitles.
- Dependencies: Speaker Identification

#### Allow Extra Time for Labels

- Requirement: Extend display duration when labels are used.
- Rationale: Labels require additional processing time.
- Conditions: Applies when speaker or sound labels are present.
- Dependencies: Speaker Identification

#### Allow Extra Time for Visual Complexity

- Requirement: Increase subtitle duration when the visual scene is complex.
- Rationale: Viewers must divide attention between reading and visual processing.
- Conditions: Applies in visually dense scenes.
- Dependencies: Visual Context

#### Allow Extra Time for Spatial Complexity

- Requirement: Extend duration when subtitles require additional eye movement.
- Rationale: Spatial positioning increases reading effort.
- Conditions: Applies when subtitles are positioned away from default reading areas.
- Dependencies: Positioning

#### Allow Extra Time for Numerical Content

- Requirement: Increase display duration for long or complex numerical values.
- Rationale: Numbers take longer to process.
- Conditions: Applies to numeric-heavy content.
- Dependencies: Content Type

#### Allow Extra Time Across Shot Changes

- Requirement: Extend subtitle duration when spanning multiple shots.
- Rationale: Visual transitions increase processing demands.
- Conditions: Applies when subtitles cross shot boundaries.
- Dependencies: Shot Matching

#### Align with Slow Speech

- Requirement: Extend subtitle timing to match slower speech delivery.
- Rationale: Maintains synchronisation and natural pacing.
- Conditions: Applies when speakers talk slowly.
- Dependencies: Synchronisation

---

### 4.5 Consistency in Timing

#### Maintain Consistent Timing Patterns

- Requirement: Apply consistent timing for subtitles of similar length and structure.
- Rationale: Predictability improves readability.
- Conditions: Applies across subtitle sequences.
- Exceptions: Variations allowed for contextual reasons.
- Dependencies: Timing Strategy

---

### 4.6 Gaps Between Subtitles

#### Use Meaningful Gaps

- Requirement: Insert gaps between subtitles when there is a pause in speech.
- Rationale: Reflects natural rhythm and prevents visual clutter.
- Conditions: Applies when silence or pauses occur.
- Dependencies: Speech Analysis

#### Enforce Minimum Gap Duration

- Requirement: Ensure gaps meet a minimum duration threshold.
- Rationale: Very short gaps create a jerky viewing experience.
- Conditions: Applies when inserting gaps.
- Dependencies: Timing Stability

#### Avoid Wasting Display Time

- Requirement: Use available time for subtitle display rather than unnecessary gaps.
- Rationale: Maximises information delivery.
- Conditions: Applies when timing allows.
- Dependencies: Efficiency

---

## 5. Synchronisation

### 5.1 Align Subtitles with Speech

#### Match Subtitle Onset to Speech Start

- Requirement: Display subtitles at the same time speech begins.
- Rationale: Supports alignment between visual cues and spoken content.
- Conditions: Applies to all spoken dialogue.
- Dependencies: Timing

#### Match Subtitle End to Speech End

- Requirement: Remove subtitles when the corresponding speech finishes.
- Rationale: Prevents re-reading and confusion.
- Conditions: Applies to all subtitle segments.
- Dependencies: Timing

---

### 5.2 Maintain Synchronisation Across Speakers

#### Sync Speaker Changes Precisely

- Requirement: Introduce subtitles for new speakers as they begin speaking.
- Rationale: Helps viewers correctly attribute dialogue.
- Conditions: Applies in multi-speaker scenarios.
- Dependencies: Speaker Identification

#### Apply Synchronisation to Off-Screen Audio

- Requirement: Synchronise subtitles with off-screen and voice-over speech.
- Rationale: Viewers rely on audio cues even when speakers are not visible.
- Conditions: Applies to narration and off-camera dialogue.
- Dependencies: Timing

---

### 5.3 Align with Speech Pace

#### Match Subtitle Rhythm to Dialogue

- Requirement: Ensure subtitle pacing reflects the rhythm of speech.
- Rationale: Maintains natural flow and comprehension.
- Conditions: Applies to all dialogue sequences.
- Dependencies: Timing

#### Limit Early or Late Display

- Requirement: Avoid displaying subtitles too early or leaving them too long after speech ends.
- Rationale: Misalignment disrupts comprehension.
- Conditions: Applies when synchronising subtitles.
- Dependencies: Timing

---

### 5.4 Ensure Subtitle Presence During Speech

#### Display Subtitles When Speech Occurs

- Requirement: Ensure subtitles are present whenever a speaker is talking.
- Rationale: Guarantees continuous access to spoken content.
- Conditions: Applies to all speech segments.
- Dependencies: Timing

#### Adapt to Speech Speed

- Requirement: Adjust subtitle timing to accommodate very fast or very slow speech.
- Rationale: Maintains readability and synchronisation.
- Conditions: Applies when speech deviates from normal pace.
- Dependencies: Editing, Timing

---

### 5.5 Minimise Lag

#### Reduce Delay Between Speech and Subtitles

- Requirement: Keep delay between speech and subtitle appearance as small as possible.
- Rationale: Improves comprehension and user experience.
- Conditions: Applies in all subtitle timing.
- Dependencies: Timing

#### Enforce Maximum Acceptable Lag

- Requirement: Prevent subtitles from appearing significantly after speech.
- Rationale: Excessive delay causes confusion.
- Conditions: Applies unless unavoidable.
- Dependencies: Editing

#### Recover Synchronisation in Sequences

- Requirement: Restore synchronisation by the end of a sequence if temporary lag occurs.
- Rationale: Prevents cumulative desynchronisation.
- Conditions: Applies in continuous dialogue sequences.
- Dependencies: Timing Strategy

---

### 5.6 Avoid Premature Information

#### Do Not Pre-empt Audio Events

- Requirement: Display subtitles only when the corresponding sound occurs.
- Rationale: Preserves narrative timing and impact.
- Conditions: Applies to sound effects and dramatic moments.
- Dependencies: Timing, Narrative Context

---

### 5.7 Separate Non-Overlapping Speakers

#### Avoid Overlapping Dialogue Representation

- Requirement: Do not display subtitles for multiple speakers unless they speak simultaneously.
- Rationale: Prevents confusion and cognitive overload.
- Conditions: Applies in multi-speaker interactions.
- Dependencies: Speaker Identification

---

## 6. Matching Shots

### 6.1 Align Subtitles with Shot Changes

#### Synchronise with Shot Boundaries

- Requirement: Align subtitle start and end times with shot transitions where possible.
- Rationale: Reduces viewer fatigue and improves coherence.
- Conditions: Applies in edited video content.
- Dependencies: Timing, Visual Context

---

### 6.2 Handle Mismatched Timing

#### Maintain Minimum Overhang Duration

- Requirement: If a subtitle extends beyond a shot change, ensure it remains visible long enough to be read comfortably.
- Rationale: Prevents abrupt disappearance.
- Conditions: Applies when exact alignment is not possible.
- Dependencies: Timing

---

### 6.3 Avoid Straddling Shots

#### Prevent Mid-Shot Transitions

- Requirement: Avoid subtitles that begin and end across different shots.
- Rationale: Improves visual consistency.
- Conditions: Applies when timing allows.
- Dependencies: Editing, Timing

---

### 6.4 Merge Across Short Shots

#### Combine Subtitles for Brief Shots

- Requirement: Merge dialogue across very short shots when individual timing is insufficient.
- Rationale: Ensures readability.
- Conditions: Applies when shots are too brief for standalone subtitles.
- Exceptions: Avoid if it reveals information prematurely.
- Dependencies: Timing, Narrative Context

---

### 6.5 Align with Speech Completion

#### End Subtitles with Speech

- Requirement: Avoid extending subtitles beyond the end of speech into subsequent shots.
- Rationale: Maintains synchronisation and clarity.
- Conditions: Applies when speech ends before a shot change.
- Dependencies: Timing

---

### 6.6 Respect Scene Boundaries

#### Do Not Cross Scene Changes

- Requirement: Do not carry subtitles into a different scene.
- Rationale: Scene transitions indicate narrative shifts.
- Conditions: Applies to all scene changes.
- Dependencies: Visual Context

---

### 6.7 Delay for Scene Transitions

#### Wait for Scene Change When Appropriate

- Requirement: Delay subtitle appearance until the new scene is visible when audio precedes visuals.
- Rationale: Prevents confusion when audio leads visual transitions.
- Conditions: Applies in pre-lapped audio scenarios.
- Exceptions: Use labels if delay is not possible.
- Dependencies: Speaker Identification

---

## 7. Identifying Speakers

### 7.1 Core Identification Strategy

#### Use Clear Speaker Identification Methods

- Requirement: Ensure each subtitle clearly indicates who is speaking.
- Rationale: Accurate speaker identification is essential for comprehension.
- Conditions: Applies in all multi-speaker scenarios.
- Dependencies: Colour, Positioning, Labels

---

### 7.2 Use Colour as Primary Method

#### Assign Unique Colours to Speakers

- Requirement: Use distinct colours to differentiate speakers.
- Rationale: Colour provides immediate visual distinction.
- Conditions: Applies when colour support is available.
- Dependencies: Colour System

#### Maintain Colour Consistency

- Requirement: Keep the same colour assigned to each speaker throughout.
- Rationale: Consistency avoids confusion.
- Conditions: Applies across the entire content.
- Dependencies: Speaker Tracking

#### Avoid Colour Reuse in Same Scene

- Requirement: Do not assign the same colour to multiple speakers appearing together.
- Rationale: Prevents ambiguity.
- Conditions: Applies in multi-speaker scenes.
- Exceptions: May reuse colours if speakers do not appear together.
- Dependencies: Scene Awareness

---

### 7.3 Structure Multi-Speaker Subtitles

#### Combine Speech Where Appropriate

- Requirement: Allow multiple speakers within a single subtitle when distinguishable.
- Rationale: Improves efficiency and reduces subtitle count.
- Conditions: Applies when clarity is maintained.
- Dependencies: Colour Differentiation

#### Separate Same-Colour Speakers

- Requirement: Use structural separation when speakers share the same visual style.
- Rationale: Prevents confusion when colour alone is insufficient.
- Conditions: Applies when colour cannot differentiate speakers.
- Dependencies: Formatting

---

### 7.4 Use Positioning

#### Use Positioning for Speaker Clarity

- Requirement: Place subtitles to reflect speaker location when helpful.
- Rationale: Spatial alignment supports identification.
- Conditions: Applies when visual context supports positioning.
- Dependencies: Visual Context

#### Avoid Positioning as Primary Method

- Requirement: Do not rely on positioning alone for identifying speakers.
- Rationale: Positioning can be ambiguous or unsupported.
- Conditions: Applies in modern subtitle workflows.
- Dependencies: Colour Usage

---

### 7.5 Use Dashes for Speaker Changes

#### Use Dashes When Colour Is Unavailable

- Requirement: Prefix each speaker’s line with a dash when colour cannot distinguish speakers.
- Rationale: Provides a clear textual cue.
- Conditions: Applies when colour is unavailable or insufficient.
- Dependencies: Formatting

#### Align Speaker Lines

- Requirement: Align lines consistently when using dashes.
- Rationale: Improves readability and structure.
- Conditions: Applies in multi-line subtitles.
- Dependencies: Layout

---

### 7.6 Use Single Quotes for Voice Distinction

#### Indicate Voice-Over Speech

- Requirement: Use single quotes to distinguish voice-over from on-screen speech when needed.
- Rationale: Prevents ambiguity between sources of speech.
- Conditions: Applies when confusion may occur.
- Dependencies: Speaker Context

#### Maintain Quote Continuity

- Requirement: Continue quotation marks across subtitles until speech ends.
- Rationale: Reflects continuous speech segments.
- Conditions: Applies in multi-subtitle voice-over sequences.
- Dependencies: Formatting

---

### 7.7 Use Double Quotes for Special Speech

#### Indicate Mechanical or Quoted Speech

- Requirement: Use double quotes to represent mechanical audio or direct quotations.
- Rationale: Differentiates speech types.
- Conditions: Applies to recorded or quoted dialogue.
- Dependencies: Formatting

---

### 7.8 Use Arrows for Off-Screen Speakers

#### Indicate Direction of Off-Screen Speech

- Requirement: Use directional markers to show where off-screen speech originates.
- Rationale: Helps locate unseen speakers.
- Conditions: Applies when speaker location is not visually clear.
- Dependencies: Positioning

#### Place Arrows Correctly

- Requirement: Position directional indicators adjacent to the relevant speech.
- Rationale: Ensures clarity and association.
- Conditions: Applies when using directional markers.
- Dependencies: Formatting

---

### 7.9 Use Labels When Necessary

#### Use Labels to Identify Speakers

- Requirement: Add speaker labels when other identification methods are insufficient.
- Rationale: Resolves ambiguity in complex scenarios.
- Conditions: Applies when multiple speakers cannot be clearly distinguished.
- Dependencies: Speaker Identification

#### Format Labels Clearly

- Requirement: Present labels distinctly from dialogue.
- Rationale: Improves readability and separation.
- Conditions: Applies when labels are used.
- Dependencies: Formatting

#### Use Generic Labels When Needed

- Requirement: Use descriptive labels when speaker identity is unknown.
- Rationale: Provides contextual clarity.
- Conditions: Applies when names are unavailable.
- Dependencies: Context Awareness

---

### 7.10 Handle Simultaneous Speech

#### Indicate Group Speech Clearly

- Requirement: Use collective labels for simultaneous speakers.
- Rationale: Avoids confusion in overlapping dialogue.
- Conditions: Applies when multiple speakers talk at once.
- Dependencies: Labelling

---

### 7.11 Metadata-Based Identification

#### Store Speaker Metadata

- Requirement: Include speaker identification as metadata where supported.
- Rationale: Enables searchability and advanced processing.
- Conditions: Applies in structured subtitle formats.
- Dependencies: File Format

---

## 8. Colours

### 8.1 Default Colour Scheme

#### Use High-Contrast Text

- Requirement: Present subtitles using high-contrast colour combinations.
- Rationale: Ensures readability across viewing conditions.
- Conditions: Applies to all subtitles.
- Dependencies: Accessibility

#### Use Standard Foreground and Background

- Requirement: Use a light text colour on a dark background by default.
- Rationale: Maximises legibility.
- Conditions: Applies unless alternative styling is required.
- Dependencies: Visual Clarity

---

### 8.2 Avoid Background Colour Usage

#### Do Not Use Background Colours for Meaning

- Requirement: Avoid using background colours to convey information.
- Rationale: Background colours reduce clarity and consistency.
- Conditions: Applies to subtitle styling.
- Dependencies: Accessibility

---

### 8.3 Speaker Colour System

#### Use Limited Colour Palette

- Requirement: Use a predefined set of colours for speaker differentiation.
- Rationale: Prevents inconsistency and confusion.
- Conditions: Applies to all coloured subtitles.
- Dependencies: Colour System

#### Ensure Contrast with Background

- Requirement: Ensure all colours maintain sufficient contrast.
- Rationale: Supports readability for all users.
- Conditions: Applies to all colour usage.
- Dependencies: Accessibility

---

### 8.4 Maintain Colour Consistency

#### Keep Speaker Colour Stable

- Requirement: Do not change a speaker’s assigned colour.
- Rationale: Supports recognition and continuity.
- Conditions: Applies throughout the content.
- Dependencies: Speaker Tracking

#### Manage Shared Colours Carefully

- Requirement: Only share colours between speakers when they are not present together.
- Rationale: Prevents ambiguity.
- Conditions: Applies when colour resources are limited.
- Dependencies: Scene Awareness

---

### 8.5 Multiple Speakers in Default Colour

#### Use Additional Identification Methods

- Requirement: Apply structural or textual identifiers when multiple speakers share the same colour.
- Rationale: Ensures clarity when colour alone is insufficient.
- Conditions: Applies in multi-speaker scenarios.
- Dependencies: Speaker Identification

---

## 9. Typography

### 9.1 Font Selection

#### Use Readable Sans-Serif Fonts

- Requirement: Use clear, legible sans-serif fonts for subtitle authoring and presentation.
- Rationale: Sans-serif fonts improve readability on screens.
- Conditions: Applies to all subtitle text.
- Dependencies: Rendering Environment

#### Prefer Wide Fonts for Authoring

- Requirement: Use wider fonts during authoring to minimise risk of overflow during rendering.
- Rationale: Rendering systems may substitute narrower fonts, increasing available space.
- Conditions: Applies during subtitle creation.
- Dependencies: Line Length

#### Allow Platform Font Substitution

- Requirement: Accept that playback systems may substitute fonts.
- Rationale: Final rendering depends on device and platform capabilities.
- Conditions: Applies to all delivery environments.
- Dependencies: Platform Constraints

---

### 9.2 Font Size

#### Set Authoring Font Size Relative to Video Height

- Requirement: Define subtitle size as a proportion of video height.
- Rationale: Ensures consistent readability across devices.
- Conditions: Applies to all subtitle authoring.
- Dependencies: Display Scaling

#### Adjust for Aspect Ratio

- Requirement: Use smaller proportional sizes for vertical formats compared to horizontal formats.
- Rationale: Maintains consistent perceived size across orientations.
- Conditions: Applies when working with different aspect ratios.
- Dependencies: Layout

#### Prevent Oversized Text

- Requirement: Ensure subtitle text does not exceed intended display size.
- Rationale: Oversized text can obscure visual content.
- Conditions: Applies in all presentation contexts.
- Dependencies: Positioning

---

### 9.3 Presentation Scaling

#### Allow Downscaling of Text

- Requirement: Permit rendering systems to reduce subtitle size if necessary.
- Rationale: Adapts to different screen sizes and viewing distances.
- Conditions: Applies in playback environments.
- Dependencies: Device Characteristics

#### Prevent Upscaling Beyond Authored Size

- Requirement: Do not increase subtitle size beyond authored dimensions.
- Rationale: Maintains layout integrity and avoids overlap with visuals.
- Conditions: Applies in rendering systems.
- Dependencies: Layout

#### Use Device-Aware Scaling

- Requirement: Adjust subtitle size based on screen size and resolution.
- Rationale: Ensures readability across devices.
- Conditions: Applies when device characteristics are known.
- Dependencies: Rendering Logic

---

### 9.4 Line Height

#### Maintain Proportional Line Height

- Requirement: Set line height relative to font size.
- Rationale: Ensures consistent spacing and readability.
- Conditions: Applies to all subtitle text.
- Dependencies: Typography

---

### 9.5 Background Rendering

#### Match Background to Text Width

- Requirement: Ensure background areas align with each line of text.
- Rationale: Prevents unnecessary visual blocks.
- Conditions: Applies when backgrounds are used.
- Dependencies: Styling

#### Maintain Continuous Background Between Lines

- Requirement: Avoid gaps between background areas for consecutive lines.
- Rationale: Improves visual cohesion.
- Conditions: Applies in multi-line subtitles.
- Dependencies: Styling

#### Apply Consistent Padding

- Requirement: Extend background slightly beyond text boundaries.
- Rationale: Improves readability and separation from visuals.
- Conditions: Applies when backgrounds are rendered.
- Dependencies: Styling

---

### 9.6 Character Support

#### Use Supported Character Sets

- Requirement: Restrict characters to those supported by the delivery platform.
- Rationale: Prevents rendering errors.
- Conditions: Applies to all subtitle content.
- Dependencies: Platform Constraints

#### Avoid Unsupported Characters

- Requirement: Do not include characters not supported by the target system.
- Rationale: Unsupported characters may not display correctly.
- Conditions: Applies in constrained environments.
- Dependencies: Encoding

#### Extend Character Set for Compatible Platforms

- Requirement: Use additional characters only when supported by the platform.
- Rationale: Enables richer expression where possible.
- Conditions: Applies in flexible environments.
- Dependencies: Platform Capability

---

### 9.7 Character Encoding

#### Encode Special Characters Safely

- Requirement: Ensure special characters are encoded in a compatible format.
- Rationale: Prevents parsing and rendering issues.
- Conditions: Applies in structured subtitle formats.
- Dependencies: File Format

#### Avoid Ambiguous Characters

- Requirement: Use standard character forms and avoid stylistic variations.
- Rationale: Ensures consistency and compatibility.
- Conditions: Applies during text authoring.
- Dependencies: Typography

---

## 10. Positioning

### 10.1 General Placement

#### Overlay Subtitles on Video

- Requirement: Place subtitles over the video image rather than outside it.
- Rationale: Ensures visibility across all playback environments.
- Conditions: Applies to all subtitle presentation.
- Dependencies: Display Environment

#### Use Safe Display Areas

- Requirement: Keep subtitles within defined safe regions of the screen.
- Rationale: Prevents clipping and ensures visibility.
- Conditions: Applies to all placements.
- Dependencies: Layout Constraints

---

### 10.2 Avoid Obstructing Content

#### Protect Key Visual Elements

- Requirement: Position subtitles to avoid covering important visual information.
- Rationale: Maintains access to visual context.
- Conditions: Applies when important visuals are present.
- Dependencies: Visual Context

---

### 10.3 Adaptive Positioning

#### Adjust Position Dynamically

- Requirement: Move subtitles when necessary to maintain visibility and clarity.
- Rationale: Static placement may obscure content.
- Conditions: Applies in dynamic scenes.
- Dependencies: Visual Context

---

### 10.4 Maintain Readability

#### Keep Consistent Reading Zones

- Requirement: Avoid excessive movement of subtitles across the screen.
- Rationale: Frequent repositioning reduces readability.
- Conditions: Applies across subtitle sequences.
- Dependencies: User Experience

---

### 10.5 Speaker-Based Positioning

#### Align with Speaker Location When Useful

- Requirement: Position subtitles near the speaker when it aids comprehension.
- Rationale: Spatial alignment helps identify speakers.
- Conditions: Applies when speaker location is clear.
- Dependencies: Speaker Identification

---

### 10.6 Platform-Specific Constraints

#### Respect Platform Layout Limits

- Requirement: Ensure subtitle placement conforms to platform-specific boundaries.
- Rationale: Different platforms impose different layout constraints.
- Conditions: Applies in multi-platform delivery.
- Dependencies: Platform Constraints

---

## 11. Non-Speech Information

### 11.1 Represent Non-Speech Audio

#### Include Relevant Non-Speech Sounds

- Requirement: Subtitle meaningful non-speech audio such as sound effects, music, and environmental sounds.
- Rationale: Non-speech audio contributes to narrative understanding.
- Conditions: Applies when sounds are relevant to context or action.
- Dependencies: Context Awareness

#### Exclude Irrelevant Sounds

- Requirement: Do not subtitle background sounds that do not add meaning.
- Rationale: Avoids unnecessary cognitive load.
- Conditions: Applies when sounds do not affect understanding.
- Dependencies: Editorial Judgement

---

### 11.2 Label Sound Effects Clearly

#### Use Textual Labels for Sounds

- Requirement: Represent non-speech audio using concise descriptive labels.
- Rationale: Provides clarity without overloading the subtitle.
- Conditions: Applies to sound effects and ambient audio.
- Dependencies: Formatting

#### Ensure Labels Are Distinct from Dialogue

- Requirement: Format sound labels differently from spoken dialogue.
- Rationale: Prevents confusion between speech and sound descriptions.
- Conditions: Applies whenever sound labels are used.
- Dependencies: Typography

---

### 11.3 Represent Music

#### Indicate Presence of Music

- Requirement: Identify when music is present.
- Rationale: Music contributes to tone and mood.
- Conditions: Applies when music is relevant to the scene.
- Dependencies: Context Awareness

#### Describe Music When Relevant

- Requirement: Provide brief descriptors of music when necessary for understanding.
- Rationale: Enhances accessibility to emotional or narrative cues.
- Conditions: Applies when music conveys meaning.
- Dependencies: Editorial Judgement

---

### 11.4 Represent Speaker Characteristics

#### Indicate Tone and Delivery

- Requirement: Include descriptors for significant vocal characteristics such as shouting or whispering.
- Rationale: Conveys intent and emotion not visible in text.
- Conditions: Applies when tone affects meaning.
- Dependencies: Context Awareness

---

### 11.5 Handle Overlapping Audio

#### Prioritise Critical Information

- Requirement: Represent the most important audio when multiple sounds occur simultaneously.
- Rationale: Avoids overwhelming the viewer.
- Conditions: Applies in complex audio environments.
- Dependencies: Editorial Judgement

---

### 11.6 Maintain Brevity in Labels

#### Keep Descriptions Concise

- Requirement: Use short, clear descriptions for non-speech elements.
- Rationale: Maintains readability within time constraints.
- Conditions: Applies to all non-speech subtitles.
- Dependencies: Timing

---

## 12. Quality Assurance and Consistency

### 12.1 Ensure Internal Consistency

#### Apply Rules Uniformly

- Requirement: Use consistent rules and formatting across all subtitles.
- Rationale: Predictability improves usability.
- Conditions: Applies to entire subtitle set.
- Dependencies: All Sections

---

### 12.2 Validate Readability

#### Confirm Readability Across Conditions

- Requirement: Test subtitles for readability under realistic viewing conditions.
- Rationale: Ensures usability across devices and contexts.
- Conditions: Applies before final delivery.
- Dependencies: Typography, Timing

---

### 12.3 Validate Synchronisation

#### Check Timing Accuracy

- Requirement: Verify that subtitles align with speech and visuals.
- Rationale: Prevents comprehension issues.
- Conditions: Applies during quality control.
- Dependencies: Timing, Synchronisation

---

### 12.4 Validate Completeness

#### Ensure Full Coverage

- Requirement: Confirm all relevant speech and sounds are included.
- Rationale: Guarantees accessibility.
- Conditions: Applies before finalisation.
- Dependencies: Editing, Non-Speech Information

---

### 12.5 Detect and Resolve Conflicts

#### Identify Rule Conflicts

- Requirement: Detect conflicts between timing, readability, and formatting constraints.
- Rationale: Subtitle authoring involves trade-offs.
- Conditions: Applies during editing and QA.
- Dependencies: All Sections

#### Resolve Conflicts by Priority

- Requirement: Prioritise comprehension and timing over formatting when conflicts occur.
- Rationale: Ensures usability is not compromised.
- Conditions: Applies when constraints cannot all be satisfied.
- Dependencies: Editing, Timing

---

### 12.6 Maintain Consistent Speaker Representation

#### Verify Speaker Identification Consistency

- Requirement: Ensure speakers are identified consistently throughout.
- Rationale: Prevents confusion.
- Conditions: Applies across entire content.
- Dependencies: Speaker Identification

---

### 12.7 Ensure Platform Compliance

#### Validate Against Delivery Requirements

- Requirement: Confirm subtitles meet platform-specific technical constraints.
- Rationale: Ensures compatibility and correct rendering.
- Conditions: Applies before distribution.
- Dependencies: File Format, Positioning

---

### 12.8 Perform Iterative Review

#### Review and Refine Subtitles

- Requirement: Iterate on subtitle quality through multiple review passes.
- Rationale: Improves accuracy and clarity.
- Conditions: Applies in production workflows.
- Dependencies: QA Process

---

### 12.9 Maintain Deterministic Output

#### Ensure Reproducibility

- Requirement: Produce consistent subtitle outputs from identical inputs.
- Rationale: Supports automation and validation systems.
- Conditions: Applies in structured workflows.
- Dependencies: Governance

---

### 12.10 Support Continuous Improvement

#### Incorporate Feedback

- Requirement: Update practices based on feedback and observed issues.
- Rationale: Improves long-term quality.
- Conditions: Applies in ongoing operations.
- Dependencies: Governance

---

### 12.11 Enforce Accessibility Outcomes

#### Validate Accessibility Effectiveness

- Requirement: Confirm subtitles meet accessibility needs for diverse users.
- Rationale: Accessibility is the primary goal.
- Conditions: Applies in all evaluations.
- Dependencies: All Sections
