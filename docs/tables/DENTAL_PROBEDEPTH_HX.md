# DENTAL_PROBEDEPTH_HX

> This table contains the historical values for periodontal documentation on a tooth.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the tooth record. Together with FINDING_ID, this forms the foreign key to the DENTAL_TOOTH_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple probing depth readings associated with the tooth and the historical instant from the DENTAL_TOOTH_HX table |
| 4 | `DENTAL_PROBEDPTH_HX` | INTEGER |  | This column tracks the history of probing depths (in mm) on a particular tooth. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

