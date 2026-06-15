# ORDER_RPTD_SIG_PRNRSN

> For each row in ORDER_RPTD_SIG_HX where a PRN (as needed) frequency is used, this table contains the list of PRN reasons that were selected, if any.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with why a medication is marked PRN. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of PRN Reasons within this record. |
| 4 | `PRN_REASON_C_NAME` | VARCHAR | org | The frequency PRN (as needed) reason category ID indicating the reasons the medication should be given on an as-needed basis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

