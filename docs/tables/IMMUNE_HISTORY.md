# IMMUNE_HISTORY

> The IMMUNE_HISTORY table contains the history data for immunizations ordered through the clinical system. It may also contain information on immunizations as reported by the patient, but not ordered/administered via clinical system. This table contains the history of changes made to the information that is found in the IMMUNE table. Fields in this table are no-add related group items in the LPL database.

**Primary key:** `IMMUNE_ID`, `LINE`  
**Columns:** 44  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMMUNE_ID` | NUMERIC | PK FK→ | The unique ID of the immunization record in your system production system. |
| 2 | `LINE` | INTEGER | PK | The Line Count for the line in the table which in combination with the IMMUNE_ID forms the primary key for this table. |
| 3 | `IMM_TYPE_HIST_ID` | NUMERIC |  | Stores the unique ID of the immunizations (LIM) master file which is associated with this immunization record. Corresponds to the type of immunization given to this patient. |
| 4 | `IMM_TYPE_HIST_ID_NAME` | VARCHAR |  | The name of the immunization. |
| 5 | `IMM_HX_PRODUCT` | VARCHAR |  | Stores the product information associated with this immunization. Products are usually related to the lot number. |
| 6 | `IMM_HX_NDC_NUM_ID` | VARCHAR |  | The unique ID of the Medication National Drug Codes (NDC) master file that is associated with this immunization and stores the NDC numbers associated with the administration of this immunization. |
| 7 | `IMM_HX_NDC_NUM_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 8 | `IMMNZTN_HX_DATE` | DATETIME |  | The date when this immunization was administered. |
| 9 | `IMM_HX_TIME` | DATETIME (Local) |  | The time when this immunization was administered. |
| 10 | `IMMNZTN_HX_DOSE` | VARCHAR |  | The dosage information for this immunization administered. |
| 11 | `IMMNZTN_HX_ROUTE_C_NAME` | VARCHAR | org | The category number for the route of the immunization, such as oral, intramuscular, or intradermal. |
| 12 | `IMMNZTN_HX_SITE_C_NAME` | VARCHAR | org | The location of the injection, if appropriate. |
| 13 | `IMMNZTN_HX_MFG_C_NAME` | VARCHAR | org | The category number for the manufacturer of this vaccine. |
| 14 | `IMMNZTN_HX_LOT` | VARCHAR |  | The LOT number for the immunization administered. |
| 15 | `IMM_HX_NEXT_DUE_DT` | DATETIME |  | The date on which the administered immunization is due next. , if in a series. This is manually established by the user, and not automatically calculated. |
| 16 | `IMM_HX_EXP_DATE` | DATETIME |  | The date on which the immunization administered expires. |
| 17 | `IMMNZTN_HX_GIVEN_ID` | VARCHAR |  | The unique ID of the user in the EMP master file that is listed in the clinical system as actually administering the immunization to the patient. |
| 18 | `IMMNZTN_HX_GIVEN_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `IMMNZTN_HX_EXT_AD_C_NAME` | VARCHAR | org | The category number for the source of verification of external administration of immunization. |
| 20 | `IMM_HX_ANSWER_ID` | VARCHAR |  | The unique ID in the questionnaire answers (HQA) master file that is associated with the immunization administered. |
| 21 | `IMMNZTN_HX_VIS_DATE` | VARCHAR |  | The free text date field associated with the immunization where VIS (Vaccine Information Statements) date is stored. |
| 22 | `IMMNZTN_HX_DEFER_C_NAME` | VARCHAR | org | The category number for the reason for deferring the immunization, e.g. patient refused, contraindication, etc. |
| 23 | `IMMNZTN_HX_COMMENT` | VARCHAR |  | The free text comments associated with the immunization administered. |
| 24 | `IMMNZTN_HX_ENTRY_ID` | VARCHAR |  | The unique ID of the user in the EMP masterfile associated with the person who entered the immunization administration information into the clinical system. |
| 25 | `IMMNZTN_HX_ENTRY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 26 | `PHYSICAL_SITE_HX` | VARCHAR |  | The physical site information for the immunization administered such as a specific hospital. |
| 27 | `IMM_HX_HIST_ADMI_YN` | VARCHAR |  | Indicates whether or not an immunization is historical or not. |
| 28 | `IMMNZTN_HX_ENT_DATE` | DATETIME |  | The date on which the immunization was entered into the system. |
| 29 | `IMMNZTN_HX_STATUS_C_NAME` | VARCHAR |  | The category number for the immunization status. Examples are "Given" if the immunization has been administered, "Deleted" if the immunization has been deleted from the administration history, "Incomplete" if the item has been ordered but not administered and a status of "Deferred" if the immunization has been deferred. |
| 30 | `IMM_HX_MAR_ADMIN_LI` | NUMERIC |  | The immunization history MAR administration line. |
| 31 | `IMM_CHRG_REC_HX_ID` | VARCHAR |  | The unique ID in the Universal Charge Line (UCL) master file that is associated with the immunization administered. |
| 32 | `IMMNZTN_HX_ENC_CSN` | NUMERIC | FK→ | This column stores the history information of immunization CSN whenever an edit was made on the Immunization. |
| 33 | `IMMNZTN_HX_DOSE_AMT` | NUMERIC |  | The history of dosage amount for the immunization administered. |
| 34 | `IMMNZTN_HX_DOSE_UNIT_C_NAME` | VARCHAR | org | The history of dosage unit for the immunization administered. |
| 35 | `IMM_HX_DUALSIGN_ID` | VARCHAR |  | History of the users who performed the second user verification on the immunization |
| 36 | `IMM_HX_DUALSIGN_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 37 | `IMM_HX_DUALSIGNINST_DTTM` | DATETIME (Local) |  | History of instant at which the immunization was verified by the second user. |
| 38 | `IMM_DEL_REASON_HX_C_NAME` | VARCHAR | org | Historic reason for immunization deletion. |
| 39 | `IMM_HX_SCAN_BARCODE` | VARCHAR |  | The history of raw data captured during immunization barcode scanning. |
| 40 | `IMMZTN_HX_ENTRY_DTTM` | DATETIME (Local) |  | Contains the date and time that the data in the row was entered. If the exact time is not known, a date may be contained in IMMNZTN_HX_ENT_DATE instead. |
| 41 | `IMM_HX_PRODUCT_C_NAME` | VARCHAR | org | The brand name associated with the vaccination administration in previous edits to the record, stored as a category value from a defined set of products. Historical version of IMM PRODUCT - CATEGORY (I LPL 4007). |
| 42 | `IMM_HX_DEFER_DUR_C_NAME` | VARCHAR | org | Each category value represents a different time scale of deferral for a vaccine administration deferral (e.g. "brief", "permanent", etc...) that was associated with the vaccine deferral at the time of a previous edit to the record. This item does NOT store the specific length of time the vaccine was deferred. This is the historical version of IMM DEFERRAL DURATION (I LPL 4077). |
| 43 | `IMM_HX_MAR_AD_LK_ID` | VARCHAR |  | Link to the INP record that may hold the administrations data - Historical. |
| 44 | `IMM_HX_LOT_NUM_ID_LOT_NUM` | VARCHAR |  | The lot number on the vial for a given medication or immunization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `IMMNZTN_HX_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `IMMUNE_ID` | [IMMUNE](IMMUNE.md) | sole_pk | high |

