# RES_SR_FINDINGS

> The RES_SR_FINDINGS table contains information about Structured Reporting as defined in the associated RES records. The information includes SR Finding Display Name, SR Finding Flag, SR Finding Macro, and SR Finding Required. This table stores I RES 56510, 56511, 56512, and 56513 which are all related numbers.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SR_DISPLAY_NAME` | VARCHAR |  | Stores a name for the RES record to use for display purposes in the Report Writer. |
| 4 | `SR_FLAG_VALUE_C_NAME` | VARCHAR | org | Stores a flag value for the finding. |
| 5 | `SR_REQUIRED_YN` | VARCHAR |  | Stores the required value for a finding and is used to determine if the finding is required as part of a report or not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

