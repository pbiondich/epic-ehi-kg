# RYAN_WHITE_SERVICE_DATA

> Ryan White Service Data.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `RW_SRV_DATE` | DATETIME |  | Ryan White service date |
| 3 | `RW_SRV_QTY` | INTEGER |  | Ryan White Service Quantity |
| 4 | `RW_SRV_PRC` | NUMERIC |  | Ryan White Service Price |
| 5 | `RW_SRV_CONT_NAME_C_NAME` | VARCHAR | org | Ryan White service contract name |
| 6 | `RW_SRV_CATEGORY_C_NAME` | VARCHAR | org | Ryan White Service Category |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

