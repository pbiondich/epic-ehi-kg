# COMM_TRACE_INFO_2

> This table contains information about communication traces.

**Overflow of:** [COMM_TRACE_INFO](COMM_TRACE_INFO.md)  
**Primary key:** `COMM_TRACE_ID`, `CONTACT_DATE_REAL`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_TRACE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `COMM_CHANNEL_C_NAME` | VARCHAR |  | Communication channel used to send this trace. |
| 4 | `RELATED_CAL_COMM_ID` | VARCHAR |  | Stores a related CAL record associated with a specific trace. |
| 5 | `COMM_AI_STATUS_C_NAME` | VARCHAR |  | Whether the content was generated using AI. |
| 6 | `SIBLING_GROUP` | VARCHAR |  | Messages sent at the same time, or messages that are fallback to other channels may all share a sibling grouper value. This is likely one RCH CSN from the group. |
| 7 | `REPLACED_BY_COMM_TRACE_CSN_ID` | NUMERIC |  | Contains a link to the CSN of the trace contact that this message was replaced by. |
| 8 | `ABOUT_MYPT_ID` | VARCHAR |  | If this trace was about a specific MyChart user, this item points to that MyChart user. Note that the MyChart user does not need to be a recipient. |
| 9 | `ABOUT_PAT_REL_ID` | NUMERIC |  | If this trace was about a specific relationship, this item points to that relationship. Note that the relationship does not need to be a recipient. |
| 10 | `THROTTLING_INIT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when the trace began being throttled. |
| 11 | `THROTTLING_INIT_LOCAL_DTTM` | DATETIME (Local) |  | The local instant when the trace began being throttled. |
| 12 | `ADAPTIVE_SRC_C_NAME` | NUMERIC |  | If the requested time to send was determined via adaptive logic, this item contains the source of the adaptive data used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

