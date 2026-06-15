# RECONCILE_SVC_ACDT

> This table contains raw line-level action codes received through claims reconciliation. This information is only populated if the line-level action code was not mapped to an Epic category value.

**Primary key:** `CLAIM_RECON_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_RECON_ID` | VARCHAR | PK | The unique identifier for the claim reconciliation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `LN_ACTION_DATA` | VARCHAR |  | Line-level action code. This value is only populated if the line-level action code does not match any category abbreviation inside of the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

