# DELIVERY_GAS_SENT

> This table contains documentation on the cord gasses that were sent, including specification of whether or not gases were sent. This information is entered in Stork's Delivery Summary activity and populated in the delivery record.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BIRTH_GASES_SENT_C_NAME` | VARCHAR | org | The sent cord gas category ID for the delivery record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

