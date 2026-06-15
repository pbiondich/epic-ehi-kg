# DELIVERY_ANALGES

> This table contains analgesics that were selected in Stork's Delivery Summary activity and populated in the delivery record. This information is also copied to the OB_EPT_BH_ANLGESIA table in the baby's Patient (EPT) record.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEL_ANALGESIC_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

