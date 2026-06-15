# V_EHI_CVG_VERIF_HX_FILTER_PAT

> EHI Filter view for audit trail of historical (i.e. old data model) coverage verification changes on a coverage record.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The ID of the coverage (CVG) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VERF_HX_PRV_STAT_C_NAME` | VARCHAR | org | When the verification status is changed, this column contains the old status. |
| 4 | `VERF_HX_NEW_STAT_C_NAME` | VARCHAR |  | When the verification status is changed, this column contains the new status. |
| 5 | `VERF_HX_USER_ID` | VARCHAR |  | When the verification status is changed, this column contains the user who caused the change. |
| 6 | `VERF_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `VERF_HX_CHANGE_DT` | DATETIME |  | When the verification status is changed, this column contains the date of the change |
| 8 | `VERF_HX_NXT_RVW_DT` | DATETIME |  | When the verification status is changed, this column contains the calculated next review date. |
| 9 | `VERF_HX_MEM_PAT_ID` | VARCHAR | FK→ | When the verification status is changed at the member level, this column contains the member's patient ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `VERF_HX_MEM_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

