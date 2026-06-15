# SDOH_DOM_CONFIG_SOURCES

> This table stores the sources that identify a patient's social risk factors or social needs for a social drivers of health domain configuration.

**Primary key:** `DOM_CONFIG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOM_CONFIG_ID_RECORD_NAME` | VARCHAR |  | The name of the social driver domain configuration record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SRC_DOM_CONFIG_ID_RECORD_NAME` | VARCHAR |  | The name of the social driver domain configuration record. |
| 4 | `SOURCES_OVERRIDE_DISP_NAME` | VARCHAR |  | The override display name of the social driver domain configuration record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

