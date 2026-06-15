# RIS_ORDER_SELFRFR_RPT

> This table contains information about result reports for a self-referred order.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RIS_RSLT_RPT_NOTE_ID` | VARCHAR |  | The result report created by the self-referred result report batch job. |
| 6 | `RIS_RSLT_RPT_PRNT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that a self-referred result report was printed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

