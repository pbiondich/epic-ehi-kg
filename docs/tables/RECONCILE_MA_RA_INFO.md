# RECONCILE_MA_RA_INFO

> This table contains reconciliation information received from Medicare Advantage Risk Adjustment files.

**Primary key:** `CLAIM_RECON_ID`, `CONTACT_DATE_REAL`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_RECON_ID` | VARCHAR | PK | The unique identifier (.1 item) for the claim status update record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `MA_RA_ALLOW_STATUS_C_NAME` | VARCHAR |  | Identifies the status of a claim export whether its diagnoses are allowed for risk adjustment or not. |
| 5 | `MA_RA_ALLOW_RSN_C_NAME` | VARCHAR |  | Indicates the reason why this claim export is allowed, disallowed, or not applicable for risk adjustment. |
| 6 | `MA_RA_ENC_TYPE_C_NAME` | VARCHAR |  | Determines the encounter type of an export defined on an MAO file. |
| 7 | `MA_RA_LINKED_PAYER_REF_NUM` | VARCHAR |  | Payer's control number for an encounter data record being referenced to on a void, replacement, or linked chart review record on an MAO file. |
| 8 | `MA_RA_SUBMIT_DATE` | DATETIME |  | Submission date recorded for an encounter data record or chart review on an MAO-004. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

