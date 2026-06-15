# ORDER_APPT_INFO

> This table stores appointment-level exam information.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this procedure order. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APPT_STUDY_STATUS_C_NAME` | VARCHAR |  | The imaging study status category ID for an order linked to an appointment (Ordered, No Show, Scheduled, etc). |
| 4 | `APPT_EXAM_BGN_DATE` | DATETIME |  | The beginning date for an appointment exam. |
| 5 | `APPT_EXAM_BGN_TIME` | DATETIME (Local) |  | The beginning time for an appointment exam. |
| 6 | `APPT_EXAM_END_DATE` | DATETIME |  | The exam end date for multiple appointments scheduled with a single order (such as in nuclear medicine, where a single order would be associated with two exams, for an image and a delayed image). |
| 7 | `APPT_EXAM_END_TIME` | DATETIME (Local) |  | The exam end time for multiple appointments scheduled with a single order (such as in nuclear medicine, where a single order would be associated with two exams, for an image and a delayed image). |
| 8 | `APPT_TECH_ID` | VARCHAR |  | The unique identifier for the lead technologist for multiple appointments scheduled with a single order (such as in nuclear medicine, where a single order would be associated with two exams, for an image and a delayed image). |
| 9 | `APPT_TECH_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

