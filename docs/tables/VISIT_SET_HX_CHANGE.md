# VISIT_SET_HX_CHANGE

> The VISIT_SET_HX_CHANGE table contains details of what items were modified in a revision of a visit set. Information about the user modifying the visit set and the time of modification can be found in VISIT_SET_HX_REVISION.

**Primary key:** `VISIT_SET_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit set record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_TRAIL_REVISION` | INTEGER |  | The revision in which this update was made. Corresponds with a line of VISIT_SET_HX_REVISION. |
| 4 | `AUDIT_TRAIL_ITEM` | VARCHAR |  | The number of the item that was updated |
| 5 | `AUDIT_TRAIL_LINE` | INTEGER |  | The line of the item in AUDIT_TRAIL_ITEM being updated. 1 for single response items. |
| 6 | `AUDIT_TRAIL_NEW_VALUE` | VARCHAR |  | The new value of the item in AUDIT_TRAIL_ITEM at the line in AUDIT_TRAIL_LINE, after the update is made. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

