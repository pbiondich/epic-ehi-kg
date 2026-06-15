# DC_ORD_TRANS

> User and instant info of the order which is transcribed as being discontinued to the paper MAR (medication administration record).

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DC_ORD_TRAN_USR_ID` | VARCHAR |  | User who transcribes the order as being discontinued to the paper MAR (medication administration record). |
| 4 | `DC_ORD_TRAN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `DC_ORD_TRAN_IN_DTTM` | DATETIME (Local) |  | Instant (date/time) that the order was transcribed as being discontinued to the paper MAR (medication administration record). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

