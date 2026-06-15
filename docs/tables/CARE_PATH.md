# CARE_PATH

> Care Path information.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `CARE_PATH_ID_LOCATOR_NAME` | VARCHAR |  | The name of the Locator record. |
| 3 | `CARE_PATH_ACTV_PATH_ID_LOCATOR_NAME` | VARCHAR |  | The name of the Locator record. |
| 4 | `CARE_PATH_ACTV_STEP` | INTEGER |  | The step on a care path where the patient is currently. |
| 5 | `CARE_PATH_PARENT_EP_ID` | NUMERIC |  | This item contains a link to the parent episode for this care path. |
| 6 | `CARE_PATH_INIT_EP_ID` | NUMERIC |  | The Episode ID of the initiating care path episode. |
| 7 | `CARE_PATH_INIT_LINE` | INTEGER |  | The line number from the step history of the initiating care path episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

