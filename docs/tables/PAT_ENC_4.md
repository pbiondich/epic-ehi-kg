# PAT_ENC_4

> This table supplements the PAT_ENC, PAT_ENC_2, and PAT_ENC_3 tables. It contains additional information related to patient encounters or appointments.

**Overflow of:** [PAT_ENC](PAT_ENC.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 58  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `FAMILY_SIZE` | INTEGER |  | The number of members in the patient's family. |
| 3 | `VISIT_NUMBER` | VARCHAR |  | The visit number for the given contact. |
| 4 | `PAT_CNCT_IND_C_NAME` | VARCHAR | org | The patient contact indicator category number for the patient encounter. |
| 5 | `DENTAL_STUDENT_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `LOC_VISIT_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `COPAY_NOT_COVERED_C_NAME` | VARCHAR | org | The copay not covered category number for the patient encounter. |
| 8 | `COPAY_COLL_FLAG_YN` | VARCHAR |  | The copay collected flag that indicates whether a copay was collected from the patient encounter. |
| 9 | `COPAY_COLL_PERSON` | VARCHAR |  | The unique ID number of the person who collected the patient's copay for the encounter. |
| 10 | `COPAY_WAIVE_RSN_C_NAME` | VARCHAR | org | The copay waive reason category number for the patient encounter. |
| 11 | `COPAY_MIN_VALUE` | NUMERIC |  | The value of the minimum copay. |
| 12 | `COPAY_RECEIPT_NUM` | VARCHAR |  | The receipt number of the copay collected. |
| 13 | `BEN_ADJ_COINS_AMT` | NUMERIC |  | The adjudicated coinsurance amount for the visit calculated by the benefits engine. |
| 14 | `BEN_ADJ_DEDUCT_AMT` | NUMERIC |  | The portion of the self-pay amount applied to the deductible for the visit. |
| 15 | `PAT_HOMELESS_YN` | VARCHAR |  | Indicates if a patient is homeless. |
| 16 | `PAT_HOMELESS_TYP_C_NAME` | VARCHAR | org | Characterizes the patients homelessness (for example chronic or sporadic) |
| 17 | `PERCENTAGE_OF_FPL` | NUMERIC |  | Indicates where the patient falls on the federal poverty level as a percentage. |
| 18 | `MSG_RECEIVED_DTTM` | DATETIME (Local) |  | The date and time the encounter creation In Basket message was received. |
| 19 | `TOBACCO_USE_VRFY_YN` | VARCHAR |  | This column indicates whether the patient's tobacco usage has been verified. A Y indicates the usage was verified. An N or null indicates the tobacco usage was not verified. It extracts a virtual item, which is calculated using EPT-19202. |
| 20 | `CR_TX_TYPE_C_NAME` | VARCHAR |  | The transaction type category number for the encounter(E-Visit or Copay). |
| 21 | `ORIG_ENC_CSN` | NUMERIC |  | Holds the CSN of the encounter this Remote Consult encounter is responding to. |
| 22 | `PHYS_BP_COMMENTS` | VARCHAR |  | This column contains the comments entered for the last recorded blood pressure for this visit. |
| 23 | `PHYS_TEMP_COMMENTS` | VARCHAR |  | This column contains the comments entered for the last recorded temperature for this visit. |
| 24 | `PHYS_TEMPSRC_COMNTS` | VARCHAR |  | This column contains the comments entered for the last recorded temperature source for this visit. |
| 25 | `PHYS_PULSE_COMMENTS` | VARCHAR |  | This column contains the comments entered for the last recorded pulse for this visit. |
| 26 | `PHYS_WEIGHT_COMNTS` | VARCHAR |  | This column contains the comments entered for the last recorded weight for this visit. |
| 27 | `PHYS_HEIGHT_COMNTS` | VARCHAR |  | This column contains the comments entered for the last recorded height for this visit. |
| 28 | `PHYS_RESP_COMMENTS` | VARCHAR |  | This column contains the comments entered for the last recorded respirations for this visit. |
| 29 | `PHYS_SPO2_COMMENTS` | VARCHAR |  | This column contains the comments entered for the last recorded oxygen saturation level (SpO2) for this visit. |
| 30 | `PHYS_PF_COMMENTS` | VARCHAR |  | This column contains the comments entered for the last recorded peak flow for this visit. |
| 31 | `INTERPRT_ASGN_CMT` | VARCHAR |  | Comments regarding the interpreter assigned to the patient's contact. |
| 32 | `PAT_HOUSING_STAT_C_NAME` | VARCHAR | org | This item stores the patient's current housing status. This is a category list item that may contain values such as Stable/Permanent, Temporary, Unstable, or Unknown. |
| 33 | `BCRA_AGE` | INTEGER |  | The patient's age at the time of the risk assessment. |
| 34 | `BCRA_MENARCHE_AGE_C_NAME` | VARCHAR |  | The patient's risk factor category number for the Age at Menarche breast cancer risk factor. |
| 35 | `BCRA_FST_LIVBIRTH_C_NAME` | VARCHAR |  | The patient's risk factor category number for the Age at First Live Birth breast cancer risk factor. |
| 36 | `BCRA_FST_DEG_REL_C_NAME` | VARCHAR |  | The patient's risk factor category number for the Number of Affected First Degree Relatives breast cancer risk factor. Only first degree relatives are considered. |
| 37 | `BCRA_NUM_BIOPSY_C_NAME` | VARCHAR |  | The patient's risk factor category number for the Number of Breast Biopsies breast cancer risk factor. |
| 38 | `BCRA_ATYP_HYPLSA_C_NAME` | VARCHAR |  | The patient's risk factor category number for the Presence of Atypical Hyperplasia in Breast Biopsies breast cancer risk factor. |
| 39 | `BCRA_RACE_C_NAME` | VARCHAR |  | The patient's risk factor category number for the Race breast cancer risk factor. |
| 40 | `LB_ENC_START_DT` | DATETIME |  | This identifies the start date of a Lab Requisition encounter. |
| 41 | `LB_ENC_END_DT` | DATETIME |  | This identifies the end date of a Lab Requisition encounter. |
| 42 | `WAITING_LIST_ID` | NUMERIC |  | The unique ID of the Waiting List record associated with this encounter. This column can be used to link to the WAITING_LIST_INFO table. |
| 43 | `SUBMITTER_ID` | NUMERIC |  | The submitting organization that the results for the lab orders on this encounter should be sent to. |
| 44 | `SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 45 | `BILL_TO_SUBMITTER_C_NAME` | VARCHAR |  | Flag indicating whether the submitter should be billed for any lab procedures performed. |
| 46 | `SUBMITTER_ACCT_ID` | NUMERIC |  | The submitter account to be used when billing laboratory procedures. |
| 47 | `LB_BLNG_ENC_SRVC_DT` | DATETIME |  | This identifies the service date of the Billing encounter used for Lab Billing. The date is in the time zone of the lab department that created the encounter. |
| 48 | `ECHKIN_STATUS_C_NAME` | VARCHAR |  | The status of the eCheck-In for this appointment. |
| 49 | `PB_VISIT_HAR_ID` | NUMERIC |  | The hospital account record used by the Professional Billing system for a given contact. |
| 50 | `TECHNICAL_REFERRAL_ID` | NUMERIC |  | The MassHealth technical referral associated with the encounter. |
| 51 | `CR_CLIENT_REF_IDNT` | VARCHAR |  | Used to store the client ID returned by the copay reduction web service |
| 52 | `CR_BENEFIT_REF_IDNT` | VARCHAR |  | The benefit reference ID number of the patient for the current encounter. |
| 53 | `CR_MESSAGE_ENGLISH` | VARCHAR |  | The copay message returned by the web service in English. |
| 54 | `CR_MESSAGE_SPANISH` | VARCHAR |  | The copay message returned by the web service in Spanish. |
| 55 | `CR_QUERY_SENT_UTC_DTTM` | DATETIME (UTC) |  | Instant the copay reduction web service query was sent to the server |
| 56 | `CR_RESP_RECVD_UTC_DTTM` | DATETIME (UTC) |  | Specifies the instant when the response to the copay reduction web service query was received |
| 57 | `CR_QUERY_ERROR` | VARCHAR |  | Specifies the error received in the response to the query sent out to get the copay reduction for the current patient encounter. |
| 58 | `COPAY_REDUCTION_AMT` | NUMERIC |  | The amount by which the copay should be reduced for the current visit |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PAT_ENC](PAT_ENC.md).

