# BEREAVED_INFO

> This table contains information about your bereaved records. These include name, address, phone numbers, and associated patients. The records included in this table are Bereavement Contact (LHB) records.

**Primary key:** `RECORD_ID`  
**Columns:** 31  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the bereavement contact record. |
| 2 | `RECORD_NAME` | VARCHAR |  | The name of the bereavement contact record. |
| 3 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status, such as active or soft-deleted. |
| 4 | `BEREAVE_STATUS_C_NAME` | VARCHAR |  | The status of the bereavement contact. |
| 5 | `BEREAVEMENT_HSB_ID` | NUMERIC |  | The unique identifier for the hospice episode of care record associated with the bereaved. |
| 6 | `BEREAVEMENT_EPT_ID` | VARCHAR |  | The unique identifier for the patient record associated with the bereaved. |
| 7 | `BEREAVEMENT_CITY` | VARCHAR |  | The city of the bereavement contact's address. |
| 8 | `BEREAVEMENT_STATE_C_NAME` | VARCHAR | org | The state of the bereavement contact's address. |
| 9 | `BEREAVEMENT_ZIP` | VARCHAR |  | The zip code of the bereavement contact's address. |
| 10 | `BEREAVE_COUNTRY_C_NAME` | VARCHAR | org | The country of the bereavement contact's address. |
| 11 | `BEREAVEMENT_HPHONE` | VARCHAR |  | The home phone number for the bereavement contact. |
| 12 | `BEREAVEMENT_WPHONE` | VARCHAR |  | The work phone number for the bereavement contact. |
| 13 | `BEREAVEMENT_MPHONE` | VARCHAR |  | The mobile phone number for the bereavement contact. |
| 14 | `BEREAVED_RELATION_C_NAME` | VARCHAR | org | The relationship of the bereavement contact to the patient. |
| 15 | `BEREAVEMENT_EMAIL` | VARCHAR |  | The email address for the bereavement contact. |
| 16 | `BEREAVEMENT_CMNTS` | VARCHAR |  | Comments entered by the user to record miscellaneous information about the bereaved. |
| 17 | `SEX_C_NAME` | VARCHAR | org | The gender of the bereavement contact. |
| 18 | `BIRTH_DATE_DT` | DATETIME |  | The date of birth of the bereavement contact. |
| 19 | `PRIMARY_LANGUAGE_C_NAME` | VARCHAR | org | The primary language of the bereavement contact. |
| 20 | `RECORD_CREATION_DT` | DATETIME |  | The date the bereavement contact record was created. |
| 21 | `INSTANT_OF_UPD_DTTM` | DATETIME (Local) |  | The instant the record was last locked or unlocked. |
| 22 | `RISK_LEVEL_C_NAME` | VARCHAR |  | Risk level of the bereaved. |
| 23 | `LAST_ADDRESS_LBL_PRINT_DTTM` | DATETIME (Local) |  | The instant the bereaved address label was last printed. |
| 24 | `UNLINK_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 25 | `GENDER_C_NAME` | VARCHAR | org | The gender identity of the bereaved. |
| 26 | `COMMBRV_PAT_NAME` | VARCHAR |  | The name of the individual for whom the bereaved is grieving. This column is only populated for Community Bereavement records. In order to link to patients using non-Community Bereavement records, use the column BEREAVED_INFO.BEREAVEMENT_EPT_ID. |
| 27 | `COMMBRV_PAT_LEGAL_SEX_C_NAME` | VARCHAR |  | The legal sex of the individual for whom the bereaved is grieving. This column is only populated for Community Bereavement records. |
| 28 | `COMMBRV_PAT_BIRTH_DATE` | DATETIME |  | The date of birth of the individual for whom the bereaved is grieving. This column is only populated for Community Bereavement records. |
| 29 | `COMMBRV_PAT_DEATH_DATE` | DATETIME |  | The date of death of the individual for whom the bereaved is grieving. This column is only populated for Community Bereavement records. |
| 30 | `COMMBRV_PAT_STATUS_C_NAME` | VARCHAR | org | The status (alive, deceased, etc) of the individual for whom the bereaved is grieving. This column is only populated for Community Bereavement records. |
| 31 | `COMMBRV_PAT_GENDER_C_NAME` | VARCHAR |  | The gender identity of the individual for whom the bereaved is grieving. This column is only populated for Community Bereavement records. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

