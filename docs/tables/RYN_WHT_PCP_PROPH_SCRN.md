# RYN_WHT_PCP_PROPH_SCRN

> Stores data for Ryan White CAREWare PCP Prophylaxis screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_PCP_PROPH_DATE` | DATETIME |  | The date of the PCP Prophylaxis screening. |
| 4 | `RW_PCP_PROPH_RSLT_C_NAME` | VARCHAR |  | The result of the PCP Prophylaxis screening. |
| 5 | `RW_PCP_PROPH_SCORE` | NUMERIC |  | The numerical score for the PCP Prophylaxis screening. |
| 6 | `RW_PCP_PROPH_CMTS` | VARCHAR |  | The comments for the PCP Prophylaxis screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

