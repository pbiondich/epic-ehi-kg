# CELL_THERAPY_REQ_VERIFY

> This table stores the users and roles that are required to verify the cell therapy infusion plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANY_MEMBER_YN` | VARCHAR |  | This item stores if any team member can verify the cell therapy infusion plan to complete the required verification. |
| 4 | `USER_ID` | VARCHAR | FK→ | This item stores the user that is required to verify the cell therapy infusion plan. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `TREATMENT_TEAM_ROLE_C_NAME` | VARCHAR | org | This item stores the role that is required to verify the cell therapy infusion plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

