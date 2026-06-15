# AUTH_REQUEST_EXT_TRN

> Event trace data from an external system and received by Payer Platform.

**Primary key:** `AUTH_REQUEST_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the authorization request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_EVT_TRACE_NUM` | VARCHAR |  | The event-level trace number from the external system. |
| 4 | `EXT_EVT_COMPANY` | VARCHAR |  | The corresponding company ID for the event-level trace number from the external system. |
| 5 | `EXT_EVT_ADDL_IDENT` | VARCHAR |  | The corresponding additional reference identifier for the event-level trace number from the external system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

