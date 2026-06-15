# COVERAGE_MEM_RIDERS_HX

> The historical values of the COVERAGE_MEMBER_RIDERS over time.

**Primary key:** `COVERAGE_ID`, `LINE`, `CVG_ITM_HX_REL_ACT_GUID`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for the rider. This column is frequently used to link to the PATIENT table. |
| 4 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 5 | `EFF_DATE` | DATETIME |  | The date when the rider becomes effective for the patient. This date should never be NULL. The period of time between this date and the term date represents a period during which the specified patient is eligible for the specified rider. This date range will not overlap any other date range for the same rider and patient. |
| 6 | `TERM_DATE` | DATETIME (UTC) |  | The date after which the rider is no longer effective for the patient. If this date is NULL, the rider is assumed to always be effective from the effective date onward. |
| 7 | `ITM_HX_START_LOCAL_DTTM` | DATETIME (Local) |  | The start instant of when the coverage/line combination is valid in local time. |
| 8 | `ITM_HX_START_UTC_DTTM` | DATETIME (UTC) |  | The start instant of when the coverage/line combination is valid in UTC. |
| 9 | `ITM_HX_END_LOCAL_DTTM` | DATETIME (Local) |  | The end instant of when the coverage/line combination is valid in local time. |
| 10 | `ITM_HX_END_UTC_DTTM` | DATETIME (UTC) |  | The end instant of when the coverage/line combination is valid in UTC. |
| 11 | `CVG_ITM_HX_REL_ACT_GUID` | VARCHAR | PK | This ID links this audit batch to one or more actions in the coverage action history table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

