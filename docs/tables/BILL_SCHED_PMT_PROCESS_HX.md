# BILL_SCHED_PMT_PROCESS_HX

> This table contains the payment processing history from the Billing Scheduled Payment (BSP) master file.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROCESS_HX_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant of the processing history. |
| 4 | `PROCESS_HX_ACTION_C_NAME` | VARCHAR |  | Stores the action of the processing history. |
| 5 | `PROCESS_HX_ACTION_DATE` | DATETIME |  | Stores the date on which the corresponding action was performed. |
| 6 | `PROCESS_HX_PMT_AMT` | NUMERIC |  | Stores the history of the amount that was scheduled or processed. |
| 7 | `PROCESS_HX_USER_ID` | VARCHAR |  | This column stores the history of the user who performed the corresponding action. |
| 8 | `PROCESS_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `PROCESS_HX_CARD_HX_LINE` | INTEGER |  | This column stores the history line from the payment method record where the transaction history is stored. |
| 10 | `PROCESS_HX_TX_IDENT` | VARCHAR |  | This column stores the transaction identifier returned by the credit card engine. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

