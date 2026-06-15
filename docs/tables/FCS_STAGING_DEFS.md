# FCS_STAGING_DEFS

> This table contains information from the Cancer Staging Definitions (FCS) record for each kind of cancer to be staged, such as the type of FCS record, a list of fields that should be available for editing, and which SmartLists to use for restricting entry in those fields.

**Primary key:** `STG_DEF_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STG_DEF_ID` | NUMERIC | PK | The ID of the FCS record containing the Cancer Staging Definitions for a kind of cancer to be staged. |
| 2 | `STG_DEF_NAME` | VARCHAR |  | The name of the FCS record containing the Cancer Staging Definitions for a kind of cancer to be staged. |
| 3 | `FCS_DISP_NAME_VIRTUAL` | VARCHAR |  | The calculated staging form display name considering based record and possible linked override record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

