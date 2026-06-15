# CL_PRL_SS

> This table contains the SmartSet/Protocol/Pathway settings that do not change per contact for each SmartSet, Protocol, Pathway, or Dental Template.

**Primary key:** `PROTOCOL_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROTOCOL_ID` | NUMERIC | PK shared | SmartSet/Protocol ID. |
| 2 | `PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

