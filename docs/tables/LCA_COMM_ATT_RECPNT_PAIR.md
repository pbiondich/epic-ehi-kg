# LCA_COMM_ATT_RECPNT_PAIR

> This table contains information regarding all attachments sent in a communication routing job. The information is used to look up which reports were sent to which users.

**Primary key:** `COMMUNICATION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the routing record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTACH_RECPNT_PAIR` | VARCHAR |  | The key for each attachment/recipient pair who received reports for this routing record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

