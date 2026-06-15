# CARE_SVC_LN

> This table stores information about healthcare service lines. Healthcare service lines are services or sets of related services that an organization is able to provide to a patient. They are used when coordinating post-discharge care or community resources for a patient.

**Primary key:** `SVC_LN_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SVC_LN_ID` | NUMERIC | PK | The unique identifier (.1 item) for the service line record. |
| 2 | `SVC_LN_NAME` | VARCHAR |  | The name (.2 item) of the service line record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [DP_FACILITY](DP_FACILITY.md) | `SVC_LN_ID` | high |

