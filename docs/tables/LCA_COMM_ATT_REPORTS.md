# LCA_COMM_ATT_REPORTS

> This table extracts the related multiple response item LCA-455.

**Primary key:** `COMMUNICATION_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the routing record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `ATT_RECPNT_REPORTS_ID` | VARCHAR |  | The reports received by each attachment and recipient pair in I LCA 450 |
| 5 | `ATT_RECPNT_REPORTS_ID_REPORT_NAME` | VARCHAR |  | The name of the report |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

