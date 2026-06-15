# COMMUNITY_RESOURCE_SDOH

> SDOH domains this community resource is meant to address.

**Primary key:** `RECOMMENDATION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECOMMENDATION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the recommendation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `SDOH_ADDRESSED_C_NAME` | VARCHAR | org | The social drivers of health domains that this community resource recommendation is intended to address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RECOMMENDATION_ID` | [COMMUNITY_RESOURCE](COMMUNITY_RESOURCE.md) | sole_pk | high |

