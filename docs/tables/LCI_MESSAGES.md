# LCI_MESSAGES

> The set identifier(s) associated with an LCI record along with the last message (AMS) record that impacted it.

**Primary key:** `EXTERNAL_CVG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the external coverage record record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BLK_DTA_MESSAGE_ID` | NUMERIC |  | Contains the indexed AMS pointer to the last bulk data message record to impact this LCI record per set identifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

