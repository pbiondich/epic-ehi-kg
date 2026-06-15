# ACCOUNT_CONTACT_2

> This table contains the information recorded in billing system account contact for each account. Each row in this table contains information about one contact and is uniquely identified by the Account ID and line number combination.

**Overflow of:** [ACCOUNT_CONTACT](ACCOUNT_CONTACT.md)  
**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID for the account record. This ID number could be encrypted if you have elected to implement enterprise reporting’s encryption security function. |
| 2 | `LINE` | INTEGER | PK | Line number to identify the account contact information within the account. |
| 3 | `FOL_UP_MYC_USER_ID` | VARCHAR |  | The ID of the MyChart user who created the contact. This ID may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 4 | `PAY_PLAN_SOURCE_C_NAME` | VARCHAR |  | The source workflow category ID that set up the payment plan for the guarantor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

