# DENTAL_PERIO_CMT_HX_RM

> This table contains the historical information for dental periodontal comments.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the mouth finding record. Together with FINDING_ID, this forms the foreign key to the DENTAL_PERIO_CMT_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple periodontal comments associated with the finding and historical instant from the DENTAL_PERIO_CMT_HX table |
| 4 | `DENTAL_PCMNT_HISTOR` | VARCHAR |  | Stores the revision history of the periodontal comment for a mouth record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

