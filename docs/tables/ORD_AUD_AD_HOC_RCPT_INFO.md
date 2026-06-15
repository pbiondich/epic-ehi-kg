# ORD_AUD_AD_HOC_RCPT_INFO

> This table contains the auditing information about the ad hoc recipient information.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUD_AD_HOC_RCPT_INFO` | VARCHAR |  | This column contains the auditing information about the ad hoc recipient information. The data is in a delimited string of the form, "Fax#\|Phone#\|Street Addr\|City\|State ID\|Zipcode\|Country ID\|County ID ". The source item is located at ORDER_RAD_RECPNT.CC_AD_HOC_INFO. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

