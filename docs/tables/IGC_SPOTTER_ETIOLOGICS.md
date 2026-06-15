# IGC_SPOTTER_ETIOLOGICS

> Data for the inpatient rehab facility (IRF) preadmission, including data from the IGC Spotter section.

**Primary key:** `HLV_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier for the value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REGISTRY_DATA_ID` | NUMERIC | shared | The unique identifier for the registry data record. |
| 4 | `ETIOLOGIC_DIAGNOSES_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

