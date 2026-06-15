# RYAN_WHITE_RECEIPT_DATA

> Ryan White Service Receipts Data.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_SRV_RCPT_DATE` | DATETIME |  | Ryan White Service Receipt Date |
| 4 | `RW_SRV_RCPT_AMOUNT` | NUMERIC |  | Ryan White Service Receipt Amount |
| 5 | `RW_SRV_RCPT_SRC_C_NAME` | VARCHAR | org | Ryan White Service Receipt Source |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

