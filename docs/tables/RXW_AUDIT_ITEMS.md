# RXW_AUDIT_ITEMS

> This contains the audit trail item identifiers and values portion for Willow Ambulatory work requests.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_LINE` | INTEGER |  | Line number of SI 92000. |
| 4 | `AUDIT_UPDATE_ITEM` | VARCHAR |  | The item number of the changed item. |
| 5 | `OLD_VALUE` | VARCHAR |  | This contains the value of the item before the update was made. This item is only populated if the item is single response and the item's previous value was not null. |
| 6 | `CONTACT_DAT` | NUMERIC |  | Stores the edited item's contact DAT. |
| 7 | `AUDIT_RM_LINE_RANGE` | VARCHAR |  | This item stores the line range of the old values for an RM item. The range is a caret delimited interval that points to rows in I RXW 92160. |
| 8 | `AUDIT_MULT_REL_LINE` | VARCHAR |  | This contains the line range of the multiple or related response item specified in I RXW 92105. This item is only populated if the item stored in I RXW 92105 is either multiple or related response and that items previous value was not null. If changes are made to any line in the item, then all lines are returned, not just the lines that were updated. For example, for a value of 2^5, the old values of the item are found in lines 2 through 5 in I RXW 92150. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

