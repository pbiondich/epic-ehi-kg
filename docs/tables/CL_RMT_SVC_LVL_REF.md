# CL_RMT_SVC_LVL_REF

> This table contains information relating to the Administrative Reference Number (REF) segment on the service line level.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with related remit claim references. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each instance of claim remit information will have its own line. |
| 3 | `REF_SVC_LN` | VARCHAR |  | This is the service line for reference segment. |
| 4 | `SVC_REF_ID_QUAL_C_NAME` | VARCHAR | org | This is the service line level reference segment ID qualifier. |
| 5 | `SVC_REF_IDENTIFIER` | VARCHAR |  | This is the service line level reference segment Identifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

