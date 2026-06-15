# COVERAGE_STATUS_HX

> The historical values of the COVERAGE_STATUS table over time.

**Primary key:** `COVERAGE_ID`, `LINE`, `CVG_ITM_HX_REL_ACT_GUID`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this record. |
| 3 | `COVERAGE_STATUS_TYPE_C_NAME` | VARCHAR |  | The coverage status type category ID for the coverage record. |
| 4 | `COVERAGE_STATUS_RESOLUTION_C_NAME` | VARCHAR | org | The coverage status resolution category ID for the coverage record. This column's associated ZC table is ZC_CVD_STAT_OUTST_ACT_RES. |
| 5 | `CREATION_DTTM` | DATETIME (Local) |  | The local date and time when the coverage gained the coverage status. |
| 6 | `CREATION_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the coverage gained the coverage status. |
| 7 | `RESOLUTION_DTTM` | DATETIME (Local) |  | The local date and time when the coverage had its resolution for this coverage status set. |
| 8 | `RESOLUTION_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the resolution had its state for this coverage status set. |
| 9 | `COVERAGE_STATE_CHANGE_REASON_C_NAME` | VARCHAR | org | The Coverage Status - Change Reason category ID for the coverage record. |
| 10 | `ITM_HX_START_LOCAL_DTTM` | DATETIME (Local) |  | The start instant of when the coverage/line combination is valid in local time. |
| 11 | `ITM_HX_START_UTC_DTTM` | DATETIME (UTC) |  | The start instant of when the coverage/line combination is valid in UTC. |
| 12 | `ITM_HX_END_LOCAL_DTTM` | DATETIME (Local) |  | The end instant of when the coverage/line combination is valid in local time. |
| 13 | `ITM_HX_END_UTC_DTTM` | DATETIME (UTC) |  | The end instant of when the coverage/line combination is valid in UTC. |
| 14 | `CVG_ITM_HX_REL_ACT_GUID` | VARCHAR | PK | This ID links this audit batch to one or more actions in the coverage action history table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

