# OBGYN_STAT

> Table for the converted OB/Gyn status structure.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OBGYN_STAT_C_NAME` | VARCHAR | org | This value is the OB/Gyn status for a patient which indicates if a patient is pregnant or not, as well as other menstrual statuses like hysterectomy, or having periods. |
| 4 | `APP_INST_UTC_DTTM` | DATETIME (UTC) |  | This instant stores the date the OB/GYN status applies to. It is generated when the OB/GYN status is saved. |
| 5 | `UPDATE_USR_ID` | VARCHAR |  | This stores the ID of the user who updated a patient's OB/GYN status. |
| 6 | `UPDATE_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

