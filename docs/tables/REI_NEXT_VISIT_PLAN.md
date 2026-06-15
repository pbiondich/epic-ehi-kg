# REI_NEXT_VISIT_PLAN

> Table containing data for a patient's fertility next visit plan. Each row corresponds to a linked patient and plan creation date.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NEXT_PLAN_PAT_ID` | VARCHAR | FK→ | Stores the ID of the patient that this next visit plan is for. |
| 4 | `PLAN_DATE` | DATETIME |  | Stores the date of the plan creation date. |
| 5 | `RETURN_DATE` | DATETIME |  | Planned return date for the patient for this plan. |
| 6 | `PLAN_COMMENT_VALUE` | VARCHAR |  | Stores the value of the saved comment for this next visit’s plan. Comments are limited to a maximum of 4000 characters. |
| 7 | `PLAN_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | Instant in which this next visit’s plan was added or updated. |
| 8 | `PLAN_USER_ID` | VARCHAR |  | User ID of the provider that added or updated this next visit’s plan. |
| 9 | `PLAN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `LATEST_PLAN_YN` | VARCHAR |  | Indicates whether this plan in the group is the latest plan for this patient for this day. |
| 11 | `REI_PLAN_STATUS_C_NAME` | VARCHAR |  | Stores the status of this plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |
| `NEXT_PLAN_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

