# HSP_ACCT_PXA_PRVCM

> This table extracts the related multiple response ICD PX - ALT - Other Provider Comment (I HAR 3132) item.

**Primary key:** `ACCT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the account record. |
| 2 | `GROUP_LINE` | INTEGER | PK | This item will store historical data of scheduled payment records associated with the guarantor's payment plans. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `IPXA_OTH_PROV_CMNT` | VARCHAR |  | The unique identifier for the account record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

