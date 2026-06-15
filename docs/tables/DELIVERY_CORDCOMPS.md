# DELIVERY_CORDCOMPS

> This table contains newborn-specific cord complications, selected in Stork's Delivery Summary activity, populated in the delivery record. This information is also copied to the OB_EPT_BH_CRDCOMPS table in the baby's Patient (EPT) record.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEL_CORD_COMP_C_NAME` | VARCHAR | org | Stores the cord complication types. This information is stored in the Delivery Record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

