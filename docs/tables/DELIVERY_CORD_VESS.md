# DELIVERY_CORD_VESS

> This table contains the number of cord vessels for the newborn. This table contains choices selected in Stork's Delivery Summary activity, and is populated in the delivery record. This information is also copied to the OB_EPT_BH_CORD_VES table in the baby's Patient (EPT) record.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEL_CORD_VESSELS_C_NAME` | VARCHAR | org | Stores the number of cord vessels for the newborn. This information is stored in the Delivery Record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

