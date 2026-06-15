# HSP_ACCT_PXA_PRVRO

> This table extracts the related multiple response ICD PX - ALT - Other Provider Role (I HAR 3131) item.

**Primary key:** `ACCT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the hospital account record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The unique identifier for the price estimate record. |
| 4 | `IPXA_OTH_PROV_RL_C_NAME` | VARCHAR | org | The unique identifier for the price estimate record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

