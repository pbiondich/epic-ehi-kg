# HSPC_HIS_VOID_HX

> This table contains a history of all void actions and undo void actions that have occurred for this item set.

**Primary key:** `OASIS_SET_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the data set record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IS_VOID_YN` | VARCHAR |  | This items stores if this was a void action. If set to false, then this action was undoing a void. |
| 4 | `VOID_OR_UNDO_VOID_USER_ID` | VARCHAR |  | This item stores the user associated with the void or undo void action. |
| 5 | `VOID_OR_UNDO_VOID_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `VOID_OR_UNDO_VOID_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant at which the void or undo void occurred. |
| 7 | `VOID_OR_UNDO_VOID_COMMENT` | VARCHAR |  | This item stores the comment added while performing a void or undo void action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OASIS_SET_ID` | [HH_OASIS_INFO](HH_OASIS_INFO.md) | sole_pk | high |

