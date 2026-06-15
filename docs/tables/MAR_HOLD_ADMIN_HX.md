# MAR_HOLD_ADMIN_HX

> MAR (medication administration record) hold/unhold administration history.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HOLD_ALL_MAR_ADMINS` | VARCHAR |  | Indicates if the medication is held (doses should not be administered temporarily) or unheld on the medication administration record (MAR). |
| 4 | `MAR_UNHOLD_ALL_DTTM` | DATETIME (Local) |  | The instant when an order is held/unheld on the MAR (medication administration record). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

