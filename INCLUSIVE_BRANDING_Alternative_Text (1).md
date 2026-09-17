# Alternative Text (Alt Text) – Comprehensive Guidance Document 

---

## Introduction to Alternative Text

### Instruction  
Explain what alternative text (alt text) is and why it's important.

### Context  
A content creator is building a news website and needs to understand the basics of image accessibility.

### Explanation  
Alternative text, often referred to as alt text or text descriptions, is a textual representation of the content and function of digital images or visual elements. It exists to ensure that users who cannot perceive visual content directly are still able to access the same information and meaning.

This primarily supports:
- Blind and visually impaired users who rely on screen readers, which convert digital content into speech
- Users of braille displays, which convert text into tactile braille output

Effective alternative text ensures equitable access to information. It should be treated as editorially important as any other component of content, including:
- Images  
- Graphics  
- Videos  
- Captions  
- Written text  

Alt text also provides additional benefits:
- Supports search engine optimisation (SEO) by making images indexable  
- Improves usability in low-bandwidth conditions where images fail to load  
- Contributes to legal compliance, including obligations under the Equality Act 2010 in the UK  

---

## Core Principles of Effective Alt Text

### Instruction  
Describe the key principles for writing effective alternative text.

### Explanation  
Effective alternative text should follow these principles:

- Communicate the core information and function of the image clearly  
- Be specific and descriptive while remaining concise  
- Avoid unnecessary phrases such as “image of” or “picture of” since assistive technologies already announce the element type  
- Do not duplicate information already available in surrounding content  
- Include any text present in the image if it is necessary for understanding  
- Use natural punctuation for clarity and readability  
- Maintain brevity, typically around 150 characters, though longer descriptions may be necessary depending on complexity  

---

## The Role of Context in Alt Text

### Instruction  
Explain how context affects alternative text and why there is no one-size-fits-all approach.

### Explanation  
Alt text is inherently contextual. The meaning of an image is determined not just by what it visually depicts, but by why it has been included in a specific piece of content.

This means:
- The same image may require different alt text in different contexts  
- Alt text should describe the meaning or purpose of the image, not just its appearance  

Example scenario:  
An image of a bird:
- In a countryside article: minimal detail may be sufficient  
- In an article about bird species: detailed physical description is necessary  
- If the bird is already described in the text: alt text can be shorter  

Reusing alt text without reconsidering context is inappropriate and can lead to loss of meaning.

---

## Decorative Images

### Instruction  
Explain what decorative images are and how to handle their alt text.

### Explanation  
Decorative images are purely aesthetic and do not contribute meaningful content. Examples include:
- Borders  
- Dividers  
- Background patterns  

Key rules:
- Decorative images must have empty alt text: `alt=""`  
- The alt attribute must still be present; it must not be omitted  
- Omitting alt attributes can cause screen readers to read filenames, which is unhelpful  

For stock images used to enhance layout:
- If they add experience or tone, include a brief description  
- If purely decorative, treat them as empty alt  

---

## Informative Images

### Instruction  
Provide guidelines for writing alt text for informative images.

### Explanation  
Informative images convey meaning, context, or emotion. These include:
- Photographs  
- Illustrations  
- Relevant objects or scenes  

Guidelines:
- Describe the image as if explaining it verbally to someone without access to it  
- Focus on relevant visual details  
- Keep descriptions concise but sufficient  
- Use plain language  
- Avoid jargon or unnecessary complexity  
- Indicate artistic style where relevant (e.g. illustration, sketch, watercolour)  

---

## Functional Images

### Instruction  
Explain how to write alt text for functional images like buttons and icons.

### Explanation  
Functional images serve as interactive controls.

Principle:
- Describe the action, not the appearance  

Examples:
- “Play” instead of “triangle icon”  
- “Search” instead of “magnifying glass”  
- “Download” instead of “arrow icon”  

Additional considerations:
- If text already labels the control, the image may be decorative  
- Where multiple similar controls exist, alt text must differentiate them  

---

## Complex Images

### Instruction  
Provide guidelines for writing alt text for complex images like charts and infographics.

### Explanation  
Complex images include:
- Charts  
- Graphs  
- Maps  
- Infographics  

Requirements:
- Provide a summary of trends or key insights  
- Ensure all critical information is accessible  

Approach:
- Focus on the purpose of the image  
- Describe patterns rather than every data point  
- Provide access to full data elsewhere if necessary  

