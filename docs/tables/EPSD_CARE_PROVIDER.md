# EPSD_CARE_PROVIDER

> This table contains information about the providers specific to this episode of care.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID assigned to the episode record (HSB .1). |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `CARE_ROLE_C_NAME` | VARCHAR | org | The role in the caretaking process that the associated provider is playing, for this episode of care. |
| 4 | `CARE_PROVIDER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `PROV_ADDR_ID_UNIQUE` | VARCHAR |  | The ID of the address used to contact a provider for this episode. The value here matches up with one of the provider's address identifiers (SER item 21000). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

