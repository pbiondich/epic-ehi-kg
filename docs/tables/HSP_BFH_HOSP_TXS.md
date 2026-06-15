# HSP_BFH_HOSP_TXS

> Table contains Hospital Billing payments that have been matched to a billing activity history record.

**Primary key:** `BFH_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the billing activity history record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HB_TX_ID` | NUMERIC |  | This column stores the unique identifier for the payment transaction that this activity helped to generate. |
| 4 | `HB_MATCHED_AMOUNT` | NUMERIC |  | Hospital Billing self-pay payment amount credited to this activity. |
| 5 | `HB_MATCHED_INS_AMOUNT` | NUMERIC |  | Hospital Billing insurance payment amount credited to this activity. |
| 6 | `HB_MATCHED_DATE` | DATETIME |  | The date on which the payment was matched to the billing activity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

