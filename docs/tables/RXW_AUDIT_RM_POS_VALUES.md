# RXW_AUDIT_RM_POS_VALUES

> This contains the audit trail's related multiple item values portion for Willow Ambulatory work requests. The values are linked to the postion ranges found in RXW_AUDIT_RM_POS_RANGE.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_RM_POS_VAL` | VARCHAR |  | This item stores the old values of positions that have changed in an RM item. The range of the position changes are defined as a caret delimited interval in I RXW 92160. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

