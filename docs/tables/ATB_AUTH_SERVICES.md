# ATB_AUTH_SERVICES

> This table contains references to the service records relevant to the authorization request.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the Auth Bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_SVCS_LIST_AUTH_BUNDLE_ID` | NUMERIC |  | The unique ID of the Auth Bundle of Record Type (ATB 30) Service Line or Service Line Event to which the rest of the related information corresponds. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

