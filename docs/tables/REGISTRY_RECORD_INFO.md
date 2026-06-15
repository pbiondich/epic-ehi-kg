# REGISTRY_RECORD_INFO

> This table contains registry record information that might be considered electronic health information (EHI).

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `REGISTRY_ID` | NUMERIC | shared | The associated registry settings record (HFR) that this registry record (RDI) is used for. |
| 4 | `REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the registry record. |
| 5 | `REG_OVERRIDE_CONTEXT` | VARCHAR |  | Stores the override context string to identify the correct override record for the registry settings record (HFR) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

