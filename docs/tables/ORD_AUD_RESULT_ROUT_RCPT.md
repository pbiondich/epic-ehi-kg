# ORD_AUD_RESULT_ROUT_RCPT

> This table contains the auditing information about the results routing recipients.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUD_RESULT_ROUTING_RCPT` | VARCHAR |  | This column contains the auditing information about the results routing recipients. The data is in a carat delimited string of the form, "INI^ID^Recipient Name^System Flag". The source item is located at ORDER_RAD_RECPNT.CC_RECIPIENTS_LIST. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

