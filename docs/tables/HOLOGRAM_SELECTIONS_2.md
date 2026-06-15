# HOLOGRAM_SELECTIONS_2

> This table stores details about each selection made in a hologram record. Which specific details are stored depends on the type of each row. Extends HOLOGRAM_SELECTIONS.

**Overflow of:** [HOLOGRAM_SELECTIONS](HOLOGRAM_SELECTIONS.md)  
**Primary key:** `HOLOGRAM_ID`, `CONTACT_DATE_REAL`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HOLOGRAM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hologram record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. For Hologram, the contact date is irrelevant. For the workflow timestamp, use the WORKFLOW_INST_UTC_DTTM column in the HOLOGRAM_DETAILS table. |
| 3 | `HOL_IS_SELECTED_YN` | VARCHAR |  | Stores whether or not an option is selected. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HOLOGRAM_ID` | [HOLOGRAM_DETAILS](HOLOGRAM_DETAILS.md) | sole_pk | high |

