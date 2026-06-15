# CL_RMT_SVC_DAT_INF

> This table contains service date information for a service line in a remittance record.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. |
| 3 | `SVC_DATE_QUAL_C_NAME` | VARCHAR |  | This is the Code specifying type of service date. |
| 4 | `SERVICE_DATE` | DATETIME |  | This is the service date. |
| 5 | `SERVICE_LN` | VARCHAR |  | This is the service line for which service date is specified |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

