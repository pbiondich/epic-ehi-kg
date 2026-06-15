# ORD_NLP_TEXT_RECOM

> This table contains information about general recommendations that were extracted from radiology reports by a natural language processing model. This table captures the resolved rate of the recommendation before the recommendation was discretely added.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TEXT_REC_REGION_C_NAME` | VARCHAR |  | The region of the recommendation in the text. |
| 4 | `TEXT_REC_MODALITY_C_NAME` | VARCHAR |  | The modality of the recommendation in the text. |
| 5 | `TEXT_REC_TIMEFR_C_NAME` | VARCHAR |  | The time frame of the recommendation in the text. |
| 6 | `TEXT_REC_STATUS_C_NAME` | VARCHAR | org | The status of the recommendation in the text. |
| 7 | `REC_ORDER_ID` | NUMERIC |  | The order placed for the recommendation in the text. |
| 8 | `REC_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The appointment scheduled for the recommendation in the text. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REC_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

