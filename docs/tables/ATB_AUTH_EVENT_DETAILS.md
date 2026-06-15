# ATB_AUTH_EVENT_DETAILS

> This table contains information about authorization request data that is only relevant to a specific event in time, rather than to the whole request.

**Primary key:** `AUTH_BUNDLE_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `AUTH_EVENT_MSG_TEXT` | VARCHAR |  | The free text description of the current auth status or change, but only as it pertains to a single event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

