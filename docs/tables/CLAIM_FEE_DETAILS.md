# CLAIM_FEE_DETAILS

> The CLAIM_FEE_DETAILS table contains claim fee amounts for the billing transaction.

**Primary key:** `TRANSACTION_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the detail transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESP_CLASS_ID` | NUMERIC | FK→ | Specify the responsibility class of this line. |
| 4 | `RESP_CLASS_ID_RECORD_NAME` | VARCHAR |  | The name of the responsibility class record. |
| 5 | `CLM_FEE_TYPE_C_NAME` | VARCHAR | org | Specify the fee type for this line. |
| 6 | `CLAIM_FEE_AMOUNT` | NUMERIC |  | Specify the amount of the fee type within the responsibility class. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RESP_CLASS_ID` | [NRC_RESP_CLASS](NRC_RESP_CLASS.md) | sole_pk | high |
| `TRANSACTION_ID` | [CAP_DTL_TX](CAP_DTL_TX.md) | sole_pk | high |

