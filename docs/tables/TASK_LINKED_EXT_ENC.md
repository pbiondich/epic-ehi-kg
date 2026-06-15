# TASK_LINKED_EXT_ENC

> Holds the reference ID for the external event that triggered task creation in the Task Engine.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_ENC_REFERENCE` | VARCHAR |  | This item stores the base DXR reference ID of each external encounter currently linked to the task. |
| 4 | `EXT_ORGANIZATION_ID` | NUMERIC |  | This item stores the DXO ID of each external encounter currently linked to the task. |
| 5 | `EXT_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

