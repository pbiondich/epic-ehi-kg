# BILLING_NOTIF_GUARANTOR

> This table contains information about guarantor billing notifications.

**Primary key:** `OUTREACH_ID`, `CONTACT_DATE_REAL`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact while the digits after the decimal are unique and distinguish each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `OUTREACH_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the associated notification in the communication record. |
| 5 | `HB_SELF_PAY_BAL` | NUMERIC |  | This column stores the HB self-pay balance of the guarantor when the notification was sent. |
| 6 | `PB_SELF_PAY_BAL` | NUMERIC |  | This column stores the PB self-pay balance of the guarantor when the notification was sent. |
| 7 | `TOTAL_SELF_PAY_BAL` | NUMERIC |  | This column stores the total self-pay balance of the guarantor when the notification was sent. |
| 8 | `HB_FULL_SELF_PAY_BAL` | NUMERIC |  | This column stores the self-pay balance of the HB hospital accounts that were fully in self-pay, and had no insurance balance when the notification was sent. |
| 9 | `PB_FULL_SELF_PAY_BAL` | NUMERIC |  | This column stores the self-pay balance of the PB hospital accounts/charges that were fully in self-pay, and had no insurance balance when the notification was sent. |
| 10 | `TOTAL_FULL_SELF_PAY_BAL` | NUMERIC |  | This column stores the total self-pay balance of HB hospital accounts and PB hospital accounts/charges that were fully in self-pay, and had no insurance balance when the notification was sent. |
| 11 | `PP_PROPOSED_MONTHLY_AMT` | NUMERIC |  | If the guarantor meets the restrictions for setting up payment plans from MyChart, this column will store the proposed monthly amount that will be shown if they were to sign up for a payment plan. If eligible, the payment plan proposals will be included in statement, balance update, and payment reminder notification. |
| 12 | `PP_PROPOSED_NUM_PMTS` | INTEGER |  | If the guarantor meets the restrictions for setting up payment plans from MyChart, this column will store the proposed number of payments that will be shown if they were to sign up for a payment plan. If eligible, the payment plan proposals will be included in statement, balance update, and payment reminder notification. |
| 13 | `HB_NON_PMT_PLAN_BAL` | NUMERIC |  | If the guarantor is on a HB/SBO payment plan, this column stores the self-pay balance that is not on a payment plan. If the guarantor is not on a payment plan, this column will store the total self-pay balance of the notification line. |
| 14 | `ACTION_AMT` | NUMERIC |  | This column stores the amount the guarantor is able to take a payment action on at the time the notification was sent. For example, a guarantor using Two-Way via SMS to pay off their payment plan due. |
| 15 | `DISCOUNT_OFFER_AMOUNT` | NUMERIC |  | If the guarantor qualifies for a discount, this column stores the amount of the discount offer. |
| 16 | `PAY_NOW_BEFORE_DISCOUNT_AMT` | NUMERIC |  | For guarantors who qualify for a discount offer, this column stores the pay now amount prior to applying the discount. |
| 17 | `DISCOUNT_PAY_BY_DATE` | DATETIME |  | If the guarantor qualifies for a discount offer that includes a pay by date, this column stores that date. A discount offer includes a pay by date when a statement is sent with a due date (I SSD 235). If no statement has been sent, the statement was sent without a due date, or the guarantor does not qualify for a discount offer, this column will be blank. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OUTREACH_ID` | [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | sole_pk | high |

