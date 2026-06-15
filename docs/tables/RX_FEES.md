# RX_FEES

> This table contains the processing fees associated with the work request.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FEE_TYPE_C_NAME` | VARCHAR | org | This item contains the fee type of a work request fee. |
| 4 | `FEE_ORDER_ID` | NUMERIC |  | This item contains the fee order representing a work request fee. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

