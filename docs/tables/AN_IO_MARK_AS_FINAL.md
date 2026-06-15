# AN_IO_MARK_AS_FINAL

> This table contains Anesthesia's post-op input/output (I/O) navigator mark as final data.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the Episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AN_IO_FIN_UTC_DTTM` | DATETIME (UTC) |  | Instant of the Anesthesia I/O (Intake / Output) navigator section being marked as final. |
| 4 | `AN_IO_FIN_USER_ID` | VARCHAR |  | User that marked the Anesthesia I/O (Intake / Output) navigator section as final. |
| 5 | `AN_IO_FIN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `AN_IO_FIN_INTAKE` | NUMERIC |  | Intake total at the point of marking Anesthesia I/O (Intake / Output) section as final. |
| 7 | `AN_IO_FIN_OUTPUT` | NUMERIC |  | Output total at the point of marking Anesthesia I/O (Intake / Output) navigator section as final. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

