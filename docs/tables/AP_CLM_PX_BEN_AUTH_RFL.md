# AP_CLM_PX_BEN_AUTH_RFL

> The referrals matched to the service line that meet benefits package requirements.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the AP claim procedure record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BENEFITS_AUTH_REFERRAL_ID` | NUMERIC |  | A referral matched to the service line that satisfies the benefit package authorization requirements. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

