# DTX_ALL

> This table contains information common across all detail transaction (DTX) records in the system for filtering purposes.

**Primary key:** `TX_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `TX_TYPE_C_NAME` | VARCHAR |  | The type of the transaction. |
| 3 | `TX_STATUS_C_NAME` | VARCHAR |  | The status of the transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

