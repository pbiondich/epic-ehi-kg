# MGRP

> The MGRP table contains a list of member groups, which are used to identify member populations under different circumstances.

**Primary key:** `MGRP_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MGRP_ID_MEM_GRP_NAME` | VARCHAR |  | The name of the member group |
| 2 | `MEM_GRP_NAME` | VARCHAR |  | The name of the member group |
| 3 | `CAP_MEM_LIMIT_MAX_AGE` | INTEGER |  | Members exceeding this age will not be considered towards the member limit when computing capitation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

