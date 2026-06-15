# CNR_COMP_INFO

> The no-add single response data for the Compounding and Repackaging (CNR) master file.

**Primary key:** `RECORD_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the Compounding and Repackaging record. Compounding and repackaging records represent the products created when pharmacists combine multiple medications to create a new medication or take one medication from a container and place it into another container. |
| 2 | `RECORD_NAME` | VARCHAR |  | The name of the Compounding and Repackaging record. Compounding and repackaging records represent the products created when pharmacists combine multiple medications to create a new medication or take one medication from a container and place it into another container. |
| 3 | `DISPENSE_CODE_C_NAME` | VARCHAR | org | Dispense Code for the compounded or repackaged product. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

