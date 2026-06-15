# CLARITY_HIP

> In Basket Registries store information to determine the recipients who can display and handle specific types of messages. This table contains the basic information about these Registries. Registries are stored in the HIP master file.

**Primary key:** `REGISTRY_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_ID` | NUMERIC | PK shared | The Registration Identification Number |
| 2 | `REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 3 | `REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

