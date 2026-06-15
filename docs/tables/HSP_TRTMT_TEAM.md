# HSP_TRTMT_TEAM

> The HSP_TRTMT_TEAM table contains information on inpatient treatment teams. Each record in this table is based on PAT_ENC_CSN_ID.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number of the treatment team member for the patient. |
| 2 | `TRTMNT_TM_BEGIN_DT` | DATETIME (Local) |  | The date and time the treatment team member started for the patient. |
| 3 | `TRTMNT_TM_END_DT` | DATETIME (Local) |  | The date and time the treatment team member ended for the patient. |
| 4 | `TRTMNT_TM_ED_YN` | VARCHAR |  | Indicates whether or not this provider was on the treatment team in the ED. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 6 | `TEAM_ADD_YN` | VARCHAR |  | This stores whether the line was added by a team. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

