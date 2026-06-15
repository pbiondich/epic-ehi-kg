# ORDER_RES_RELATED_ORDS

> Store the orders marked as related to a recommendation.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RELATED_ORDER_ID` | NUMERIC |  | This item stores orders related to this recommendation. |
| 4 | `RELATED_ORDS_STS_C_NAME` | VARCHAR | org | This item stores the review status of the related orders. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

