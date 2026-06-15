# FLAG_INFO

> Contains information about the flag records. These include name, type, description, and applicable external error codes. Flags are used by Ambulatory Pharmacy to mark fill requests as needing additional review.

**Primary key:** `RECORD_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID of a flag record. |
| 2 | `RECORD_ID_RECORD_NAME` | VARCHAR |  | The flag name. |
| 3 | `RECORD_NAME` | VARCHAR |  | The flag name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

