# WOUND_THERAPY_TREAT_AUDIT

> This table stores audit trail data about wound therapy treatments that have been applied to a wound.

**Primary key:** `IP_LDA_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IP_LDA_ID` | VARCHAR | PK shared | The unique identifier for the wound. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `THERAPY_IP_LDA_ID` | VARCHAR |  | The previously documented wound therapy device that treated this wound. |
| 4 | `TREATMENT_START_UTC_DTTM` | DATETIME (UTC) |  | The previously documented treatment start instant |
| 5 | `TREATMENT_END_UTC_DTTM` | DATETIME (UTC) |  | The previously documented treatment end instant |
| 6 | `USER_ID` | VARCHAR | FK→ | The user who previously documented this data |
| 7 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `ENTRY_UTC_DTTM` | DATETIME (UTC) |  | The instant this data was previously documented at |
| 9 | `EDITED_LINE` | INTEGER |  | The line number for the value documented before this line was entered, if this was not the first entry. Corresponds to the value of LINE for another row in WOUND_THERAPY_TREAT_AUDIT. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

