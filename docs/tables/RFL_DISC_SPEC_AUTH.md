# RFL_DISC_SPEC_AUTH

> RFL_DISC_SPEC_AUTH contains discipline-specific authorization information used by Home Health.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VISIT_DISCIPLINE_C_NAME` | VARCHAR | org | A Home Health discipline category number specified on the referral. |
| 4 | `DISC_SPEC_REQ_VIS` | INTEGER |  | Contains the number of requested visits for the specified discipline. |
| 5 | `DISC_SPEC_AUTH_VIS` | INTEGER |  | Contains the number of authorized visits for the specified discipline. |
| 6 | `EFFECTIVE_DATE` | DATETIME |  | The Effective date for this line of the auth cert info |
| 7 | `END_DATE` | DATETIME |  | The End Date for this line of auth cert info |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

