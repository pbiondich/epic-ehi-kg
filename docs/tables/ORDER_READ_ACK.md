# ORDER_READ_ACK

> This table is used to store information from the overtime-related Orders items used for the result read/acknowledgment tracking feature. Namely, this is the Read or Acknowledge by User (I ORD 1910) and Read or Acknowledged On (I ORD 1915) items.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for when and who viewed the results associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `READ_ACK_ACTUAL_UTC_DTTM` | DATETIME (UTC) |  | This item stores when the result was actually viewed by an end user. |
| 6 | `WHO_READ_ACK_EMP_ID` | VARCHAR |  | This item stores which user viewed this result. |
| 7 | `WHO_READ_ACK_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

