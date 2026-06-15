# PR_EST_FILTERS

> Contains information on filters that have been applied to price estimate HB historical case codes.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HB_FILTER_DRG_ID` | VARCHAR |  | Contains a DRG code filter for an HB historical case section. |
| 4 | `HB_FILTER_DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 5 | `HB_FILTER_ICD_PX_ID` | VARCHAR |  | Contains an ICD code filter for an HB historical case section. |
| 6 | `HB_FILTER_ICD_PX_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 7 | `HB_FILTER_CPT` | VARCHAR |  | Contains a CPT code filter for an HB historical case section. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

