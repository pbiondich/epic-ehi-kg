# DENTAL_FURC_LOC_HX

> This table contains the history of locations where furcation is present on a tooth.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the furcation finding record. Together with FINDING_ID, this forms the foreign key to the DENTAL_FINDING_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple furcation locations associated with the finding and the historical instant from the DENTAL_FINDING_HX table |
| 4 | `DENT_FURC_LOC_HX_C_NAME` | VARCHAR |  | The history of locations where furcation is present on a tooth. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

