# EXT_ADDRESS

> The EXT_ADDRESS table contains information about Care Everywhere Direct message recipients. The records in this table are Direct addresses of external recipients (DXA records) designated for Care Everywhere.

**Primary key:** `EXT_ADDRESS_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXT_ADDRESS_ID` | NUMERIC | PK | The unique identifier (.1 item) for the recipient record. |
| 2 | `MIXED_DIRECT_ADDR` | VARCHAR |  | Formatted like an email address, this is how Direct messaging knows where to send a message. This item is stored in mixed case to use in display in addressing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

