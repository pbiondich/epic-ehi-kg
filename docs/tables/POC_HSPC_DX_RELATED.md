# POC_HSPC_DX_RELATED

> This table indicates whether the hospice diagnoses at the time of the completed plan of care were hospice related.

**Primary key:** `POC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier (.1 item) for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HOSPICE_RELATED_C_NAME` | VARCHAR |  | Whether the hospice diagnoses at the time of the completed plan of care were hospice related. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

