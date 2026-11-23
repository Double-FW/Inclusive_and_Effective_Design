# Age-related inclusion data — migration notice

This file is retained at its original path so existing links continue to work. Its former age-by-disability tables have been withdrawn from current use.

## Why the legacy estimates are not reproduced

The old tables presented UK-, US-, EU- and Canada-oriented ranges across broad age bands. Those figures were not consistently linked to a specific source, population, measure and denominator at row or cell level. Some were described as interpolated estimates. The 61–80 and 80+ bands also both included age 80, so they could not be used as disjoint groups in demographic calculations. Repeating those numbers in a new repository would give unsupported estimates a false appearance of precision.

Do not use the former tables for prevalence claims, audience sizing, forecasting, persona weighting or model training. Do not infer a smooth age-related curve from the old ranges.

## Current guidance

Use the following canonical material in [Accessibility Demographics](https://github.com/Double-FW/Accessibility_Demographics):

- [Age-related demographic statistics and estimation methods](https://github.com/Double-FW/Accessibility_Demographics/blob/main/Accessibility_Demographic_Statistics_and_Estimation_Methods.md#6-hearing-sight-and-ageing) — current evidence records, source definitions, denominators, evidence status and estimation methods. Relevant references include HE03, VI07, DR02, DR04, AG01 and AG02.
- [Ageing and changing customer needs](https://github.com/Double-FW/Accessibility_Demographics/blob/main/research/ageing-and-changing-needs.md) — research questions, evidence limits and customer-relationship implications. Detailed motor and cognitive age profiles remain open work.
- [Ageing and customer retention](https://github.com/Double-FW/Accessibility_Demographics/blob/main/quick-guides/03-ageing-and-customer-retention.md) — practical design and retention guidance linked to the current evidence.

## Interpretation rules

- Preserve each statistic's source population, definition, denominator, date and evidence status.
- Do not combine measures merely because they refer to the same age group; cumulative thresholds and population compositions are not interchangeable with prevalence.
- Keep mobility distinct from dexterity, and age distinct from diagnosis or digital capability.
- Use compatible age bands and population counts for projections. State assumptions and uncertainty.
- Treat design implications as guidance to investigate with people, not as proof that every older person has the same needs.

For wider service outcomes, use the [Inclusive Digital Service Outcome Dataset](Inclusive_Digital_Service_Outcome_Dataset.md). This migration notice is routing information only and is not a source of demographic estimates.
