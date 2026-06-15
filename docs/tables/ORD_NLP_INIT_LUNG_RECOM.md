# ORD_NLP_INIT_LUNG_RECOM

> This table contains information about lung screening recommendations that were created by a natural language processing model.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RECOMMENDATION_FINDING_ID` | NUMERIC |  | The unique ID of the recommendation finding record associated with this recommendation information. |
| 4 | `SX_PROG_REC_C_NAME` | VARCHAR | org | The screening program recommendation category ID. |
| 5 | `DUE_DATE` | DATETIME |  | The due date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

