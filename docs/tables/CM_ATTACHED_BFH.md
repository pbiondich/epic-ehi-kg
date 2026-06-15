# CM_ATTACHED_BFH

> Table to contain information regarding Billing Follow-up History records attached to CRMs.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTACHED_BFH_ID` | NUMERIC |  | Lists the Billing Follow-up history items on this customer service record. |
| 4 | `BFH_ENTRY_USER_ID` | VARCHAR |  | The LPR ID of the user who completed the Billing account action. |
| 5 | `BFH_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `BFH_ENTRY_UTC_DTTM` | DATETIME (UTC) |  | Instant of the last update to the BFH record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

