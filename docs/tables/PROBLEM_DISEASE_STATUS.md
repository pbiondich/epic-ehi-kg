# PROBLEM_DISEASE_STATUS

> Stores disease status information for a problem on a patient's problem list.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROBLEM_DISEASE_STATUS_C_NAME` | VARCHAR | org | Represents the disease status of a problem on the problem list. |
| 4 | `DISEASE_STATUS_START_DATE` | DATETIME |  | Represents the earliest possible date that a problem could have had its disease status effective. The latest possible date is stored in DISEASE_STATUS_END_DATE. If the start and end dates for a row are the same, then the date for that row is exact rather than fuzzy. |
| 5 | `DISEASE_STATUS_END_DATE` | DATETIME |  | Represents the last possible date that a problem could have had its disease status effective. The earliest possible date is stored in DISEASE_STATUS_START_DATE. If the start and end dates for a row are the same, then the date for that row is exact rather than fuzzy. |
| 6 | `DISEASE_STATUS_PROV_USER_ID` | VARCHAR |  | Documents the user who either entered or most recently changed disease status information for this problem. |
| 7 | `DISEASE_STATUS_PROV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `DISEASE_STATUS_MAP_VAL_C_NAME` | VARCHAR |  | Disease Status Mapping for custom statuses |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

