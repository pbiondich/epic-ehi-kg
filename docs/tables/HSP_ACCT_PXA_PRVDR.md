# HSP_ACCT_PXA_PRVDR

> This table extracts the related multiple response ICD PX - ALT - Other Provider (I HAR 3130) item.

**Primary key:** `ACCT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the promotion record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The Account ID of the transfer to self-pay action or next responsible party to self-pay action performed in insurance payment posting. |
| 3 | `VALUE_LINE` | INTEGER | PK | Invoice ID that is associated with one payment Explanation of Benefits master file line. Use this field along with INV_LINE to link to the proper record in the INV_CLM_LN_ADDL table. |
| 4 | `IPXA_OTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

