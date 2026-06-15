# AN_HGM_RECORD_INFO

> This table stores the Scripting template (HGM) record information such as the type and context of each record.

**Primary key:** `RECORD_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID of the macro record for this row. |
| 2 | `RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the Scripting Template. |
| 3 | `RECORD_NAME` | VARCHAR |  | The name of the Scripting Template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

