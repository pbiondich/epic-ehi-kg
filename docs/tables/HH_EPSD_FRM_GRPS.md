# HH_EPSD_FRM_GRPS

> Holds the form groups that are attached to the patient's episode. These form groups automatically pull into new encounters that may use them, even if they are normally optional.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FRM_GRP_ID` | NUMERIC |  | This item stores the form groups that are attached to the patient's episode. These form groups automatically display in new visits during this patient's episode. These form groups display even if listed as optional in the contact type, but only if the contact type uses the form group. |
| 4 | `FRM_GRP_ID_RECORD_NAME` | VARCHAR |  | Stores the form group record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

