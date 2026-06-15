# BILL_SCHED_PP_ACTION_HX

> This table contains information about actions performed on a payment plan.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time that an action occurred on the payment plan. |
| 4 | `ACTION_DTTM` | DATETIME (Local) |  | The local date and time that an action occurred on the payment plan. |
| 5 | `PMT_PLAN_ACTION_TYPE_C_NAME` | VARCHAR |  | The category ID of the payment plan history action type. |
| 6 | `PB_PMT_ADJ_TX_ID` | NUMERIC |  | The unique ID of the professional billing payment or credit adjustment associated with this payment plan history action. |
| 7 | `PB_CHARGE_TX_ID` | NUMERIC |  | The unique ID of the professional billing charge associated with this payment plan history action. |
| 8 | `PB_MATCH_LINE_NUM` | INTEGER |  | The unique ID of the professional billing payment match line associated with this payment plan history action. |
| 9 | `HB_PMT_ADJ_TX_ID` | NUMERIC |  | The unique ID of the hospital billing payment or credit adjustment associated with this payment plan history action. |
| 10 | `PB_ORIG_PMT_ADJ_TX_ID` | NUMERIC |  | The unique ID of the original professional billing payment or credit adjustment associated with this payment plan history action. If the hospital or professional billing payment or credit adjustment was transferred from professional billing originally, this is the original transaction. Otherwise, this is the same as the professional billing payment or credit adjustment. |
| 11 | `HB_ORIG_PMT_ADJ_TX_ID` | NUMERIC |  | The unique ID of the original hospital billing payment or credit adjustment associated with this payment plan history action. If the hospital or professional billing payment or credit adjustment was transferred from hospital billing originally, this is the original transaction. Otherwise, this is the same as the hospital billing payment or credit adjustment. |
| 12 | `APPLIED_AMT` | NUMERIC |  | The payment/credit adjustment amount applied to the payment plan balance. A positive number reduces the balance and a negative number increases the balance. |
| 13 | `APPLIED_TO_DUE_AMT` | NUMERIC |  | The payment/credit adjustment amount applied to the payment plan due amount. A positive number reduces the due amount and a negative number increases the due amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

