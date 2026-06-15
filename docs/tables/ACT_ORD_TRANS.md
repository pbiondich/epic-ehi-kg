# ACT_ORD_TRANS

> Action order transcription user and instant information.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACT_ORD_TRAN_USR_ID` | VARCHAR |  | The unique identifier of the user who transcribes the order as being active to the paper Medication Administration Record (MAR). |
| 4 | `ACT_ORD_TRAN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ACT_ORDER_TRAN_DTTM` | DATETIME (Local) |  | The instant (date/time) that the user transcribes the order as being active to the paper MAR (medication administration record). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

