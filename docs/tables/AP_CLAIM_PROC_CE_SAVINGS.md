# AP_CLAIM_PROC_CE_SAVINGS

> This table stores code edit saving information for a service.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALLOW_AMOUNT_PRIOR_CODE_EDIT` | NUMERIC |  | The allowed amount of the service prior to a code edit. |
| 4 | `ALLOW_AMOUNT_POST_CODE_EDIT` | NUMERIC |  | The allowed amount of the service after a code edit. |
| 5 | `COMPUTED_CODE_EDIT_SAVINGS` | NUMERIC |  | The system computed code edit saving on a service for a particular code editor. |
| 6 | `OVERRIDE_CODE_EDIT_SAVINGS` | NUMERIC |  | The overridden code edit saving on a service for a particular code editor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

