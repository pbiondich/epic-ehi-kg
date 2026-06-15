# DOCS_RCVD_TREAT_RESTR

> This table contains treatment restrictions for the received document.

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
| 5 | `TRT_REF_ID` | VARCHAR |  | A unique reference identifier for a specific treatment restriction |
| 6 | `CODE_STATUS_C_NAME` | VARCHAR | org | The code status category ID for the received document. |
| 7 | `CODE_STS_DISP_NAME` | VARCHAR |  | The code status display name |
| 8 | `TREATMENT_C_NAME` | VARCHAR | org | The treatment category ID for the received document |
| 9 | `TREAT_PERMITTED_C_NAME` | VARCHAR | org | The treatment permitted category ID for the received document. |
| 10 | `TREAT_LIMITS_HNO_ID` | VARCHAR |  | The unique ID of the note record for the limitations or circumstances that apply to the treatment restriction |
| 11 | `TREAT_START_DATE` | DATETIME |  | The start date of the treatment restriction |
| 12 | `TREAT_END_DATE` | DATETIME |  | The end date of the treatment restriction |
| 13 | `TREAT_EXPLANATION_HNO_ID` | VARCHAR |  | The unique ID of the note record for additional free-text notes on the treatment restriction |
| 14 | `TREAT_RESTR_CHKSUM` | VARCHAR |  | Stores the checksum of the treatment restriction |
| 15 | `TREAT_RESTR_SRC_CSN` | NUMERIC |  | Stores the CSN of the source DXR that has the treatment restriction information |
| 16 | `TREAT_LAST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the instant we consider the date this treatment restriction was last changed |
| 17 | `TREATMENT_DISP_NAME` | VARCHAR |  | The display name of the code for the medical treatment the treatment restriction relates to |
| 18 | `TRT_CODE_STATUS_GRP_IDENT` | VARCHAR |  | Identifier of the group that this Treatment Restriction/Code Status belongs to |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

