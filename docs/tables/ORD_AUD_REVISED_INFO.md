# ORD_AUD_REVISED_INFO

> This table contains audit information about the revised info.

**Overflow family:** [ORD_AUD_REVISED_INFO_2](ORD_AUD_REVISED_INFO_2.md)  
**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVISE_USR_EXTERNAL_VALUES` | VARCHAR |  | This column contains the audit information about all the revising users (external values). The values are delimited by "^". The source item is located at RIS_REVISE_RSLTS.REVISING_USER_ID. This column shows the translated external value as of when the column was last extracted. |
| 4 | `REVISE_USR_EMP_IDS` | VARCHAR |  | This column contains the audit information about all the revising users (IDs). The values are delimited by "^". The source item is located at RIS_REVISE_RSLTS.REVISING_USER_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

