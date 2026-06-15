# CLM_3PP_PRICING_HX

> This table stores the third-party pricing activities for the claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRICING_ENTITY_ID` | NUMERIC |  | This item stores third-party pricing entity. |
| 4 | `PRICING_ENTITY_ID_RUL_NAME` | VARCHAR |  | The name of the third-party pricing entity, grouper, or rule. |
| 5 | `ENTITY_GROUPER_ID` | NUMERIC |  | This item stores the third-party pricing entity grouper. |
| 6 | `ENTITY_GROUPER_ID_RUL_NAME` | VARCHAR |  | The name of the third-party pricing entity, grouper, or rule. |
| 7 | `SEND_DT` | DATETIME |  | This item stores the date the claim was sent for third-party pricing. |
| 8 | `DUE_DT` | DATETIME |  | This item stores the due date for the third-party pricing. |
| 9 | `COMPLETE_DT` | DATETIME |  | This item stores the third-party pricing complete date. |
| 10 | `CANCEL_DT` | DATETIME |  | This item stores the date the claim batch for third-party pricing was cancelled. |
| 11 | `REJECTED_YN` | VARCHAR |  | This item stores whether the third-party pricer rejected the claim. |
| 12 | `ACTION_C_NAME` | VARCHAR |  | This item stores the action that should be taken for a claim that has been rejected by the third party pricer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

