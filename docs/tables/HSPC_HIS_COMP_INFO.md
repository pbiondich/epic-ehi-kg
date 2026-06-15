# HSPC_HIS_COMP_INFO

> This table stores information about which users contributed to filling out the Hospice Item set. This correlates to item Z0400 on the hospice item set.

**Primary key:** `DATASET_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DATASET_ID` | NUMERIC | PK shared | The unique identifier for the data set record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMPLETING_USER_ID` | VARCHAR |  | This item tracks which users contributed to filling out the Hospice Item Set. This correlates directly to item Z0400 on the HIS. |
| 4 | `COMPLETING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `SECT_COMPLETED_DATE` | DATETIME |  | This item tracks the date that a given user contributed to filling out the Hospice Item Set. This correlates directly to item Z0400 on the HIS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

