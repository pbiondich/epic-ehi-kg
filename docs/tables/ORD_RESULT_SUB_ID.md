# ORD_RESULT_SUB_ID

> Mapping of SUB_ID (I ORD 2080) values to Result Findings (RES) records (for administrable procedures).

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the child/instance order that has been resulted (via a blood bank interface) with information about units of blood that are available for transfusion into the patient associated with this order ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RES_TO_SUB_IDN` | VARCHAR |  | The internal identifier for this order ID which matches to a subset of the lines (via item ORD 2080) in related group for results (item ORD 2000). This item is only populated if a corresponding results findings (RES) record has been created. |
| 6 | `RES_TO_SUBID_RES_ID` | NUMERIC |  | The unique ID of the result finding that is unique for a given supply/drug substitution (SUB) ID and order ID pair. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

