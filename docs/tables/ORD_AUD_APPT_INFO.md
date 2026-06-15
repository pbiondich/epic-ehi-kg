# ORD_AUD_APPT_INFO

> This table contains audit information about the appointment-level info for imaging studies.

**Overflow family:** [ORD_AUD_APPT_INFO_2](ORD_AUD_APPT_INFO_2.md), [ORD_AUD_APPT_INFO_3](ORD_AUD_APPT_INFO_3.md), [ORD_AUD_APPT_INFO_4](ORD_AUD_APPT_INFO_4.md), [ORD_AUD_APPT_INFO_5](ORD_AUD_APPT_INFO_5.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APPT_STUDY_STATUES` | VARCHAR |  | Audit column for appointment study statues (category values) for an imaging procedure. The values are delimited by "^". The source item is located at ORDER_APPT_INFO.APPT_STUDY_STATUS_C. |
| 4 | `APPT_STUDY_STAUES_EXT_VALS` | VARCHAR |  | Audit column for appointment study statues (external category values) for an imaging procedure. The values are delimited by "^". The source item is located at ORDER_APPT_INFO.APPT_STUDY_STATUS_C. This column shows the translated external value as of when the column was last extracted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

