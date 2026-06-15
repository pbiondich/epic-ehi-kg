# ATB_SVCS_LINKING

> This table contains links to other records or concepts that are specific to the Auth Bundle record when it is a service.

**Primary key:** `AUTH_BUNDLE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `SVCS_LINKED_AUTH_ID` | NUMERIC |  | The unique ID of the Authorization (AUT) that corresponds to this Service ATB. |
| 3 | `SVCS_LNKD_UM_AUTH_ID` | NUMERIC |  | The linked UM AUT that corresponds to this Service ATB. Set and used when processing an incoming response to an internal UM submission to help with service matching. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

