# RFL_REF_TO_REGIONS

> This table holds the list of geographical areas for referred to geographical steering in Referral and Order Entry. It will only be populated if the "Use Referred to Geographic Areas" Referral system definition is set to Yes.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REF_TO_AREAS_ID_AREA_NAME` | VARCHAR |  | The name of the geograpic region |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

