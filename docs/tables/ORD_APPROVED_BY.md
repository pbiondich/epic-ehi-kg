# ORD_APPROVED_BY

> This table contains information about the order approval, including approving user, and time at which the order was approved.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `APRV_BY_USER_ID` | VARCHAR |  | The ID of the user who approved an edited result. |
| 6 | `APRV_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `APRV_BY_INST_DTTM` | DATETIME (Local) |  | The time stamp of the instant the edited result was approved. |
| 8 | `APRV_BY_CNCT_DT` | DATETIME |  | The contact date that the edited result was approved. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

