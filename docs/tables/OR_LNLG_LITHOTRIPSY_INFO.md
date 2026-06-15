# OR_LNLG_LITHOTRIPSY_INFO

> This table contains information about the lithotripsy procedure.

**Primary key:** `RECORD_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `TOTAL_STONES` | INTEGER |  | This item stores the total number of stones for the lithotripsy procedure. |
| 3 | `LITHO_FLUOROSCOPY_TIME` | NUMERIC |  | This item stores the total fluoroscopy time for the lithotripsy procedure. |
| 4 | `LITHO_POSITIONING_DTTM` | DATETIME (UTC) |  | This item stores the time when a patient was positioned for the lithotripsy procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

