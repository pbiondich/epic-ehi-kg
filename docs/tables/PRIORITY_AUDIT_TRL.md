# PRIORITY_AUDIT_TRL

> Table to track changes to the priority of a transport request.

**Primary key:** `TRANSPORT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSPORT_ID` | NUMERIC | PK FK→ | The unique ID of the Transport Request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NEW_PRIORITY_C_NAME` | VARCHAR |  | The new transport request priority in the audit trail. |
| 4 | `OLD_PRIORITY_C_NAME` | VARCHAR |  | The old transport request priority in the audit trail |
| 5 | `PRIOR_CHNG_DTTM` | DATETIME (UTC) |  | The instant at which a transport request priority was changed. |
| 6 | `PRIOR_CHNG_USER_ID` | VARCHAR |  | The unique ID of the user who changed the priority of this transport request. |
| 7 | `PRIOR_CHNG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSPORT_ID` | [TXPORT_REQ_INFO](TXPORT_REQ_INFO.md) | sole_pk | high |

