# RECONCILE_MA_RA_DX_INFO

> This table contains reconciliation information regarding statuses of diagnoses from Medicare Advantage Risk Adjustment files.

**Primary key:** `CLAIM_RECON_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_RECON_ID` | VARCHAR | PK | The unique identifier (.1 item) for the claim status update record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MA_RA_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `MA_RA_DX_FLAG_C_NAME` | VARCHAR |  | List of flags denoting whether corresponding diagnoses are added, deleted, or not applicable for risk adjustment for this file load. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

