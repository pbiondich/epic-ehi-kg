# LNO_LAB_RESULTS

> This table contains lab result, test, order, and specimen information associated with result reports.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the LNO record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESULT_ID` | VARCHAR | shared | The unique identifier of the result on the report. |
| 4 | `TEST_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 5 | `ORDER_ID` | NUMERIC | shared | The unique ID of the order records that are associated with the report. |
| 6 | `SPECIMEN_ID` | VARCHAR | shared | These are the specimens on the report. |
| 7 | `SUSC_PREF_LINE` | INTEGER |  | Stores the line in related group LNO 51266 that holds which susceptibility tests in the order were reported to the submitter recipient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

