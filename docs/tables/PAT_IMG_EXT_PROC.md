# PAT_IMG_EXT_PROC

> This table contains the list of external imaging procedures performed on the patient and entered in the Comparison Studies activity. It includes the procedure (EAP) ID, facility, exam date, and comments.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `EXT_PROC_DATE` | DATETIME |  | The performed date of the external procedure that used for comparison studies. |
| 5 | `EXT_PROC_CMT` | VARCHAR |  | Comments entered for an external procedure used for comparison studies. |
| 6 | `EXT_PROC_DEL_YN` | VARCHAR |  | Indicates whether an external procedure (used for comparison studies) has been deleted. 'Y' indicates the external procedure has been deleted. |
| 7 | `EXT_PROC_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

