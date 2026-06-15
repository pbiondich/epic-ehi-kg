# HH_MED_INCL_POC_CSN_INFO

> This table stores information about which plans of care this medication order is included in.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INCL_POC_CSN_ID` | NUMERIC |  | For home health patients, this item stores the Plan of Care record CSNs that include this medication. |
| 4 | `WHICH_SIGS_ON_POC_C_NAME` | VARCHAR |  | This column stores which medication sigs to show on the plan of care referred to in column INCL_POC_CSN_ID. This indicates whether the plan of care shows the prescribed sig, a taking differently sig, or both. |
| 5 | `WHICH_PTD_LINE_ON_POC` | INTEGER |  | The line number of the taking differently sig that is displayed for this medication on a plan of care. This column refers to the LINE column |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

