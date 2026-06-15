# VISIT_SET_SLOT_HX_CHANGE

> The VISIT_SET_SLOT_HX_CHANGE table contains details of what slot items were modified in a revision of a slot. Information about the revision can be found in VISIT_SET_SLOT_HX_RVSN.

**Primary key:** `VISIT_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact. |
| 5 | `AUDIT_SLOT_REVISION` | INTEGER |  | The revision number for this set of changes to a slot. Coincides with a line of VISIT_SET_SLOT_HX_REVISION. |
| 6 | `AUDIT_SLOT_ITEM` | VARCHAR |  | The slot item changed |
| 7 | `AUDIT_SLOT_NEW_VALUE` | VARCHAR |  | The value that the item in AUDIT_SLOT_ITEM was changed to for this revision. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

