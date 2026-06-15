# CLARITY_LOC

> This table contains information about your location records. These include revenue locations and patients' primary clinics/locations. The records included in this table are Facility Profile (EAF) records that are designated as facility, service area, and location records. That is, Type of Location (I EAF 27) has a value of 1, 2, or 4.

**Overflow family:** [CLARITY_LOC_2](CLARITY_LOC_2.md)  
**Primary key:** `LOC_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 2 | `LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [PRE_AR_SESSION](PRE_AR_SESSION.md) | `LOC_ID` | high |

