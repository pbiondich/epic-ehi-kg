# STMT_NOTIF_SMARTMARKUP

> *** Deprecated *** Contains the mnemonics used to resolve the content for the statement notification.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the stmt/det bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SMARTMARKUP_MNEM` | VARCHAR |  | Stores the mnemonics used while resolving SmartMarkup for the notification content of this statement. |
| 4 | `SMARTMARKUP_VALUE` | VARCHAR |  | The SmartMarkup values used when resolving the notification content. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

