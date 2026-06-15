# ORDER_RES_PATH

> Stores the pathology codes and malignancy types attached to a pathology result on an order.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID of the finding record corresponding to this result. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PATH_CODES_C_NAME` | VARCHAR | org | The pathology codes category ID for the pathology result record. |
| 4 | `MALIGNANCY_TYPE_C_NAME` | VARCHAR | org | The malignancy types category ID for the pathology result record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

