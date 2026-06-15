# OR_LNLG_TOURN_TMS

> This table contains the Tourniquet Times information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `TOURN_INFLATION_TI` | DATETIME (Attached) |  | The inflation time of the tourniquet. |
| 4 | `TOURN_DEFLAT_TIME` | DATETIME (Attached) |  | The deflation time of the tourniquet. |
| 5 | `TOURN_TOTAL_TIME` | INTEGER |  | The total time of the tourniquet. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

