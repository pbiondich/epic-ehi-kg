# OR_CASE_ANES_STAF

> The OR_CASE_ANES_STAF table contains OR management system case anesthesia staff.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of line of the anesthesia staff requested for this case. |
| 3 | `ANESTH_PANEL` | VARCHAR |  | The panel where the anesthesia staff is requested. |
| 4 | `ANESTH_ROLE_C_NAME` | VARCHAR | org | The role of the anesthesia staff member within the case. |
| 5 | `AN_TEAM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

