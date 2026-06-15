# EPRESCRIBE_ERROR_ACTIONS

> This table holds information about e-prescribing error resolution triggered before the May 23 version. E-prescribing error resolution on or after the upgrade to the May 23 version will be stored to ERX_EVENT table instead.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESOLVING_ACTION_C_NAME` | VARCHAR |  | This item indicates how an e-prescribing error was resolved. |
| 4 | `RESOLVING_USER_ID` | VARCHAR |  | This item indicates which user resolved an e-prescribing error. |
| 5 | `RESOLVING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RESOLVED_UTC_DTTM` | DATETIME (UTC) |  | This item indicates when an e-prescribing error was resolved. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

