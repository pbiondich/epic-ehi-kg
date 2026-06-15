# OR_LNLG_ANEEQP_TMS

> This table contains the Anesthesia Equipment Times Information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANES_EQUIP_ST_TIME` | DATETIME (Attached) |  | The anesthesia equipment start time. |
| 4 | `ANES_EQUIP_END_TIM` | DATETIME (Attached) |  | The anesthesia equipment end time. |
| 5 | `AN_EQUIP_TOTAL_TIM` | INTEGER |  | The anesthesia equipment total time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

