# QRY_ADDL_RESPONSE

> This table extracts the response status (examples: whether the query was read, reply type, and timestamp) of the secondary recipients of the query.

**Primary key:** `QUERY_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUERY_ID` | NUMERIC | FK→ | The unique identifier for the query record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `ADDL_RESP_USER_ID` | VARCHAR |  | Stores the non-primary responding users of the query. |
| 5 | `ADDL_RESP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ADDL_RESPONSE_C_NAME` | VARCHAR |  | Stores the non-most recent responses of the query. |
| 7 | `ADDL_RESP_UTC_DTTM` | DATETIME (UTC) |  | Stores the non-most recent response instant of the query in UTC. |
| 8 | `QUERY_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |
| 9 | `ADDL_RESP_USR_WRKFLW_C_NAME` | VARCHAR |  | This item describes what workflows additional users responded to QRYs in. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QUERY_CSN_ID` | [QRY_CONTACT_INFO](QRY_CONTACT_INFO.md) | sole_pk | high |
| `QUERY_ID` | [QRY_RECORD_INFO](QRY_RECORD_INFO.md) | sole_pk | high |

