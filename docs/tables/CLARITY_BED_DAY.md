# CLARITY_BED_DAY

> This table contains information about bed day type classification records, which are used in the Referrals and Case Management modules.

**Primary key:** `BED_DAY_TYPE_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BED_DAY_TYPE_ID` | NUMERIC | PK | The unique ID assigned to the bed day type record. |
| 2 | `BED_DAY_TYPE_ID_BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |
| 3 | `BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [BED_DAYS_MATCH](BED_DAYS_MATCH.md) | `BED_DAY_TYPE_ID` | high |
| [REFERRAL_BED_DAY](REFERRAL_BED_DAY.md) | `BED_DAY_TYPE_ID` | high |

