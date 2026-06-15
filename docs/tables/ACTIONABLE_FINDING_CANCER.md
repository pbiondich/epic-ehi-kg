# ACTIONABLE_FINDING_CANCER

> This table contains information about what cancer was detected after an actionable finding was documented for the order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CANCER_TYPE_C_NAME` | VARCHAR | org | The type of cancer found by the incidental finding. |
| 4 | `CANCER_TREATMENT_YN` | VARCHAR |  | Did the patient start cancer treatment after an incidental finding lead to a cancer diagnosis? |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

