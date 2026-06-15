# OR_LNLG_SURG_STAFF

> This table contains the Surgical Staff information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the Line (ORM) record |
| 2 | `STAFF_RTLS_OFF_YN` | VARCHAR |  | Whether RTLS tracking has been manually turned off for the provider on this case log. |
| 3 | `STAFF_PRIMARY_PROV_THIN_LOG_YN` | VARCHAR |  | USED ONLY FOR THIN LOGS. Marks a provider as the primary on a procedure. Only one provider per log can be marked as primary. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

