# RECONCILE_CLAIM_STATUS

> This table contains claim-level status code information for claims reconciliation.

**Primary key:** `CLAIM_RECON_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_RECON_ID` | VARCHAR | PK | The unique identifier for the claim reconciliation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CLM_STAT_CODE_C_NAME` | VARCHAR | org | Claim level status code received in a reconciliation file if value matches codes in the current claim status code category. |
| 6 | `CLM_STAT_DATA` | VARCHAR |  | Claim level status code received in a reconciliation file. Set only if the value does not match a category abbreviation in the current claim status code category. |
| 7 | `CLM_CAT_CODE_C_NAME` | VARCHAR | org | Claim level category code received in a reconciliation file if value matches codes in the claim status category code category. |
| 8 | `CLM_CAT_CODE_DATA` | VARCHAR |  | Claim level category code received in a reconciliation file. Set only if the value does not match a category abbreviation in the claim status category code category. |
| 9 | `CLM_MAPPED_ACT_C_NAME` | VARCHAR |  | Mapped action for the status code. |
| 10 | `CLM_ACT_CODE_C_NAME` | VARCHAR | org | Claim level action code received in a reconciliation file if value matches codes in the claim action category. |
| 11 | `CLM_ACT_CODE_DATA` | VARCHAR |  | The claim level action code received in a reconciliation file. It is set when the value received in the file does not match any category abbreviation in the claim action category. |
| 12 | `CLM_ENTITY_CODE_C_NAME` | VARCHAR | org | Claim level entity code received in a reconciliation file. Set only if the received value matches a category abbreviation in the claim entity code category. |
| 13 | `CLM_ENTITY_DATA` | VARCHAR |  | Claim level entity code received in a reconciliation file. Set only if the value does not match a category abbreviation in the claim entity code category. |
| 14 | `CLM_INFO_REQ_CODE` | VARCHAR |  | Code that defines additional information being requested. |
| 15 | `CLM_STATUS_MSG` | VARCHAR |  | Claim level status message received in a reconciliation file. |
| 16 | `ACK_CODE_C_NAME` | VARCHAR |  | Implementation acknowledgment code received in a Healthcare Acknowledgment (999) file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

