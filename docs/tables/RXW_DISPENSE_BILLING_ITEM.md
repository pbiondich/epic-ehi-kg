# RXW_DISPENSE_BILLING_ITEM

> This table contains information about payments made for outpatient pharmacy prescription fills.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `BILL_ITEM_TYPE_C_NAME` | VARCHAR |  | This item contains the type of billing item this line contains. |
| 5 | `AMOUNT` | NUMERIC |  | This item contains the currency value amount for the billing item. |
| 6 | `BILLING_COMMENT` | VARCHAR |  | This item contains the comments for a pharmacy dispense billing item. |
| 7 | `CHECK_NUM` | VARCHAR |  | This item contains the check number for a pharmacy dispense payment of type "Check". |
| 8 | `ADJUSTMENT_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `COMP_INST_DTTM` | DATETIME (UTC) |  | This item contains the instant when the billing item was completed. |
| 10 | `NON_PAY_REASON_C` | INTEGER |  | This item contains the non-payment reason for a pharmacy dispense billing item of type of "Non-Payment". |
| 11 | `PMT_TYPE_C_NAME` | VARCHAR | org | This item contains the payment type for pharmacy dispense billing items of type "payment". |
| 12 | `ASSOCIATED_PAT_ID` | VARCHAR | FK→ | The patient associated with a billing item. Currently, this is only used for the Non-Payment payment type. The unpaid amount will only be associated with prescriptions and merchandise charges associated with that patient. This item will not be set if Professional Billing integration is not enabled for the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASSOCIATED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

