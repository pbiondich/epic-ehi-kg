# DOCS_RCVD_TRANSPLANT_INFO

> Cosmos discrete data received on transplants.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `TRANSPLANT_REFERENCE_IDENT` | VARCHAR |  | This item stores the unique reference id associated with the transplant episode |
| 6 | `TRANSPLANT_SURGERY_DATE` | DATETIME |  | Transplant surgery date |
| 7 | `TRANSPLANT_REFERRAL_DATE` | DATETIME |  | Transplant episode referral date |
| 8 | `TRANSPLANT_EVALUATION_DATE` | DATETIME |  | Transplant Episode evaluation date |
| 9 | `TRANSPLANT_WAITLIST_DATE` | DATETIME |  | Transplant episode waitlisted date |
| 10 | `TRANSPLANT_SINGLE_SRC_DXO_ID` | NUMERIC |  | Source organization for transplant info with a single source. |
| 11 | `TRANSPLANT_SINGLE_SRC_DXO_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 12 | `TRANSPLANT_PHASE_C_NAME` | VARCHAR |  | Phase of the current transplant episode |
| 13 | `TRANSPLANT_PHASE_DATE` | DATETIME |  | Specifies the date that phase, status, and reason took effect for the current transplant episode |
| 14 | `TRANSPLANT_STATUS_C_NAME` | VARCHAR | org | The status of the current transplant episode |
| 15 | `TRANSPLANT_REASON_C_NAME` | VARCHAR | org | The reason corresponding to the status set in the current transplant episode |
| 16 | `TRANSPLANT_MANAGING_CENTER_C_NAME` | VARCHAR | org | The managing center corresponding to this transplant episode |
| 17 | `TRANSPLANT_EPISODE_TYPE_C_NAME` | VARCHAR |  | This item denotes whether a transplant episode corresponds to a donor or recipient |
| 18 | `TRANSPLANT_ADMISSION_IDENT` | VARCHAR |  | The admission reference ID associated with a patient's admission encounter for transplant |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

