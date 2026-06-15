# OR_CASE_STAFF_NEED

> The OR_CASE_STAFF_NEED table contains OR management system case surgical staff.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the surgical staff requested for the case. |
| 3 | `STAFF_REQ_YN` | VARCHAR |  | The category value which indicates whether the surgical staff member is required for the case. |
| 4 | `STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `STAFF_START_OFFSET` | INTEGER |  | The start time for the surgical staff. It is measured in minutes relative to the beginning of the case. |
| 6 | `STAFF_END_OFFSET` | INTEGER |  | The end time for the surgical staff. It is measured in minutes relative to the beginning of the case. |
| 7 | `STAFF_PANEL` | VARCHAR |  | The panel where the surgical staff is requested. |
| 8 | `STAFF_TYPE_C_NAME` | VARCHAR | org | The type of surgical staff requested for the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

