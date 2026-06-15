# CVG_MEM_STAT_OUTST_ACT_HX

> The historical values of the CVG_MEMBER_STAT_OUTST_ACT table over time.

**Primary key:** `COVERAGE_ID`, `LINE`, `CVG_ITM_HX_REL_ACT_GUID`  
**Columns:** 17  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CVD_STAT_OUTST_ACTION_C_NAME` | VARCHAR | org | The covered status outstanding action category ID for this member on the coverage record. |
| 5 | `CVD_STAT_OUTST_ACT_RES_C_NAME` | VARCHAR | org | The covered status outstanding action resolution category ID for this member on the coverage record. |
| 6 | `APN_QUAL_EVNT_C_NAME` | VARCHAR | org | The covered status outstanding action qualifying event category ID for this member on the coverage record. |
| 7 | `QUALIFYING_EVENT_DATE` | DATETIME |  | The qualifying event date for this outstanding action for the member on the coverage record. |
| 8 | `CVD_STATUS_OUTST_ACT_LOC_DTTM` | DATETIME (Local) |  | The instant the action was added to the coverage in the local time zone. |
| 9 | `CVD_STATUS_OUTST_ACTION_DTTM` | DATETIME (UTC) |  | The date and time when the action was added to the coverage in UTC time. |
| 10 | `CVD_STAT_OUT_ACT_RES_LOC_DTTM` | DATETIME (Local) |  | The instant the resolution was last changed in the local time zone. |
| 11 | `CVD_STATUS_OUTST_ACT_RES_DTTM` | DATETIME (UTC) |  | The instant the resolution was last changed in UTC. |
| 12 | `CVD_STAT_OUT_ACT_DENIAL_RSN_C_NAME` | VARCHAR | org | The covered status outstanding action denial reason on the coverage. |
| 13 | `ITM_HX_START_LOCAL_DTTM` | DATETIME (Local) |  | The start instant of when the coverage/line combination is valid in local time. |
| 14 | `ITM_HX_START_UTC_DTTM` | DATETIME (UTC) |  | The start instant of when the coverage/line combination is valid in UTC. |
| 15 | `ITM_HX_END_LOCAL_DTTM` | DATETIME (Local) |  | The end instant of when the coverage/line combination is valid in local time. |
| 16 | `ITM_HX_END_UTC_DTTM` | DATETIME (UTC) |  | The end instant of when the coverage/line combination is valid in UTC. |
| 17 | `CVG_ITM_HX_REL_ACT_GUID` | VARCHAR | PK | This ID links this audit batch to one or more actions in the coverage action history table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

