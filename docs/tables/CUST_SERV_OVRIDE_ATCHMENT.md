# CUST_SERV_OVRIDE_ATCHMENT

> Extracts the overridden attachment types for this NCS (customer service) record.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVERRIDE_USER_ID` | VARCHAR |  | Stores user who overrode the required attachment. |
| 4 | `OVERRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `OVERRIDE_ATTACH_UTC_DTTM` | DATETIME (UTC) |  | Stores instant that the required attachment type was overridden. |
| 6 | `OVERRIDE_REC_TYPE_C_NAME` | VARCHAR |  | Stores the type of record that was overridden. |
| 7 | `OVERRIDE_REASON_C_NAME` | VARCHAR | org | Stores the reason for why the attachment was overridden. |
| 8 | `OVERRIDE_REASON_CMT` | VARCHAR |  | Stores the comment on the reason why the user overrode the required attachment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

