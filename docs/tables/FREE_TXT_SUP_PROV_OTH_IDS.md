# FREE_TXT_SUP_PROV_OTH_IDS

> The other IDs of the free-text supervising provider. For instance, a state-specific ID number, such as the Texas Department of Public Safety (DPS) number.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ID_NUM` | VARCHAR |  | This is the ID number for other IDs of the free-text supervising provider. |
| 4 | `ID_TYPE_ID` | NUMERIC |  | The unique identifier for the ID types for other IDs of the free-text supervising provider. |
| 5 | `ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

