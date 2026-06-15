# TXPORT_DATA_AUDIT

> Contains audit data from the transport request.

**Primary key:** `TRANSPORT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSPORT_ID` | NUMERIC | PK FK→ | The unique identifier for the request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_USER_ID` | VARCHAR |  | This item stores the user that changed data for this request. |
| 4 | `AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `AUDIT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant that data was changed for this request. |
| 6 | `AUDIT_REQ_DATE` | DATETIME |  | This item stores the new date information. |
| 7 | `AUDIT_REQ_TM` | DATETIME (Local) |  | This item stores the new time information. |
| 8 | `AUDIT_USR_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSPORT_ID` | [TXPORT_REQ_INFO](TXPORT_REQ_INFO.md) | sole_pk | high |

