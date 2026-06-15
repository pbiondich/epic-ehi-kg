# COD_CONTACT_INFO

> The table COD_CONTACT_INFO contains information about coding records (records in the COD master file). A row in this table contains information about each individual contact for coding records. Coding records store information from Clinical Documentation Improvement (CDI) reviews. A single coding record is created for the hospital account, with each contact (or row) containing information from a separate CDI review of the account.

**Primary key:** `CONTACT_SERIAL_NUM`  
**Columns:** 37  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | shared | The unique identifier for the coding record. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `CONTACT_SERIAL_NUM` | NUMERIC | PK shared | The contact serial number (CSN) of the contact. |
| 4 | `CONTACT_NUM` | INTEGER |  | The contact number of the contact. |
| 5 | `CNCT_TYPE_C_NAME` | VARCHAR |  | The contact type of the contact. |
| 6 | `CDI_USER_ID` | VARCHAR |  | The user ID of the clinical documentation improvement (CDI) specialist who performed the CDI review. |
| 7 | `CDI_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CDI_NEXT_REVIEW_DT` | DATETIME |  | The next review date for a clinical documentation improvement (CDI) review. |
| 9 | `CDI_PX_CODE_SET_C_NAME` | VARCHAR | org | The procedure code set in a clinical documentation improvement (CDI) review. |
| 10 | `CDI_DX_CODE_SET_C_NAME` | VARCHAR | org | The diagnosis code set in a clinical documentation improvement (CDI) review. |
| 11 | `CONTACT_STAT_C_NAME` | VARCHAR | org | This item stores the current status of a contact on the coding record. |
| 12 | `CDI_REVIEW_LOC_DTTM` | DATETIME (Attached) |  | The date and time that a clinical documentation improvement (CDI) review took place, relative to the timezone of the location in which the review took place. |
| 13 | `LINKED_QUERY_ID` | NUMERIC |  | This column is reserved for future development. |
| 14 | `SOURCE_CSN_ID` | NUMERIC |  | This item contains the contact serial number from the source coding record associated with this coding contact. This item is set when a coding contact is merged from another coding record. |
| 15 | `ADMIT_DATETIME_UTC_DTTM` | DATETIME (UTC) |  | The admission date associated with the hospital account's primary encounter. |
| 16 | `DISCHARGE_DATETIME_UTC_DTTM` | DATETIME (UTC) |  | The discharge instant associated with the hospital account's primary encounter. |
| 17 | `ADMIT_CATEGORY_C_NAME` | VARCHAR | org | The admission category for the patient. |
| 18 | `TRANSFER_FROM_C_NAME` | VARCHAR | org | The transfer source of the patient. |
| 19 | `DISCH_DEST_C_NAME` | VARCHAR | org | The discharge destination for the patient. |
| 20 | `HOSP_ADMSN_TYPE_C_NAME` | VARCHAR | org | The admission type for the patient. |
| 21 | `ADMIT_SOURCE_C_NAME` | VARCHAR | org | The point of origin for the patient. |
| 22 | `DISCH_DISP_C_NAME` | VARCHAR | org | The discharge disposition of the patient. |
| 23 | `MEANS_OF_ARRV_C_NAME` | VARCHAR | org | The means of arrival for the patient. |
| 24 | `PRIMARY_HOSP_SERV_C_NAME` | VARCHAR | org | The primary service for the patient. |
| 25 | `SECONDARY_HOSP_SERV_C_NAME` | VARCHAR |  | The secondary service of the patient. |
| 26 | `ADMITTING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 27 | `ATTENDING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 28 | `REFFERING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 29 | `HEALTH_PLAN_TASK_ID` | VARCHAR |  | The task being performed when this contact was created. |
| 30 | `LATEST_DOCUMENT_CSN_ID` | NUMERIC |  | The latest DXR contact that was available for the associated encounter when this record was coded. |
| 31 | `LATEST_CLAIM_ID` | NUMERIC |  | The ID of the latest claim in the adjustment sequence available for the associated original claim when this contact was coded. If the claim had never been adjusted at the point that this contact was coded, then this will be the original claim. |
| 32 | `CDI_START_USER_ID` | VARCHAR |  | This item stores the user ID of the CDI specialist who started the CDI review. This will only be different from item 600 (CDI User) when the start user pends a review and a seperate user later finishes the review. |
| 33 | `CDI_START_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 34 | `UNLINKED_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 35 | `UNLINK_TYPE_OF_BILL` | VARCHAR |  | The type of bill that is associated with the coding session |
| 36 | `UNLINK_CRR_FORMAT_C_NAME` | VARCHAR |  | The electronic claim format (CMS or UB) to use for the associated chart review. |
| 37 | `CDI_REVIEW_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The encounter the CDI review was documented in. If the review was done in the chart (not in an encounter) this item will not be populated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CDI_REVIEW_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

