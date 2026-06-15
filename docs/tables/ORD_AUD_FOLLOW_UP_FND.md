# ORD_AUD_FOLLOW_UP_FND

> This table contains the auditing information related to the follow up findings.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUDIT_FOLLOW_UP_FINDING_ID` | NUMERIC |  | The unique identifier of the result finding that is the current value of the result tracking finding follow-up. Whenever ORD_RSLT_TRK_FND_FOLLOWUP.FOLLOWUP_FINDING_ID is changed, this column will store the current value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

