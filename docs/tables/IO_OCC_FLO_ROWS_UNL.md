# IO_OCC_FLO_ROWS_UNL

> This table displays a portion of the Flowsheet rows for the patient encounter that were intake and output (IO) occurrence rows. Do not use this table directly--instead use view IO_OCC_FLO_ROWS.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier for the inpatient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IO_OCC_FSROW_IDS` | VARCHAR |  | Flowsheet rows that can be used for IO occurrence documentation. For duplicable rows, the identifier used to distinguish among multiple rows is stored in column OCCURRENCE. |
| 4 | `IO_OCC_FSROW_IDS_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 5 | `OCCURRENCE` | INTEGER |  | If the flowsheet group/row is duplicable, this will distinguish the occurrence. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

