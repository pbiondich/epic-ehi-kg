# HOME_INFUSION_EPSD_HX

> Home Infusion episode history.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RXHX_SVC_PAUSED_YN` | VARCHAR |  | History of service pause flag |
| 4 | `RXHX_START_DATE` | DATETIME |  | History of Start Date |
| 5 | `RXHX_END_DATE` | DATETIME |  | History of the end date |
| 6 | `RXHX_LINE_TYPE_C_NAME` | VARCHAR | org | History of Line Type |
| 7 | `RXHX_LUMENS_NUM` | INTEGER |  | History of number of lumens |
| 8 | `RXHX_IP_LDA_ID` | VARCHAR |  | The unique ID of an LDA linked to the home infusion episode |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

