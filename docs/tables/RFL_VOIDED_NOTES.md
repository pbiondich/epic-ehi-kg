# RFL_VOIDED_NOTES

> Voided notes attached to a referral.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral in database. |
| 2 | `LINE` | INTEGER | PK | The line number of the referral note. |
| 3 | `NOTE_ID` | VARCHAR | shared | Note ID of a voided note. |
| 4 | `NOTE_DATETIME` | DATETIME (Local) |  | Note creation date/time of a voided note. |
| 5 | `USER_ID` | VARCHAR | FK→ | User ID of user who created/modified the voided note. |
| 6 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

