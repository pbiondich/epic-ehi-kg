# EPA_CODED_REFS

> This table holds the coded references used for electronic prior authorization questions.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REF_CODE` | VARCHAR |  | This item holds the code for an electronic prior authorization coded reference. |
| 4 | `REF_CODE_QUALIFIER_ID` | NUMERIC |  | This item holds the qualifier for an electronic prior authorization coded reference. |
| 5 | `REF_CODE_QUALIFIER_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 6 | `REF_CODE_SYS_VER` | VARCHAR |  | This item holds the code system version for an electronic prior authorization coded reference. |
| 7 | `REF_CODE_DESC` | VARCHAR |  | This item holds the description for an electronic prior authorization coded reference. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

