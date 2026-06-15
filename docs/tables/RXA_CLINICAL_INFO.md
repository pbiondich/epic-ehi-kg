# RXA_CLINICAL_INFO

> This table holds data relating to clinical information used in prescription adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MEASUREMENT_DATE` | DATETIME |  | The date that clinical information was collected or measured. (494-ZE) |
| 6 | `MEASUREMENT_UNIT_C_NAME` | VARCHAR |  | NCPDP code indicating the metric or English units used with the clinical information. (497-H3) |
| 7 | `MEASUREMENT_VALUE` | VARCHAR |  | The actual value of clinical information. (499-H4) |
| 8 | `MEASUREMENT_TIME` | DATETIME (Attached) |  | The time that clinical information was collected or measured. (495-H1) |
| 9 | `MEASUREMENT_DIM_C_NAME` | VARCHAR |  | NCPDP code indicating the clinical domain of the observed value in Measurement Value. (496-H2) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

