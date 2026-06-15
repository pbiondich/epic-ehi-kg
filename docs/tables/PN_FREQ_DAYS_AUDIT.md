# PN_FREQ_DAYS_AUDIT

> This table stores the audit history of updates to the progress note frequency in days episode override item, including the frequency, the user who set that frequency, and the instant it was set.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RHB_PN_NUM_DAYS_HX` | INTEGER |  | This audit trail item stores past values of the Rehab - Progress Note Frequency in Days [I HSB 63038]. This is updated whenever the Progress Note Frequency in Days item is changed. |
| 4 | `RHB_PN_NUM_DAYS_USER_ID` | VARCHAR |  | This audit trail item stores the user ID of the user who changed the value of the Rehab - Progress Note Frequency in Days [I HSB 63038]. This is updated whenever the Progress Note Frequency in Days item is changed. |
| 5 | `RHB_PN_NUM_DAYS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RHB_PN_DAYS_UTC_DTTM` | DATETIME (UTC) |  | This audit trail item stores the instant users changed the value of the Rehab - Progress Note Frequency in Days [I HSB 63038]. This is updated whenever the Progress Note Frequency in Days item is changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

