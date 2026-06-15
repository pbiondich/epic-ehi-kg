# UNOS_MALIG_HX_TYPE

> If the patient has a history of malignant cancer, this table displays the types of tumors as defined by the United Network for Organ Sharing (UNOS).

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UNOS_MALIG_HX_TY_C_NAME` | VARCHAR |  | If the patient has a history of malignant cancer, indicates the types of tumors. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

