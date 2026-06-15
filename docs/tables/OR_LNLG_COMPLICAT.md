# OR_LNLG_COMPLICAT

> This table contains the Complications information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 2  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `COMPLICATIONS_C_NAME` | VARCHAR | org | The complication type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

