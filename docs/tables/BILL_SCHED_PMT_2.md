# BILL_SCHED_PMT_2

> This table contains information about scheduled payments. This can include payment plan agreements and payments, Visit Auto Pay payment plans and payments, and trust transfers and payments.

**Overflow of:** [BILL_SCHED_PMT](BILL_SCHED_PMT.md)  
**Primary key:** `SCHED_PMT_ID`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the scheduled payment record. |
| 2 | `PP_INITIAL_DUE_AMT` | NUMERIC |  | The amount requested to be paid on this payment plan at the start of the monthly cycle. |
| 3 | `PP_INITIAL_OVERPAID_AMT` | NUMERIC |  | The amount in which this payment plan was overpaid at the start of the monthly cycle. |
| 4 | `PP_INITIAL_OVERDUE_AMT` | NUMERIC |  | The overdue amount on this payment plan at the start of the monthly cycle. |
| 5 | `PP_REMAINING_DUE_AMT` | NUMERIC |  | The outstanding amount for this month on this payment plan. |
| 6 | `PP_PAID_AMT` | NUMERIC |  | The total amount paid towards the current month's due amount. This number includes payments, reversals, and transfers that affect the due, but will not include adjustments and other non-payment transactions. |
| 7 | `PP_OVERPAYMENT_AMT` | NUMERIC |  | The amount that is overpaid and accounting for future months. |
| 8 | `PP_OVERDUE_AMT` | NUMERIC |  | The amount that was unpaid from prior months. |
| 9 | `PP_OVERPMT_CONTRIB_MTHD_C_NAME` | VARCHAR |  | The category ID of the payment plan overpayment contribution method setting in the hospital billing profile at the time of the payment plan tracker record's creation. |
| 10 | `PP_AUTO_PAY_INCL_OVERDUE_YN` | VARCHAR |  | Indicates that the Auto Pay payment plan amount should include any overdue balances when processing. This is copied from the hospital billing profile at the time of the payment plan's most recent calculation. A 'Y' indicates that the payment plan should include overdue balances. 'N' indicates that it should not. NULL indicates that this is not an Auto Pay payment plan. |
| 11 | `PP_PB_UNDIST_PMT_AMT` | NUMERIC |  | The total amount of PB payments that have been applied to the payment plan but not yet applied to PB visit accounts on the payment plan. |
| 12 | `PAID_ON_AGREEMENT_AMT` | NUMERIC |  | Stores the total payment amount processed on this agreement. This means we will not carry over the previous payment total if a new agreement is created via a payment method update or edits to the terms. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [BILL_SCHED_PMT](BILL_SCHED_PMT.md).

