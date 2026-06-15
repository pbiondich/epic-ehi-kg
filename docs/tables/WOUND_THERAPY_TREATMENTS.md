# WOUND_THERAPY_TREATMENTS

> This table stores data about wound therapy treatments that have been applied to a wound.

**Primary key:** `IP_LDA_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IP_LDA_ID` | VARCHAR | PK shared | The unique identifier for the wound being treated. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `THERAPY_IP_LDA_ID` | VARCHAR |  | The wound therapy that treated this wound. |
| 4 | `TREATMENT_START_UTC_DTTM` | DATETIME (UTC) |  | The instant treatment started |
| 5 | `TREATMENT_END_UTC_DTTM` | DATETIME (UTC) |  | The instant treatment ended |
| 6 | `USER_ID` | VARCHAR | FK→ | The user who entered this data |
| 7 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `ENTRY_UTC_DTTM` | DATETIME (UTC) |  | The instant the user entered this data |
| 9 | `EDITED_LINE` | INTEGER |  | The line number for the previously documented value in the audit trail, if this line has been edited. Corresponds to LINE in WOUND_THERAPY_TREAT_AUDIT. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

