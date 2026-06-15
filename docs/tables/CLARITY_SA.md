# CLARITY_SA

> The CLARITY_SA table contains information about your service areas. The records included in this table are facility profile records that are designated as facility, service area or payor business segment. That is, Type of Location, has a value of 1, 4 or 11.

**Primary key:** `SERV_AREA_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 2 | `SERV_AREA_NAME` | VARCHAR |  | The name of the service area. |
| 3 | `EXTERNAL_NAME` | VARCHAR |  | The name of the record that appears in billing correspondences such as statements and letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

