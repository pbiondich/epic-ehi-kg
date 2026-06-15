# DELIVERY_ANES_MTHD

> This table contains anesthesia methods that were selected in Stork's Delivery Summary activity and populated in the delivery record. This information is also copied to the OB_EPT_BH_ANSTHSIA table in the baby's Patient (EPT) record.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEL_ANESTH_METHOD_C_NAME` | VARCHAR | org | This item stores the anesthesia method that was in use at the time of delivery. This information is stored in the Delivery Record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

