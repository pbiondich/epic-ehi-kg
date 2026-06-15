# RX_IVENT_USERINFO

> User-related info for an intervention: users and their associated roles in the intervention.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | NUMERIC | PK FK→ | The unique ID for the intervention. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USER_ID` | VARCHAR | FK→ | The ID of the user associated with a role in the intervention. |
| 4 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ROLE_C_NAME` | VARCHAR | org | The role for a particular user involved in an intervention. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

