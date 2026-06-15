# OB_HSB_DEL_RP_DTTM

> The OB_HSB_DEL_RP_DTTM table contains membrane rupture date and time information recorded from the OB Delivery Summary. It uses the list of rupture dates and times stored in the patient's delivery record and combines them to create a list of date/time values. If a rupture time was recorded with no corresponding date, it is considered incomplete documentation and the line is thrown out.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID assigned to the episode record (HSB .1). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OB_DEL_RUP_DTTM` | DATETIME (Local) |  | This column extracts the date and time of rupture for a delivery record. It uses the list of rupture dates and times stored in the patient's delivery record and concatenates them to create a list of correlated date/time values. If no time value was recorded, the default is midnight (use RUPT_TM_PRESENT_YN to determine if a midnight value is entered by the user or defaulted in). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

