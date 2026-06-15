# RXW_OVERTIME_SINGLE

> This table tracks overtime single items for RXW records. These records at a basic level represent sets of fills that are processed together in a part of the outpatient pharmacy workflow. For example this record type is used for work requests, shipping containers and dispense transactions.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `RX_SUBTOTAL` | NUMERIC |  | This item contains the subtotal amount due for all prescription items in this dispense transaction. |
| 4 | `OTHER_SUBTOTAL` | NUMERIC |  | This item contains the subtotal amount due for all non-prescription items in this dispense transaction. |
| 5 | `TAX_AMOUNT` | NUMERIC |  | This item contains the amount of sales tax for items in this dispense transaction. |
| 6 | `TOTAL_AMOUNT_PAID` | NUMERIC |  | This item contains the total amount paid by the patient for this dispense transaction. This excludes any due amount that was written off or deferred to patients account for payment at a later point in time. |
| 7 | `PMT_INST_DTTM` | DATETIME (UTC) |  | This item contains the instant this payment contact was completed and posted to the dispense transaction record. |
| 8 | `CHANGE_GIVEN` | NUMERIC |  | This item contains the amount of change that was given back to a patient in cash for the dispense transaction. |
| 9 | `BILLING_USER_ID` | VARCHAR |  | This item contains the user who owns the contact for billing. |
| 10 | `BILLING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `CASH_TENDERED` | NUMERIC |  | This item contains the amount of cash tendered by the patient for a dispense transaction payment encounter. |
| 12 | `HEALTH_EXPENSE_TOTAL` | NUMERIC |  | This column contains the health expense total for an ambulatory pharmacy POS sale. Health expenses include prescriptions and merchandise which are qualified healthcare expenses. This value includes tax and shipping. |
| 13 | `HEALTH_EXPENSE_SUBTOTAL` | NUMERIC |  | This column contains the health expense subtotal for an ambulatory pharmacy POS sale. Health expenses include prescriptions and merchandise which are qualified healthcare expenses. This value does not include tax or shipping. |
| 14 | `RX_MERCH_PAT_ID` | VARCHAR | FK→ | If Professional Billing integration is enabled, this contains the patient that was selected to own the charges for merchandise products. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RX_MERCH_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

