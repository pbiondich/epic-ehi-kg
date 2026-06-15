# OR_LNLG_SURG_ATTRE_CHG

> This item stores if surgical attire has been changed, and it can be used for Surgical Site Infection (SSI) reporting. Intra-op nurses will typically document this information in the Site Completion form.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SURG_ATTIRE_CHNG_C_NAME` | VARCHAR | org | Stores if surgical attire has been changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

