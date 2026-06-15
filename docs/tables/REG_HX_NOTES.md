# REG_HX_NOTES

> This table contains information for tracking registration history event notes.

**Primary key:** `NOTE_ID`  
**Columns:** 37  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `REG_HX_EVENT_C_NAME` | VARCHAR |  | The Reg History event type category number for the Reg History event being tracked. |
| 3 | `REG_HX_OPEN_PAT_CSN` | NUMERIC | FK→ | The unique contact serial number for the contact of the open patient encounter at the time of the note creation. |
| 4 | `REG_HX_ENTRY_DTTM` | DATETIME (UTC) |  | The date and time when the note was created. If the date is null, the default value is 01/01/1900. If the time is null, the default value is 00:00. |
| 5 | `REG_HX_USER_ID` | VARCHAR |  | The unique ID of the user logged in when the note was generated. |
| 6 | `REG_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `REG_HX_LOGIN_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `REG_HX_SRC_EAR_ID` | NUMERIC |  | The unique ID of the account where an address change occurred in an address change event. |
| 9 | `REG_HX_SRC_CVG_ID` | NUMERIC |  | The unique ID of the coverage for which the subscriber's address changed in an address change event. |
| 10 | `REG_HX_CITY_OLD` | VARCHAR |  | The previous city for an address change event. |
| 11 | `REG_HX_STATE_OLD_C_NAME` | VARCHAR | org | The previous state for an address change event. |
| 12 | `REG_HX_ZIP_OLD` | VARCHAR |  | The previous ZIP/postal code for an address change event. |
| 13 | `REG_HX_CNTRY_OLD_C_NAME` | VARCHAR | org | The previous country for an address change event. |
| 14 | `REG_HX_CNTY_OLD_C_NAME` | VARCHAR | org | The previous county for an address change event. |
| 15 | `REG_HX_HN_OLD` | VARCHAR |  | The previous house number for an address change event. |
| 16 | `REG_HX_DSTRCT_OLD_C_NAME` | VARCHAR | org | The previous district for an address change event. |
| 17 | `CONFRM_ERR_FINIS_YN` | VARCHAR |  | Indicates whether the confirmation record that triggered a warning or error was a finish confirmation record. |
| 18 | `REG_HX_OLD_EFFFR_DT` | DATETIME |  | The old effective-from date when a coverage-level effective date was changed. If the date is null, the default value is 01/01/1900. |
| 19 | `REG_HX_NEW_EFFFR_DT` | DATETIME |  | The new effective-from date when a coverage-level effective date was changed. If the date is null, the default value is 01/01/1900. |
| 20 | `REG_HX_OLD_EFFTO_DT` | DATETIME |  | The old effective-to date when a coverage-level effective date was changed. If the date is null, the default value is 01/01/1900. |
| 21 | `REG_HX_NEW_EFFTO_DT` | DATETIME |  | The new effective-to date when a coverage-level effective date was changed. If the date is null, the default value is 01/01/1900. |
| 22 | `REG_HX_CITY_NEW` | VARCHAR |  | The new city for an address change event. |
| 23 | `REG_HX_STATE_NEW_C_NAME` | VARCHAR |  | The new state for an address change event. |
| 24 | `REG_HX_ZIP_NEW` | VARCHAR |  | The new ZIP/postal code for an address change event. |
| 25 | `REG_HX_CNTRY_NEW_C_NAME` | VARCHAR |  | The new country for an address change event. |
| 26 | `REG_HX_CNTY_NEW_C_NAME` | VARCHAR |  | The new county for an address change event. |
| 27 | `REG_HX_HN_NEW` | VARCHAR |  | The new house number for an address change event. |
| 28 | `REG_HX_DSTRCT_NEW_C_NAME` | VARCHAR |  | The new district for an address change event. |
| 29 | `REG_HX_VERF_ID` | NUMERIC |  | The unique ID of the verification record associated with the verification event for this row. This column is frequently used to link to the VERIFICATION table. |
| 30 | `REG_HX_FO_SOURCE_C_NAME` | VARCHAR |  | The source of a filing order change. |
| 31 | `REG_HX_FO_REV_ACC_C_NAME` | VARCHAR | org | The reason that a filing order change was accepted when it was reviewed. |
| 32 | `REG_HX_FO_REV_REJ_C_NAME` | VARCHAR | org | The reason that a filing order change was rejected when it was reviewed. |
| 33 | `REG_HX_FO_RV_CER_ID` | VARCHAR |  | The rule (CER) ID that an automatic filing order change was associated with. |
| 34 | `REG_HX_FO_RV_CER_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 35 | `REG_HX_FO_WQ_ID` | VARCHAR |  | The workqueue (WQF) ID that a filing order review change was associated with. |
| 36 | `REG_HX_FO_WQ_ID_WORKQUEUE_NAME` | VARCHAR |  | The name of the workqueue |
| 37 | `REG_HX_FO_REV_CMT` | VARCHAR |  | The free-text reason given by the user that a filing order change was made. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REG_HX_OPEN_PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

