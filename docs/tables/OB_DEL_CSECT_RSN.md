# OB_DEL_CSECT_RSN

> This table contains the category values which correspond to indications for cesarean section. This data comes from the Delivery Summary activity.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. The delivery record ID on which the data is stored. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CESAREAN_REASON_C_NAME` | VARCHAR | org | The category values which correspond to indications for cesarean section. This data comes from the Delivery Summary activity. You should link out to ZC_OB_CSECT_IND_CS.OB_CSECT_IND_CS_C to get the category name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

