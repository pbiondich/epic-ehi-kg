# ASSOCD_ORGANISMS

> This table contains the organisms which have been associated with infection cases. This can be used to find infection cases which were associated with a specific organism or MDRO definition. These are not NHSN pathogens which are stored in NHSN_PS_FORM.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOCD_ORGANISM_ID` | NUMERIC |  | Stores the organisms records associated with the case. The allowed types are " (non-Beaker LLO), 1 (Beaker LLO), and 4 (MDRO Definition). |
| 4 | `ASSOCD_ORGANISM_ID_NAME` | VARCHAR |  | The name of the organism. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

