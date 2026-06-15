# CONDITION_ORDER_CONTACT

> It contains order condition-related items.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `COND_TYPE_TEXT` | VARCHAR |  | comment for condition type |
| 5 | `COND_MODIFIER_C_NAME` | VARCHAR | org | modified condition type |
| 6 | `COND_MODIFIER_TEXT` | VARCHAR |  | Adding comment to a modified condition type |
| 7 | `SEG_ORDER_ID` | NUMERIC |  | This item stores the order that a particular report segment is linked to. This order is part of a group of orders that share a result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

