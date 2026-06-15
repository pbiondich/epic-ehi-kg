# ORD_AUD_APPT_INFO_5

> This table contains audit information about the appointment-level info for imaging studies.

**Overflow of:** [ORD_AUD_APPT_INFO](ORD_AUD_APPT_INFO.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APPT_ITMS_ASNS` | VARCHAR |  | Audit column for appointments' asn for an imaging procedure. The values are delimited by "^". The source item is located at ORDER_APPT_INFO.LINKED_APPOINTMENTS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

