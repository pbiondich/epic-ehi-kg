# RES_TSTLVL_EXT_CMT

> Test level external string comments. These comments would be reported back to the chart or on a result report.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record for this row. This column is frequently used to link to the RES_COMPONENTS table or the RES_MICRO_CULTURE table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TST_EXT_COMM_STRING` | VARCHAR |  | Stores multi line string comments which will be reported to the chart. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

