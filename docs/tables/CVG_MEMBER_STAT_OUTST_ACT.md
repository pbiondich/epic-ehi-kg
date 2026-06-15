# CVG_MEMBER_STAT_OUTST_ACT

> This table stores the outstanding actions for the covered status of a member on a coverage record.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CVD_STAT_OUTST_ACTION_C_NAME` | VARCHAR | org | The covered status outstanding action category ID for this member on the coverage record. |
| 5 | `CVD_STAT_OUTST_ACT_RES_C_NAME` | VARCHAR | org | The covered status outstanding action resolution category ID for member on the coverage record. |
| 6 | `APN_QUAL_EVNT_C_NAME` | VARCHAR | org | The covered status outstanding action qualifying event category ID for the member on the coverage record. |
| 7 | `QUALIFYING_EVENT_DATE` | DATETIME |  | The qualifying event date for this outstanding action for the member on the coverage record. |
| 8 | `CVD_STAT_OUT_ACT_DENIAL_RSN_C_NAME` | VARCHAR | org | The covered status outstanding action denial reason on the coverage. This is extracted as the category title. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

