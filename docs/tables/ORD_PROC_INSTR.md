# ORD_PROC_INSTR

> This table contains information about order-specific procedure process instructions clinicians see in Order Composer when they sign the order. This item is essentially a SmartText block, which might contain SmartLinks, that is pulled in from the networked Proces Info (I EAP 10650) item at signing.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_PROC_INSTR` | VARCHAR |  | Process Instructions displayed to end user in the order editing window when signing the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

