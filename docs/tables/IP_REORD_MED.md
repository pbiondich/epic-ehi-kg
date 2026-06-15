# IP_REORD_MED

> This table displays reordered medication information.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier for the inpatient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORIGINAL_ERX_IP` | VARCHAR |  | The original reordered medication ID. |
| 4 | `SUBSTITUTE_ERX_IP` | VARCHAR |  | The substitute for the reordered medication ID. |
| 5 | `OLD_ORDER_ID_IP` | VARCHAR |  | The reordered current medication ID. |
| 6 | `REORD_PEND_IP_YN` | VARCHAR |  | Stores if the reorderd medication is pending or not. |
| 7 | `NEW_ORDER_ID_IP` | VARCHAR |  | The new reordered current medication ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

