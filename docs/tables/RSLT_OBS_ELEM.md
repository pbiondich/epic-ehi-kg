# RSLT_OBS_ELEM

> The RSLT_OBS_ELEM table contains data about observation elements (stored in RES records). Observations include findings such as pulmonary nodules. Elements are characteristics of the observation, such as size and composition.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ELEM_CODE` | VARCHAR |  | The element codes corresponding to each element value (I RES 52572) in the observation. |
| 4 | `ELEM_NAME` | VARCHAR |  | The display name for the element code (I RES 52570). |
| 5 | `ELEM_VALUE` | VARCHAR |  | The value of the data element (I RES 52570). |
| 6 | `ELEM_DISPLAY_VALUE` | VARCHAR |  | The display name for the element value (I RES 52572). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

