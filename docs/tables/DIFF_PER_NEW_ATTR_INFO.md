# DIFF_PER_NEW_ATTR_INFO

> The new attributed provider information for the difference period.

**Primary key:** `DIFF_PERIOD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DIFF_PERIOD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the difference period record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NEW_ATTR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `ASSGN_ATTR_CHANGE_TYPE_C_NAME` | VARCHAR |  | The type of assignment and attribution change that is requested by the difference period. |
| 5 | `NEW_ATTR_PROV_NAME` | VARCHAR |  | The name of the proposed attributed provider in the event that there is no provider record. |
| 6 | `NEW_ATTR_PROV_NPI` | INTEGER |  | The proposed attributed provider NPI for the difference period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DIFF_PERIOD_ID` | [DIFFERENCE_PERIOD](DIFFERENCE_PERIOD.md) | sole_pk | high |

