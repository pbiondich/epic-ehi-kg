# ARPB_TX_REFCOM_HX

> Refund request comment history.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REFUND_CMT_DTTM` | DATETIME (Local) |  | Instant a refund comment was made. |
| 4 | `REFUND_CMT_TEXT` | VARCHAR |  | Refund comment created when reviewing refund. |
| 5 | `REFUND_CMT_USER_ID` | VARCHAR |  | User who created the refund comment. |
| 6 | `REFUND_CMT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

