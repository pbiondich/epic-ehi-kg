# IP_REORDER_RX

> This table contains reordered meds information.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `ORIGINAL_ERX` | VARCHAR |  | The original medication the patient was using. |
| 4 | `REOR_ORDER_MED_ID` | NUMERIC |  | The order ID of the medication being reordered. |
| 5 | `NEW_ORDER_MED_ID` | NUMERIC |  | The new order ID for the medication. |
| 6 | `REORDRD_MED_PEND_YN` | VARCHAR |  | This determines if the reordered medication is a pending order. |
| 7 | `SUBSTITUTE_ERX` | VARCHAR |  | The substitute medication ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

