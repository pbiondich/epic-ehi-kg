# TXT_ORDPROV_OTH_ID

> This clarity table holds the other IDs of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. For instance, a state-specific ID number, such as the Texas Department of Public Safety (DPS) number.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TXT_ORDPROV_OTH_ID` | VARCHAR |  | The other ID of the ordering provider if the provider does not exist in Epic. (For instance, a state-specific ID number, such as the Texas DPS number). |
| 4 | `TXT_ORDPROV_TYP_ID` | NUMERIC |  | The ID type for other IDs of the ordering provider if the provider does not exist in Epic. (For instance, a state-specific ID number, such as the Texas DPS number.) |
| 5 | `TXT_ORDPROV_TYP_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

