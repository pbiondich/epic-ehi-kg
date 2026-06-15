# ORDER_TODAYS_FOCUS_HX

> Audit history for orders being marked as today's focus.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_TODAYS_FOCUS_YN` | VARCHAR |  | This item shows the audit trail for the "Patient Availability - Is Today's Focus?" item (I ORD 34390). The item can be set through Patient Availability print group. |
| 4 | `HX_TODAYS_FOCUS_UTC_DTTM` | DATETIME (UTC) |  | This item shows the instant that the "Patient Availability - Is Today's Focus?" item (I ORD 34390) was changed to the value in this row. |
| 5 | `HX_TODAYS_FOCUS_USER_ID` | VARCHAR |  | This item shows the user that updated the "Patient Availability - Is Today's Focus?" item (I ORD 34390) to the value in this row. |
| 6 | `HX_TODAYS_FOCUS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

