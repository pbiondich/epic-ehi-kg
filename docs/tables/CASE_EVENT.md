# CASE_EVENT

> The CASE_EVENT table allows you to report on events associated with case records.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The line number of the events associated with this case record. |
| 3 | `EVENT_C_NAME` | VARCHAR | org | The category number of the event. |
| 4 | `EFF_DATE` | DATETIME |  | The effective date of the event. |
| 5 | `END_DATE` | DATETIME |  | The end date of the event. |
| 6 | `WORK_STATUS_C_NAME` | VARCHAR | org | The work status in the event. |
| 7 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 9 | `COMMENTS` | VARCHAR |  | The comments of the event. |
| 10 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user who created the event. |
| 11 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

