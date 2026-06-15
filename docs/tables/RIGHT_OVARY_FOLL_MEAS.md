# RIGHT_OVARY_FOLL_MEAS

> Follicle measurements from the right ovary.

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
| 5 | `RIGHT_AVERAGE` | NUMERIC |  | The average of all the measurements taken for a follicle in the right ovary. |
| 6 | `RIGHT_DIMENSION_1` | NUMERIC |  | The first dimension measurement for a follicle in the right ovary. |
| 7 | `RIGHT_DIMENSION_2` | NUMERIC |  | The second dimension measurement for a follicle in the right ovary. |
| 8 | `RIGHT_DIMENSION_3` | NUMERIC |  | The third dimension measurement for a follicle in the right ovary. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

