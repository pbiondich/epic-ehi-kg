# DERM_SKINEXAM_FINDING

> Clarity table for dermatology skin exam finding no-add items.

**Primary key:** `FINDING_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `COPY_FINDING_SRC_FINDING_ID` | NUMERIC |  | This item contains the finding record that this finding was copied from. This is used for auditing purposes. |
| 3 | `PALETTE_FINDING_SRC_RECORD_ID` | NUMERIC |  | This item contains the palette row record that the finding was added from. This is used for auditing purposes. |
| 4 | `PALETTE_FINDING_SRC_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the Scripting Template. |
| 5 | `DERM_APPROX_LOC_YN` | VARCHAR |  | This item indicates whether a finding represents an approximate location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

