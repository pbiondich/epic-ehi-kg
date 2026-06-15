# OR_CASE_SERVICE_SPEC_NEED

> Case service-specific special needs.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SERVICE_SPECIAL_NEED_SERVICE_C_NAME` | VARCHAR | org | This documents any service-specific special needs related to the service. |
| 4 | `SERVICE_SPECIAL_NEED_STATUS_C_NAME` | VARCHAR | org | Specify any service specific special needs regarding the status. |
| 5 | `SERVICE_SPECIAL_NEED_COMM` | VARCHAR |  | Specify any comments for service specific special needs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

