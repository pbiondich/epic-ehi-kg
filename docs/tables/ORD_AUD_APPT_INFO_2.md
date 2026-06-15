# ORD_AUD_APPT_INFO_2

> This table contains audit information about the appointment-level info for imaging studies.

**Overflow of:** [ORD_AUD_APPT_INFO](ORD_AUD_APPT_INFO.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APPT_EXAM_BEGIN_TIMES` | VARCHAR |  | Audit information about the appoitment begin times. The values are delimited by "^". The source item is located at ORDER_APPT_INFO.APPT_EXAM_BGN_TIME. |
| 4 | `APPT_EXAM_BEGIN_DATES` | VARCHAR |  | Audit information about the appoitment begin dates. The values are delimited by "^". The source item is located at ORDER_APPT_INFO.APPT_EXAM_BGN_DATE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

