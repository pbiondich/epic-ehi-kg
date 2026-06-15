# ORD_NLP_INITIAL_RECOM

> This table contains information about general recommendations that were extracted from radiology reports by a natural language processing model.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RECOMMENDATION_FINDING_ID` | NUMERIC |  | The unique ID of the recommendation finding record associated with this recommendation information. |
| 4 | `GENERAL_RECOM_C_NAME` | VARCHAR | org | The general recommendation category ID. |
| 5 | `ANATOMY_REGION_C_NAME` | VARCHAR | org | The anatomical region category ID. |
| 6 | `MODALITY_TYPE_C_NAME` | VARCHAR | org | The modality category ID. |
| 7 | `GEN_RECOM_DUE_IN_C_NAME` | VARCHAR | org | The timeframe category ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

