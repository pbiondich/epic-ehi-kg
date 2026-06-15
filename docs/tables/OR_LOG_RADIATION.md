# OR_LOG_RADIATION

> Clarity table to store the radiation info in log.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RAD_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `RAD_TYPE_C_NAME` | VARCHAR | org | The type of radiation from the fluoroscopy being performed. |
| 5 | `RAD_DOSE` | NUMERIC |  | The amount of radiation from the fluoroscopy being performed. |
| 6 | `RAD_UNIT_C_NAME` | VARCHAR | org | The unit of radiation from the fluoroscopy being performed. |
| 7 | `RAD_FLUORO_MINUTES` | NUMERIC |  | The duration of the fluoroscopy being performed. |
| 8 | `RAD_DAP` | NUMERIC |  | The dose area product from the fluoroscopy being performed. |
| 9 | `RAD_PANEL` | INTEGER |  | The panel associated with the documented radiation information. |
| 10 | `RAD_PANEL_COMMENT` | VARCHAR |  | The comments associated with the radiation type on the panel. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

