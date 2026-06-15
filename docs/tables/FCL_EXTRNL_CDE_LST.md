# FCL_EXTRNL_CDE_LST

> The list value database (FCL) stores information about data as defined by external specifications, for example NCPDP claim adjudication. This table stores information about those list values.

**Primary key:** `EXT_CODE_LST_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXT_CODE_LST_ID` | NUMERIC | PK | The unique identifier for the list/value record. |
| 2 | `EXT_CODE_LST_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 3 | `EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

