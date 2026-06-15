# DENTAL_ORTHODONTICS

> Table for storing Orthodontics Episode items such as Treatment Scope, Treatment Start Date, etc.

**Primary key:** `SUMMARY_BLOCK_ID`, `CONTACT_DATE_REAL`  
**Columns:** 22  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `ORTHO_BANDING_DATE` | DATETIME |  | Date on which the brackets or bands were placed on patient's teeth. |
| 5 | `ORTHO_END_DATE` | DATETIME |  | Date on which the last phase of an orthodontic treatment ends. |
| 6 | `ORTHO_ESTIMATED_LENGTH` | INTEGER |  | Estimated number of months an orthodontic treatment would last. |
| 7 | `ORTHO_TX_SCOPE_C_NAME` | VARCHAR | org | The current scope of orthodontic treatment. |
| 8 | `ORTHO_EPSD_STATUS_C_NAME` | VARCHAR | org | Status of the episode in terms of "Ongoing", "Pending", or "Discontinued". |
| 9 | `ORTHO_EPSD_STATUS_REASON_C_NAME` | VARCHAR | org | Reason why an orthodontics episode is pending or discontinued. |
| 10 | `ORTHO_MODIFIED_INST_DTTM` | DATETIME (UTC) |  | History item that tracks every instant an orthodontic episode has been modified. |
| 11 | `ORTHO_MODIFIED_USER_ID` | VARCHAR |  | Stores the user that modified orthodontics data for this history line. |
| 12 | `ORTHO_MODIFIED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `ORTHO_MODIFIED_CSN` | NUMERIC |  | Stores the contact CSN where data was modified for this history line. |
| 14 | `ORTHO_STATUS_COMMENT` | VARCHAR |  | Comment on why an orthodontics episode status is paused or discontinued. |
| 15 | `ORTHO_TX_STATUS_C_NAME` | VARCHAR |  | This is the status of the orthodontic treatment. |
| 16 | `ORTHO_DENTITION_C_NAME` | VARCHAR |  | This is the treatment dentition for the orthodontics episode. |
| 17 | `OWNER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `TREAT_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 19 | `ORTHO_READY_TX_YN` | VARCHAR |  | This item stores whether the patient is ready for treatment in this episode. The item is documented as part of the patient's comprehensive exam. If left blank, then a clinical decision has not yet been made. |
| 20 | `ORTHO_TX_PHASE` | INTEGER |  | This is the treatment phase for the orthodontic treatment. |
| 21 | `ORTHO_COMP_SCORE_C_NAME` | VARCHAR |  | This is the compliance score for an orthodontic episode. |
| 22 | `HYG_ORTHO_COMP_SCORE_C_NAME` | VARCHAR |  | This is the hygiene score for an orthodontic episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

