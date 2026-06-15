# FAM_DOC_GEN_AUD_TRL

> This table stores data for the generic audit trail from a family document.

**Primary key:** `FAM_DOC_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FAM_DOC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the family document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GEN_AUD_UPDATE_ITEM` | INTEGER |  | The number of the item in the general audit table that was updated. |
| 4 | `GEN_AUD_PREV_VAL` | VARCHAR |  | The previous value stored for the item. |
| 5 | `GEN_AUD_NEW_VALUE` | VARCHAR |  | The new value stored for the item. |
| 6 | `GEN_AUD_UPDATE_USER_ID` | VARCHAR |  | The ID of the user who updated the item. |
| 7 | `GEN_AUD_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `GEN_AUD_UPDATE_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the item was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAM_DOC_ID` | [FAM_DOC](FAM_DOC.md) | sole_pk | high |

