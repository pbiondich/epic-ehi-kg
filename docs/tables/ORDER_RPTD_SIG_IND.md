# ORDER_RPTD_SIG_IND

> For each row in ORDER_RPTD_SIG_HX, this table contains the list of indications of use that were selected, if any.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with the indications for this medication. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of indications within this record. |
| 4 | `INDICATION_ID` | NUMERIC |  | The indications of use for the medication instructions. |
| 5 | `INDICATION_ID_MEDICAL_COND_NAME` | VARCHAR |  | This contains the name of the medical condition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

