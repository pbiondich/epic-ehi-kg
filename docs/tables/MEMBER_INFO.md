# MEMBER_INFO

> This table contains information about members

**Primary key:** `BENEFIT_USAGE_ID`  
**Columns:** 3  
**Joined by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BENEFIT_USAGE_ID` | VARCHAR | PK | The unique ID of the benefit usage record. |
| 2 | `BENEFIT_USAGE_NAME` | VARCHAR |  | The name of the member benefit usage record. |
| 3 | `MEMBERSHIP_TYPE_ID_MEMBERSHIP_NAME` | VARCHAR |  | The name for membership/benefit record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (6)

| From | Column | Confidence |
|------|--------|------------|
| [MEMBER_CRM_LINKS](MEMBER_CRM_LINKS.md) | `BENEFIT_USAGE_ID` | high |
| [MEMBER_ENCTR_LINKS](MEMBER_ENCTR_LINKS.md) | `BENEFIT_USAGE_ID` | high |
| [MEMBER_PAT_LINKS](MEMBER_PAT_LINKS.md) | `BENEFIT_USAGE_ID` | high |
| [MEMBER_PAYMENTS](MEMBER_PAYMENTS.md) | `BENEFIT_USAGE_ID` | high |
| [MEMBER_USAGE_HIST](MEMBER_USAGE_HIST.md) | `BENEFIT_USAGE_ID` | high |
| [PATIENT_MEB_NETWRK](PATIENT_MEB_NETWRK.md) | `BENEFIT_USAGE_ID` | high |

