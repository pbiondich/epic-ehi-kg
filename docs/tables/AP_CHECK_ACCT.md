# AP_CHECK_ACCT

> The AP_CHECK_ACCT table contains summary information for your checking accounts used when paying claims or capitation and also information regarding the checks printed and the printer used for printing these checks.

**Primary key:** `ACCT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of each checking account record. |
| 2 | `ACCT_ID_ACCT_NAME` | VARCHAR |  | The name of each checking account. |
| 3 | `ACCT_NAME` | VARCHAR |  | The name of each checking account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

