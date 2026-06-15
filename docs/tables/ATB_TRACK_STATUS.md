# ATB_TRACK_STATUS

> This table stores Auth Bundle process tracking status information.

**Primary key:** `AUTH_BUNDLE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `TRACK_SUM_DECISION_C_NAME` | VARCHAR |  | The Summarized Decision category ID for the Auth Bundle. |
| 3 | `TRACK_AUTH_PROC_STATUS_C_NAME` | VARCHAR |  | The Process Status category ID for the Auth Bundle. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

