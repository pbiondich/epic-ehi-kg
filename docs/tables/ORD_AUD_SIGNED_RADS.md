# ORD_AUD_SIGNED_RADS

> This table contains audit information about all signing physicians who took an action on the imaging study.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SIGNED_RAD_EXTERNAL_VALUES` | VARCHAR |  | This column stores an audited list of the imaging physicians that have signed an order. The values are delimited by "^". The source item is located at RIS_SGND_INFO.SIGNED_PROV_ID. This column shows the translated external value as of when the column was last extracted. |
| 4 | `SIGNED_RAD_IDS` | VARCHAR |  | Stores an audited list of the imaging physicians that have signed an order. The values are delimited by "^". The source item is located at RIS_SGND_INFO.SIGNED_PROV_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

