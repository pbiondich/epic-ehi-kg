# ORD_AUD_ATTACHED_PROTCL

> This table contains audit information about the list of protocols which have been assigned to the imaging order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROTOCOL_EXTERNAL_VALUES` | VARCHAR |  | Audit of the list of protocols (external values) which have been assigned to the imaging order. The values are delimited by "^". The source item is located at PROTOCOL_INFO.ASGN_PROTOCOL_ID. This column shows the translated external value as of when the column was last extracted. |
| 4 | `PROTOCOL_LQF_IDS` | VARCHAR |  | Audit of the list of protocols (IDs) which have been assigned to the imaging order. The values are delimited by "^". The source item is located at PROTOCOL_INFO.ASGN_PROTOCOL_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

