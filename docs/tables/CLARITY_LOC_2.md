# CLARITY_LOC_2

> This table contains information about your location records. These include revenue locations and patients' primary clinics/locations. The records included in this table are Facility Profile (EAF) records that are designated as facility, service area, and location records. That is, Type of Location (I EAF 27) has a value of 1, 2, or 4.

**Overflow of:** [CLARITY_LOC](CLARITY_LOC.md)  
**Primary key:** `LOC_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 2 | `EXTERNAL_NAME` | VARCHAR |  | External name for the record. This name will be displayed in billing correspondences such as statements and letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [CLARITY_LOC](CLARITY_LOC.md).

