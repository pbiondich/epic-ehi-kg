# DENTAL_GINGIVALMARGIN_HX

> This table contains the past gingival margin values recorded for a tooth.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the tooth record. Together with FINDING_ID, this forms the foreign key to the DENTAL_TOOTH_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple gingival margin readings associated with the tooth and the historical instant from the DENTAL_TOOTH_HX table |
| 4 | `DENT_GING_MARG_HX` | INTEGER |  | This item tracks the history of gingival margin readings (in mm) on a particular tooth. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

