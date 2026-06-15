# HSP_BFH_PROF_TXS

> Table contains Professional Billing payments that have been matched to a billing activity history record. Professional Billing self-pay payments are matched to billing activity history records only in service areas with Single Billing Office enabled.

**Primary key:** `BFH_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the billing activity history record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PB_MATCHED_DATE` | DATETIME |  | Date the Professional Billing payment was credited to the performed activity. |
| 4 | `PB_TX_ID` | NUMERIC | FK→ | This column stores the unique identifier for the Professional Billing transaction that this follow-up activity helped to generate. |
| 5 | `PB_MATCHED_AMOUNT` | NUMERIC |  | Self-pay amount from the Professional Billing transaction that this follow-up activity was credited with generating. Professional Billing self-pay payments are matched to billing activity records only in service areas with Single Billing Office enabled. |
| 6 | `PB_TX_MATCH_HX_LINE` | INTEGER |  | Match line in the Professional Billing transaction matching history that is credited to this activity. |
| 7 | `PB_MATCHED_INSURANCE_AMOUNT` | NUMERIC |  | This column stores the insurance amount from the professional billing transactions that are credited to this activity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |
| `PB_TX_ID` | [PB_DTL_TX](PB_DTL_TX.md) | sole_pk | high |

