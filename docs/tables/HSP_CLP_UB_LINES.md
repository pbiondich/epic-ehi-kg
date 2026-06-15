# HSP_CLP_UB_LINES

> This table maps the hospital transactions on UB claim lines in Hospital Billing, both ordinal printed lines and revenue code lines from the claim print record and can be joined to the lines of HSP_CLP_UB_LINE_TXS.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The hospital transactions line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSP_CLP_REV_CODE_LINE` | INTEGER |  | This item holds the line pointers to the 200 group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

