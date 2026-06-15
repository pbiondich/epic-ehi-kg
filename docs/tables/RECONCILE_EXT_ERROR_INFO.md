# RECONCILE_EXT_ERROR_INFO

> This table contains external errors received from a trading partner when doing encounter reporting.

**Primary key:** `CLAIM_RECON_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_RECON_ID` | VARCHAR | PK | The unique identifier (.1 item) for the claim status update record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SVC_LINE_NUMBER` | VARCHAR |  | The service line number that the external error is related to. If the error applies to the entire claim this is not set. |
| 6 | `EXTERNAL_ERROR_CODE_C_NAME` | VARCHAR | org | The external error code category ID for the external error received from a trading partner. |
| 7 | `EXTERNAL_ERROR_DESCRIPTION` | VARCHAR |  | The trading partner's description of the error that was received back. |
| 8 | `DUPLICATE_EPIC_ICN` | VARCHAR |  | Identifies a prior duplicate claim submission. This identifier is the Epic submitted control number from the original 837 submission which a trading partner has identified this new claim submission as a duplicate of. |
| 9 | `DUPLICATE_EPIC_CLAIM_ID` | NUMERIC |  | Identifies a prior duplicate claim submission. This is the unique identifier (.1 item) for the claim in Epic this is a duplicate of. |
| 10 | `DUPLICATE_PAYER_REF_NUM` | VARCHAR |  | Identifies a prior duplicate claim submission. This is the reference number in the trading partner's system assigned to the prior submission this claim is a duplicate of. |
| 11 | `DUPLICATE_SVC_LINE_NUMBER` | VARCHAR |  | Identifies which service line of a prior duplicate submission this line was a duplicate of. |
| 12 | `IS_LINE_REJ_YN` | VARCHAR |  | A flag that indicates whether or not this service line was rejected. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

