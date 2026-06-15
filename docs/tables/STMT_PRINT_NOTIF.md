# STMT_PRINT_NOTIF

> Stores information about when a MyChart/non-MyChart statement/detail bill notification was sent to the guarantor.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIF_DTTM` | DATETIME (UTC) |  | Stores the instant when a MyChart/non-MyChart statement/detail bill notification was sent to the guarantor. |
| 4 | `NOTIF_DEST_TYPE_C_NAME` | VARCHAR |  | Stores the destination type to which the statement/detail bill notification was sent. |
| 5 | `NOTIF_DEST` | VARCHAR |  | Stores the destination to which the statement/detail bill notification was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

