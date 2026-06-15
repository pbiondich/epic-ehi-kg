# VERIF_STATUS_HX

> The VERIF_STATUS_HX table contains the history of your verification records. These records include verification information for patients, guarantors, coverages, coverage members, hospital accounts, and encounters.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the verification record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VERIF_STATUS_HX_C_NAME` | VARCHAR | org | The history of the verification status for this record. |
| 4 | `VERIF_DATE_HX_DTTM` | DATETIME (UTC) |  | The history of the date on which the record was verified. |
| 5 | `VERIF_USER_HX_ID` | VARCHAR |  | The history of the user who last verified the record. |
| 6 | `VERIF_USER_HX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `NEXT_REV_DATE_HX_DT` | DATETIME |  | The history of the next review date for this record. |
| 8 | `STAT_CHNG_HX_DTTM` | DATETIME (UTC) |  | The history of the status change date for this record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