Example:  
A chart description should summarise key comparisons and trends rather than listing all values.

---

## Images Containing Text

### Instruction  
Explain how to write alt text for images containing text.

### Explanation  
When images contain embedded text:
- Reproduce the text exactly in the alt description if it is essential  
- For large amounts of text, provide a separate text-based alternative  

Goal:  
Ensure parity of information between visual and non-visual users.

---

## 9. Describing People

### Instruction  
Provide guidelines for describing people in alternative text.

### Explanation  
When describing people:
- Include names if relevant and not already provided  
- Only mention ethnicity, religion, or cultural markers if editorially relevant  
- Avoid assumptions about:
  - Age  
  - Gender  
  - Disability  
  - Relationships  

Focus on:
- Observable attributes (clothing, posture, setting)  
- Visible assistive devices if present  

---

## Captions vs Alt Text

### Instruction  
Explain the difference between captions and alternative text.

### Explanation  
Captions and alt text serve different roles:

Captions:
- Provide contextual or editorial information  
- May include credits, dates, or narrative  

Alt text:
- Describes visual content only  
- Must not include editorial metadata  

They must not be duplicated, as both are read by screen readers.

---

## Maps

### Instruction  
Provide guidelines for writing alt text for maps.

### Explanation  
Maps often require more detail than alt text can accommodate.

Best practices:
- Provide a summary in alt text  
- Link to detailed directions or descriptions  

Structure detailed content with headings for navigation.

---

## Screen Reader Behaviour

### Instruction  
Explain how screen readers work with alternative text.

### Explanation  
Screen readers:
- Interpret HTML structure  
- Announce element types automatically  
- Read alt text aloud  

Implications:
- Avoid redundant phrases like “image of”  
- Keep descriptions concise to improve usability  

---

## Technical Implementation

### Instruction  
Provide technical implementation guidance for alternative text in HTML.

### Explanation  

Standard images:
- Use `alt` attribute on `<img>`  

Decorative images:
- Use `alt=""`  

SVG:
- Use `role="img"` and `aria-label`  

Complex images:
- Use `aria-describedby` for extended descriptions  

Important:
- Do not rely on CSS background images for meaningful content  

---

## Common Mistakes

### Instruction  
Explain best practices that avoid common mistakes.

### Explanation  
Avoid:
- Redundant phrasing  
- Duplicating nearby content  
- Missing alt attributes  
- Overly verbose descriptions  
- Making assumptions  
- Reusing alt text without context review  

---

## Final Checklist

### Instruction  
Provide a checklist for reviewing alt text.

### Explanation  

Before publishing:
- Does the description convey the image clearly?  
- Is it concise and relevant?  
- Is unnecessary phring removed?  
- Is context considered?  
- Are decorative images correctly handled?  

---

## Content-Type Variations

### Instruction  
Explain how alt text differs by content type.

### Explanation  

Different image types require different approaches:

- Decorative: empty alt  
- Informative: descriptive summary  
- Functional: action-based description  
- Text images: include text  
- Complex: summarise + link to details  

Context of content (news, education, marketing) influences depth and focus.

---

## Testing Alt Text

### Instruction  
Provide guidance on testing alternative text.

### Explanation  

Testing methods:
- Use screen readers (NVDA, JAWS, VoiceOver)  
- Disable images  
- Test across devices  
- Validate with real users  

Expected outcomes:
- All meaningful images have appropriate descriptions  
- Decorative images are ignored  
- Users can complete tasks without visual access  

---

## Platform-Specific Considerations

### Instruction  
Explain platform-specific considerations.

### Explanation  

iOS:
- Use `accessibilityLabel`  

Android:
- Use `contentDescription`  

Web:
- Use `alt` consistently across responsive images  

All platforms:
- Alt text contributes to accessible naming  
- Must be tested in real environments  

---

## Special Scenarios

### Instruction  
Provide guidance for edge cases.

### Explanation  

Dynamic content:
- Update alt text dynamically  

User-uploaded images:
- Prompt users for alt text  
- Provide guidance and moderation  

Images as links:
- Describe destination or action  

Multilingual:
- Match language of surrounding content  

---

## Closing Note

The overarching objective of alternative text is to ensure that all users—regardless of how they access content—receive equivalent meaning, usability, and experience, and overall the atlernative should evoke the same emotional response as the image, especially is it is a narrative image
