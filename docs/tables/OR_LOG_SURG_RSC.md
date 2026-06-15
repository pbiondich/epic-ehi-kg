# OR_LOG_SURG_RSC

> The OR_LOG_SURG_RSC table contains OR management system log surgical resources.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log the surgeons/staff/resources refers to. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the surgeon/staff/resource in the surgical log. |
| 3 | `SRG_STF_RES_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `REQUIRED_YN` | VARCHAR |  | Yes/no flag which indicates if the surgeon/staff/resource is required in the surgical log. |
| 5 | `SURG_REC_TYPE_C_NAME` | VARCHAR |  | The category value indicating the surgical record type for the surgeon/staff/resource. |
| 6 | `RESOURCE_TYPE_C` | VARCHAR |  | The category value indicating the surgical resource type for the staff/resource. |
| 7 | `BATCH_ASSIGN_YN` | VARCHAR |  | Yes/no flag which indicates if the Surgeon/Staff/Resource was batch assigned in the surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

