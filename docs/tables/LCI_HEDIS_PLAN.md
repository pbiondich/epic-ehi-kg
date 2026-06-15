# LCI_HEDIS_PLAN

> Clarity table for the HEDIS plan related items in LCI.

**Primary key:** `EXTERNAL_CVG_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the external coverage record record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `HEDIS_PLAN_EFF_DATE` | DATETIME |  | The effective date for an NCQA HEDIS plan of an external coverage contact. |
| 5 | `HEDIS_PLAN_TERM_DATE` | DATETIME |  | The termination date for an NCQA HEDIS plan of an external coverage contact. |
| 6 | `HEDIS_PLAN_TYPE_C_NAME` | VARCHAR |  | The plan type for an NCQA HEDIS plan of an external coverage contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

