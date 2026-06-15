# RXW_AUDIT_RM_POS_RANGE

> This contains the audit trail's related multiple item positions portion for Willow Ambulatory work requests. This should be used in conjunction with column AUDIT_RM_LINE_RANGE found in table RXW_AUDIT_ITEMS to find the values in table RXW_AUDIT_RM_POS_VALUES.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_RM_POS_RANGE` | VARCHAR |  | This item stores the position range of the old values for an RM item. The range is a caret delimited interval that points to rows in I RXW 92161. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

