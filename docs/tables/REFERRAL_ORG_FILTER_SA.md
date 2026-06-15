# REFERRAL_ORG_FILTER_SA

> This table holds a list of authorized service areas, business segments and the patient associated with each referral. This table is used with Organizational Filtering. An organization will have access to a referral if they are authorized for at least one of the referral's associated service areas/business segments or if they are authorized for the referral's associated patient.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple service areas and business segments can be associated with a referral. |
| 3 | `AUTH_SA_OR_BUS_SEG_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

