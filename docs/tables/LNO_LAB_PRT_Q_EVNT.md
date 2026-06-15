# LNO_LAB_PRT_Q_EVNT

> This table contains lab print queue event log information for result reports.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the LNO record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PQ_SPECIMEN_ID` | VARCHAR |  | Stores the specimen record of the result from the request on the print queue. |
| 4 | `PQ_TESTLINE` | INTEGER |  | Stores the test line in the specimen of the result from the request on the print queue. |
| 5 | `PQ_ORDER_ID` | NUMERIC |  | Stores the order of the result from the request on the print queue. |
| 6 | `PQ_EVENT_ID` | VARCHAR |  | Stores the event of the result from the request on the print queue. |
| 7 | `PQ_EVENT_ID_RECORD_NAME` | VARCHAR |  | The name of the event template. |
| 8 | `PQ_RESULT_ID` | VARCHAR |  | The unique ID of the result from the request on the print queue. |
| 9 | `PQ_INSTANT` | DATETIME (Local) |  | Stores the instant the request was processed and added here. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

