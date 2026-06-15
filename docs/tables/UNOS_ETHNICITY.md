# UNOS_ETHNICITY

> The candidate's race. On UNOS forms prior to the 2023 version, this table also included the candidate's ethnicity. Starting with the 2023 version of the UNOS forms, ethnicity data is now stored in UNOS_INFO.UNOS_ETHNICITY_C.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UNOS_ETHNICITY_C_NAME` | VARCHAR |  | The candidate's race. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

