# V_EHI_ELEM_VAL_PREV_CAPTION

> This view contains the historical captions for SmartData element values.

**Primary key:** `HLV_ID`, `UPDATE_NUM`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `UPDATE_NUM` | INTEGER | PK | This column groups together rows of data that were stored together. A higher UPDATE_NUM means a more recent update. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `PREVIOUS_CAPTION` | VARCHAR |  | This column stores the previous captions for SmartData element values. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

