# OR_LNLG_PRE_SKIN

> This table contains the Preop Skin information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 3  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `PREOP_SKIN_SITE_C_NAME` | VARCHAR | org | The pre-op skin site. |
| 3 | `PREOP_SKIN_LAT_C_NAME` | VARCHAR | org | Indicates the laterality of a pre-op skin site. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

