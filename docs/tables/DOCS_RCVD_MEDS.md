# DOCS_RCVD_MEDS

> This table stores medications received from outside sources.

**Overflow family:** [DOCS_RCVD_MEDS_2](DOCS_RCVD_MEDS_2.md), [DOCS_RCVD_MEDS_3](DOCS_RCVD_MEDS_3.md)  
**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 72  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MED_REF_ID` | VARCHAR |  | This item stores the unique reference ID. |
| 6 | `MED_NAME` | VARCHAR |  | This item stores the medication name. |
| 7 | `MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 8 | `MED_DIRECTIONS` | VARCHAR |  | This item stores free text sig for the medication. |
| 9 | `MED_DOSE` | VARCHAR |  | This item stores dosage for the medication. |
| 10 | `MED_DISCRETE_DOSE` | VARCHAR |  | This item stores discrete dose for the medication. |
| 11 | `MED_ROUTE` | VARCHAR |  | This item stores route information for the medication. |
| 12 | `MED_ROUTE_ID_C_NAME` | VARCHAR | org | This item stores mapped route information for the medication. |
| 13 | `MED_QUANTITY` | VARCHAR |  | This item stores the medication quantity. |
| 14 | `MED_IS_LONG_TERM_YN` | VARCHAR |  | This item is set if the medication is long term. |
| 15 | `MED_START_DATE` | DATETIME |  | This item stores the start date of the medication. |
| 16 | `MED_END_DATE` | DATETIME |  | This item stores the end date of the medication. |
| 17 | `MED_FORM` | VARCHAR |  | This item stores the form of the medication. |
| 18 | `MED_FORM_ID_C_NAME` | VARCHAR | org | This item stores the mapped form of the medication. |
| 19 | `MED_DOSE_UNIT` | VARCHAR |  | This item stores the dose units associated with the medication. |
| 20 | `MED_DOSE_UNIT_ID_C_NAME` | VARCHAR | org | This item stores the mapped dose unit associated with the medication. |
| 21 | `MED_FREQ` | VARCHAR |  | This item stores the frequency to take this medication. |
| 22 | `MED_FREQ_ID` | VARCHAR |  | This item stores the mapped frequency to take this medication. |
| 23 | `MED_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 24 | `MED_ORIG_REFILLS` | NUMERIC |  | This item stores the original refills for the medications. |
| 25 | `MED_REFILL_REMAIN` | NUMERIC |  | This item stores the remaining refills for the medications. |
| 26 | `MED_RSN_FOR_DISC` | VARCHAR |  | This item stores the reason for discontinuation. |
| 27 | `MED_RSN_FOR_DISC_C_NAME` | VARCHAR | org | This item stores the mapped reason for discontinuation. |
| 28 | `MED_SRC_ORD_ID` | NUMERIC |  | This item stores the record ID of the source medication record. |
| 29 | `MED_TYPE_OF_CHNG_C_NAME` | VARCHAR |  | This item stores the type of change associated with the medication. |
| 30 | `MED_SRC_DXR_CSN` | NUMERIC |  | This item will store the contact serial number (CSN) of the Received Document record that owns the instance of this medication. |
| 31 | `MED_DUP_GRP_ID` | VARCHAR |  | This item will store a duplicate grouping identifier. |
| 32 | `MED_DUP_OVRD_ORD_ID` | NUMERIC |  | This item stores the record identifier of the local medication that this external medication should be grouped with. |
| 33 | `MED_STATUS_C_NAME` | VARCHAR |  | This item stores the status of the medications. |
| 34 | `MED_REQ_RES_COMMENT` | VARCHAR |  | The response comments received with an incoming electronic prescription message. |
| 35 | `MED_PRIM_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 36 | `MED_SEC_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 37 | `MED_LAST_UPD_DTTM` | DATETIME (UTC) |  | This item stores the date and time when the medication was last updated by the external system. |
| 38 | `MED_PT_SRC_APP_C_NAME` | VARCHAR | org | If this medication is a patient-entered medication (i.e. Received Documents type = 25), this item stores the application which was used to edit the medication for the contact (e.g. MyChart or Welcome). If blank, this is assumed to be MyChart. |
| 39 | `MED_EARLIESTFILL_DT` | DATETIME |  | The first or earliest date on which the medication in the medication prescribed segment of the external e-prescription can be filled. |
| 40 | `MED_IS_MIXTURE_YN` | VARCHAR |  | This column indicates whether the medication in the medication prescribed segment of the external e-prescription, received through the incoming e-prescribing interface, is a mixture. |
| 41 | `MED_IS_SUPPLY_YN` | VARCHAR |  | This column indicates whether the medication in the medication prescribed segment of the external e-prescription, received through the incoming e-prescribing interface, is a medication supply (for example, a test strip). |
| 42 | `MED_DEA_CODE_C_NAME` | VARCHAR | org | The DEA schedule for the medication in the medication prescribed segment of the external e-prescription received through the incoming e-prescribing interface. |
| 43 | `MED_DT_START_NF_C_NAME` | VARCHAR |  | This item stores the nullFlavor value from the effectiveTime low node in a received CDA document. |
| 44 | `MED_DT_END_NF_C_NAME` | VARCHAR |  | This item stores the nullFlavor value from the effectiveTime high node in a received CDA document. |
| 45 | `MED_STATE_C_NAME` | VARCHAR |  | This item stores the value from the statusCode node in a received CDA document. This item itself is not the status of the medication. |
| 46 | `MED_ADMIN_AMT` | VARCHAR |  | The admin amount for a unit dose of the medication associated with the medication prescribed segment of the external e-prescription. |
| 47 | `MED_ADMN_AMT_UNIT_C_NAME` | VARCHAR |  | The unit of measurement for the admin amount of the medication dose in the medication prescribed segment of the external e-prescription. |
| 48 | `MED_DOSE_PAR_VALUE` | VARCHAR |  | The value of the patient's clinical measurement used for dosing a unit dose of the medication in the medication prescribed segment of the external e-prescription. For weight-based dosing, the value is stored in kilograms and for BSA-based dosing, the value is stored in square meters (m2). |
| 49 | `MED_DOSE_TYPE_C_NAME` | VARCHAR | org | The dosing type, based on the patient's clinical measurement, used for determining the unit dose amount of the medication in the medication prescribed segment of the external e-prescription |
| 50 | `MED_DURATION` | VARCHAR |  | The duration of therapy for the medication associated with the medication prescribed segment of the external e-prescription. |
| 51 | `MED_DURATION_UNIT_C_NAME` | VARCHAR |  | The unit for the duration of therapy for the medication associated with the medication prescribed segment of the external e-prescription. |
| 52 | `MED_TTL_DOSE` | VARCHAR |  | The total amount for a unit dose of a medication that uses a patient's clinical measurement (for example, weight or BSA) for dosing in the medication prescribed segment of the external e-prescription. |
| 53 | `MED_TTL_DOSE_UNT_C_NAME` | VARCHAR |  | The unit for the total amount for a unit dose of a medication that uses a patient's clinical measurement (for example, weight or BSA) for dosing in the medication prescribed segment of the external e-prescription. |
| 54 | `MED_HIST_STATUS_C_NAME` | VARCHAR |  | The item indicates whether the medication is current, historical, or a more specific subset of historical. |
| 55 | `MED_HIST_DATE` | DATETIME |  | This item stores the date that the historical status for this medication is valid through. After this date, the historical status needs to be rechecked. |
| 56 | `MED_SRC_WPR_ID` | VARCHAR |  | Stores the ID of the MyChart user who edited the medication for the contact. |
| 57 | `MED_START_UTC_DTTM` | DATETIME (UTC) |  | Start instant for this medication |
| 58 | `MED_TYPE_C_NAME` | VARCHAR |  | Type of medication (Inpatient, Outpatient, etc) |
| 59 | `AUTH_PROV` | VARCHAR |  | Authorizing provider name |
| 60 | `MED_DISP_NAM` | VARCHAR |  | Medication display name |
| 61 | `MED_SUM` | VARCHAR |  | Medication summary |
| 62 | `SRC_ORD_REF_ID` | VARCHAR |  | Source order reference ID |
| 63 | `REC_ACT_C_NAME` | VARCHAR |  | Reconciliation action |
| 64 | `MED_END_UTC_DTTM` | DATETIME (UTC) |  | Contains the instant that this medication ends. |
| 65 | `MED_REM_DUR` | INTEGER |  | Contains the remaining duration for this medication |
| 66 | `MED_REM_DUR_UNIT_C_NAME` | VARCHAR |  | Contains the unit of the remaining duration for this medication |
| 67 | `NEXT_ADM_INST_DTTM` | DATETIME (UTC) |  | Contains the instant of the next scheduled administration (at the time of sending). |
| 68 | `MED_EVENT_ID` | VARCHAR |  | Reference ID of the encounter this medication was ordered in |
| 69 | `MED_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the contact serial number of the encounter that the medication was added on. |
| 70 | `MED_ORDER_ID` | NUMERIC |  | Order ID that was created from this document |
| 71 | `PRN_COMMENT` | VARCHAR |  | This item stores the PRN comment for a PRN medication. |
| 72 | `MED_IN_PACKAGE_YN` | VARCHAR |  | if the medication is included in the multidose package |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

