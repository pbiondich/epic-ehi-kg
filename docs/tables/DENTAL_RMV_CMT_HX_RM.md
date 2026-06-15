# DENTAL_RMV_CMT_HX_RM

> This table contains the historical information for comments on why a finding or procedure was removed from the patient's chart.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the dental finding or procedure record. Together with FINDING_ID, this forms the foreign key to the DENT_RMV_CMT_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple comments associated with the finding or procedure and the historical instant from the DENT_RMV_CMT_HX table |
| 4 | `DENTAL_RMV_CMT_HX` | VARCHAR |  | The history of the comment for why a finding or procedure was removed from a patient's Tooth Chart |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

