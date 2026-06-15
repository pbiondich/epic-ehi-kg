# PAT_PREF_LAB_HX

> This table contains the edit history for patient's preferred lab, including the lab, edit action, edit user, and instant of edit.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAB_EDIT_HX_ID` | NUMERIC |  | Patient's preferred labs' edit history. |
| 4 | `LAB_EDIT_HX_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 5 | `LAB_EDIT_ACT_HX_C_NAME` | VARCHAR |  | This column contains the category value corresponding to the edit action taken on the patient's preferred labs. |
| 6 | `LAB_EDIT_USR_HX_ID` | VARCHAR |  | This column contains the user ID corresponding to the edit action taken on the patient's preferred labs. |
| 7 | `LAB_EDIT_USR_HX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `LAB_EDIT_IN_HX_DTTM` | DATETIME (Local) |  | The instant the edit action was taken on the patient's preferred labs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

