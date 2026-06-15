# ORD_AUD_RCPT_ROUTING_ADDR

> This table contains the auditing information about the recipient's routing address.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUD_RCPT_ROUTING_ADDR` | VARCHAR |  | This column contains the auditing information about the recipient's routing address. If the recipient has an SER or EMP record with multiple addresses, this item contains a dash-delimited string with the SER or EMP .1 and the ID number of the address to which the result will be routed. This item is null when the recipient has no SER or EMP record. For SER recipients, the address ID corresponds to SER 21000, which is available in Clarity. The source item is located at ORDER_RAD_RECPNT.ROUTING_ADDRESS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

