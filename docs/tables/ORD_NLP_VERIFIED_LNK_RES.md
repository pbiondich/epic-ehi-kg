# ORD_NLP_VERIFIED_LNK_RES

> This table contains information about links between findings and general recommendations that were present on orders when the output from a natural language processing model to extract findings and recommendations was verified or last modified.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FINDING_ID` | NUMERIC | shared | The unique ID of the finding record associated with this link. |
| 4 | `RECOMMENDATION_FINDING_ID` | NUMERIC |  | The unique ID of the recommendation finding record associated with this link. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

