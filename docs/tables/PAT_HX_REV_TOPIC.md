# PAT_HX_REV_TOPIC

> This table contains information about where in the application the history was reviewed for a patient. The history types (the kind of history reviewed) associated with a header (where the history was reviewed) are in PAT_HX_REV_TYPE. Additional information about when a patient's history was reviewed and by whom is found in the PAT_HX_REVIEW table.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated instance of history review in this encounter. Together with PAT_ENC_CSN_ID, this forms the foreign key to the PAT_HX_REVIEW table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple history topics that were reviewed for the associated instance of review and encounter from the PAT_HX_REVIEW table. |
| 4 | `HX_REVIEWED_HEADER` | VARCHAR |  | The header (a short title or description) and possibly, depending where in the application the history was reviewed, a unique record ID that describe where the history was reviewed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

