# RSH_RECRUIT_PREF_HX

> This table contains the history of patient research recruitment preferences.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RSH_PREF_HX_C_NAME` | VARCHAR |  | Contains the history of the patient's explicit research recruitment preference. |
| 4 | `RSH_PREF_HX_UTC_DTTM` | DATETIME (UTC) |  | Contains the history of the instants that the patient has indicated an explicit research recruitment preference. |
| 5 | `RSH_PREF_HX_EMP_ID` | VARCHAR |  | Contains the history of the users who have recorded the patient's explicit research recruitment preference. |
| 6 | `RSH_PREF_HX_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `RSH_PREF_HX_MYPT_ID` | VARCHAR |  | Contains the history of the MyChart users who have recorded the patient's explicit research recruitment preference. |
| 8 | `RSH_PREF_HX_LOCAL_DTTM` | DATETIME (Local) |  | Contains the history of the instants that the patient has indicated an explicit research recruitment preference in local time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

