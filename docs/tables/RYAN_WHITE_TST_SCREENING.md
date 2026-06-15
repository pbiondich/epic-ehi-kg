# RYAN_WHITE_TST_SCREENING

> Holds data for Ryan White CAREWare TST Screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_TST_DATE` | DATETIME |  | Date of the TST screening. |
| 4 | `RW_TST_RESULT_C_NAME` | VARCHAR |  | The result of the TST screening. |
| 5 | `RW_TST_SCORE` | NUMERIC |  | The numerical score of the TST screening. |
| 6 | `RW_TST_ACTION_C_NAME` | VARCHAR |  | The action corresponding to the TST screening. |
| 7 | `RW_TST_COMMENTS` | VARCHAR |  | The comments for the TST screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

