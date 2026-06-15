# CLASSIFIER

> This table stores information about classifier records which are used in the auto status assignment and notifications processes for referrals and for establishing case management record creation triggers.

**Primary key:** `CLASSIFIER_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLASSIFIER_ID` | VARCHAR | PK | The unique identifier for the classifier. |
| 2 | `CLASSIFIER_ID_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |
| 3 | `CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CASE_MGMT](CASE_MGMT.md) | `CLASSIFIER_ID` | high |

