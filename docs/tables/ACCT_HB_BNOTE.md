# ACCT_HB_BNOTE

> This table contains Hospital Billing billing notes for guarantor accounts.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of the guarantor record for this row. This column is frequently used to link to the ACCOUNT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HB_BILLING_NOTE` | VARCHAR |  | This column contains one line of the Hospital Billing billing note of the guarantor account for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

