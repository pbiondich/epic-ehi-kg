# CL_OSQ

> This table contains the SmartGroup settings that do not change per contact for each SmartGroup.

**Primary key:** `ORDERSET_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDERSET_ID_ORDERSET_NAME` | VARCHAR |  | The SmartGroup record name. This is different from the display name, which is stored in CL_OSQ_OT.DISPLAY_NAME. |
| 2 | `ORDERSET_NAME` | VARCHAR |  | The SmartGroup record name. This is different from the display name, which is stored in CL_OSQ_OT.DISPLAY_NAME. |
| 3 | `DISPLAY_NAME_NO_ADD` | VARCHAR |  | A no-add display name for an OSQ record |
| 4 | `OVRD_VERSION_NAME` | VARCHAR |  | The user entered version name for the User Order Set override record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

