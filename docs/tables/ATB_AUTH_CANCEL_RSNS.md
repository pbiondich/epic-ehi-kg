# ATB_AUTH_CANCEL_RSNS

> This table contains the reasons for cancellation when the authorization decision is withdrawn or dismissed.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_PYR_CANCEL_RSN_C_NAME` | VARCHAR |  | The reasons for the canceled status received from the payer. Only relevant when the payer decision is canceled. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

