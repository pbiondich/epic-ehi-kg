# CL_CLM_GRP

> The CL_CLM_GRP table is the master table for whole claim component group (CMC) records. These whole claim component group records are often networked from Vendor-Network Contract or Benefit Package tables.

**Primary key:** `CLM_GRP_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLM_GRP_ID_COMP_GRP_NAME` | VARCHAR |  | The name for the whole claim component group. |
| 2 | `COMP_GRP_NAME` | VARCHAR |  | The name for the whole claim component group. |
| 3 | `DESCRIPTION` | VARCHAR |  | The description of the whole claim component group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

