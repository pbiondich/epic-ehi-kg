# MYC_LETTER_RELEASE

> Information about when letters get released to MyChart.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USER_ID` | VARCHAR | FK→ | The user which released this letter to MyChart |
| 4 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `LETTER_REL_ACTION_C_NAME` | VARCHAR |  | The action taken regarding releasing this letter to MyChart |
| 6 | `LETTER_RELEASE_DTTM` | DATETIME (Local) |  | The instant at which this action related to releasing this letter to MyChart was taken. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

