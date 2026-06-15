# ODC_REC_STATUS_HX

> The ODC_REC_STATUS_HX table contains the status history information for the order context record.

**Primary key:** `ORDER_CONTEXT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_CONTEXT_ID` | NUMERIC | PK FK→ | The unique identifier for the order context record, which contains information about when orders are intended to be used. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SDFL_EDIT_INST_DTTM` | DATETIME (UTC) |  | The instant that the record status was changed. |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | The user who changed the record status. |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTION_C_NAME` | VARCHAR |  | The record status flag category ID for the action that was applied to the order context record status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_CONTEXT_ID` | [ODC_BASIC](ODC_BASIC.md) | sole_pk | high |

