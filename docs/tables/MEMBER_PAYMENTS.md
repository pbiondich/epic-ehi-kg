# MEMBER_PAYMENTS

> This table contains information about payments by the member

**Primary key:** `BENEFIT_USAGE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BENEFIT_USAGE_ID` | VARCHAR | PK FK→ | The unique ID of the benefit usage record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The date when a benefit usage was recorded. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `PAYMENT_C` | VARCHAR | org | The payment type. |
| 5 | `RECEIPT_NUM` | VARCHAR |  | The receipt number for the payment. |
| 6 | `AMOUNT_PAID` | NUMERIC |  | The amount paid in the transaction. |
| 7 | `PAYMENT_NAME` | VARCHAR |  | The name appearing on check/credit card. |
| 8 | `CHECK_NUMBER` | VARCHAR |  | The check number. |
| 9 | `CHECK_DATE` | DATETIME |  | The check date. |
| 10 | `CC_NUMBER` | INTEGER |  | The credit card number. |
| 11 | `CC_EXPIRE` | VARCHAR |  | The expiration date for credit card. |
| 12 | `CC_TYPE_C` | VARCHAR | org | The credit card type. |
| 13 | `OTHER_PAYMENT_C` | VARCHAR | org | The other mode of payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BENEFIT_USAGE_ID` | [MEMBER_INFO](MEMBER_INFO.md) | sole_pk | high |

