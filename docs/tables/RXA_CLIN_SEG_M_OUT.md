# RXA_CLIN_SEG_M_OUT

> Stores information about clinical measurements recorded in the pharmacy for purposes of prescription claims adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `O_MEASURE_DATE` | DATETIME |  | The date that clinical information was collected or measured. |
| 6 | `O_MEASURE_TIME` | DATETIME (UTC) |  | The time that clinical information was collected or measured. |
| 7 | `O_MEASURE_DIMNS_ID` | NUMERIC |  | Code indicating the clinical domain of the observed value in 'Measurement Value' (499-H4). |
| 8 | `O_MEASURE_DIMNS_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 9 | `O_MEASURE_UNIT_ID` | NUMERIC |  | Code indicating the metric or English units used with the clinical information. |
| 10 | `O_MEASURE_UNIT_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 11 | `O_MEASURE_VALUE` | VARCHAR |  | Actual value of clinical information. |
| 12 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

