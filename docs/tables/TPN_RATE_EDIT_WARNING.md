# TPN_RATE_EDIT_WARNING

> Stores information on whether or not a TPN order has rate live-edit warnings and based off of the value we can determine what kind of warning was shown to the user.

**Primary key:** `ORDER_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `TPN_RATE_EDIT_WARN_C_NAME` | VARCHAR |  | Warning that appears during rate live-edit modifications for TPNs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

