# COVERAGE_MEMBER_RIDERS

> This table stores member-level riders and their effective period. Members will only have riders in this table if there are riders with a selection mode of 4-Member-Specific (PLAN_GRP_RIDER.RIDER_SEL_MODE_C = 4) for the employer group on their coverage (COVERAGE.PLAN_GRP_ID) and the rider been assigned to the member.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for the rider. This column is frequently used to link to the PATIENT table. |
| 4 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 5 | `EFF_DATE` | DATETIME |  | The date when the rider becomes effective for the patient. This date should never be NULL. The period of time between this date and the term date represents a period during which the specified patient is eligible for the specified rider. This date range will not overlap any other date range for the same rider and patient. |
| 6 | `TERM_DATE` | DATETIME |  | The date after which the rider is no longer effective for the patient. If this date is NULL, the rider is assumed to always be effective from the effective date onward. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

