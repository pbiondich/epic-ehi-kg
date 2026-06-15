# PRE_CLM_REV_SUBMISSIONS

> Each row in this table represents a Home Health Pre-Claim Review submission to Medicare for approval to send the final claim for full reimbursement.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 6 | `SUBMISSION_INSTANT_DTTM` | DATETIME (Local) |  | Stores the instant the Pre-Claim Review submission was recorded as sent to CMS. |
| 7 | `SUBMISSION_STATUS_C_NAME` | VARCHAR |  | The status of a Pre-Claim Review submission. |
| 8 | `SUBMISSION_UTN` | VARCHAR |  | The unique tracking number (UTN) of a Pre-Claim Review submission, as provided by CMS in response to a Pre-Claim Review submission. |
| 9 | `SUBMISSION_NOTE_ID` | VARCHAR |  | The identifier for a note that stores comments about this Pre-Claim Review submission. A unique note exists for each submission line if note data has been entered. |
| 10 | `PCR_REASON_C_NAME` | VARCHAR | org | The reason that a Pre-Claim Review submission has not been affirmed, as provided by CMS in response to a Pre-Claim Review submission. |
| 11 | `PCR_SUBMISSION_DCN` | VARCHAR |  | The document control number (DCN) of a Pre-Claim Review submission, as provided by CMS when a Pre-Claim Review submission is first submitted. |
| 12 | `PCR_BILLING_PERIOD` | INTEGER |  | The billing period number for a Pre-Claim Review submission. This is 1 (or blank) for the first account in a certification period and 2 for the second account in a certification period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

