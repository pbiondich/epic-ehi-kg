# REG_ABST_ESIGNATURE_DATA

> This table contains information about e-signatures on abstraction records.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ESIGNATURE_KEY` | VARCHAR |  | The unique key of this e-signature. |
| 4 | `ESIGNATURE_METADATA_INDEX` | INTEGER |  | The line in the e-signature metadata that contains the information related to the signature used for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

