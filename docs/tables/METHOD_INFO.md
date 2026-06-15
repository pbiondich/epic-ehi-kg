# METHOD_INFO

> The METHOD_INFO table contains record level information for instrument interface, method, method grouper, and middle tier interface records.

**Primary key:** `METHOD_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `METHOD_ID` | VARCHAR | PK | The unique ID of the instrument interface, method, method grouper, or middle tier interface record. |
| 2 | `METHOD_ID_METHOD_NAME` | VARCHAR |  | The name of the instrument interface, method, method grouper, or middle tier interface record. |
| 3 | `METHOD_NAME` | VARCHAR |  | The name of the instrument interface, method, method grouper, or middle tier interface record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

