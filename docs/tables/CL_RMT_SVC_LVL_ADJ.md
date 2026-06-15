# CL_RMT_SVC_LVL_ADJ

> This table contains the claim adjustment (CAS) level information for a service line of a remittance record.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. |
| 3 | `CAS_SERVICE_LINE` | VARCHAR |  | This is the service line which this adjustment information refers. |
| 4 | `SVC_CAS_GRP_CODE_C_NAME` | VARCHAR | org | This is the Code identifying the general category of payment adjustment. |
| 5 | `SVC_ADJ_REASON_CD` | VARCHAR |  | This is the Code identifying the detailed reason the adjustment was made. |
| 6 | `SVC_ADJ_AMT` | NUMERIC |  | This is the amount of the adjustment. |
| 7 | `SVC_ADJ_QTY` | NUMERIC |  | This is the units of service being adjusted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

