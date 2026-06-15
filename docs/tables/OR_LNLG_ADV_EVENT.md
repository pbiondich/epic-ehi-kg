# OR_LNLG_ADV_EVENT

> This table contains the Adverse Event information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line (ORM) record. |
| 2 | `ADVERSE_EVENT_C_NAME` | VARCHAR | org | The adverse event category number for the adverse event that occurred. |
| 3 | `ADV_EVENT_TIME` | DATETIME (Local) |  | The time at which the adverse event occurred. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

