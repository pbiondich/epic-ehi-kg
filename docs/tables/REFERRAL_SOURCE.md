# REFERRAL_SOURCE

> The REFERRAL_SOURCE table contains information about referral sources. Referral sources can be physicians who write medical referrals for patients, or they can be marketing sources by which you acquire new patients.

**Primary key:** `REFERRING_PROV_ID`  
**Columns:** 3  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRING_PROV_ID` | VARCHAR | PK | The referral ID for the referral record. |
| 2 | `REFERRING_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 3 | `REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [ACCOUNT](ACCOUNT.md) | `REFERRING_PROV_ID` | high |
| [ORDER_PROC](ORDER_PROC.md) | `REFERRING_PROV_ID` | high |
| [PRE_AR_CHG](PRE_AR_CHG.md) | `REFERRING_PROV_ID` | high |
| [PRE_AR_SESSION](PRE_AR_SESSION.md) | `REFERRING_PROV_ID` | high |
| [REFERRAL](REFERRAL.md) | `REFERRING_PROV_ID` | high |

