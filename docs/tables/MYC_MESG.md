# MYC_MESG

> This table contains information on messages sent to and from web-based chart system patients.

**Primary key:** `MESSAGE_ID`  
**Columns:** 56  
**Joined by:** 37 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK | The unique ID used to identify a web-based chart system message record. A new record is created each time a patient sends a message from a web-based chart system to a system user and each time a system user sends a message to a web-based chart system patient. |
| 2 | `CREATED_TIME` | DATETIME (Local) |  | The date and time the web-based chart system message record was created in local time. |
| 3 | `PARENT_MESSAGE_ID` | VARCHAR |  | The unique ID of the original message in a chain of web-based chart system messages between patients and system users. |
| 4 | `INBASKET_MSG_ID` | VARCHAR |  | The unique ID of the system message associated with the web-based chart system message. An example is when a patient sends a message to a system user. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 6 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 7 | `FROM_USER_ID` | VARCHAR |  | The unique ID of the system user who sent a web-based chart system message to a patient. |
| 8 | `FROM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `TO_USER_ID` | VARCHAR |  | The unique ID of the system user who was sent a web-based chart system message from a patient. |
| 10 | `TO_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `TOFROM_PAT_C_NAME` | VARCHAR |  | The message direction category number for the web-based chart system message. 1 corresponds to "To patient". 2 corresponds to "From patient". |
| 12 | `ORIGINAL_TO` | VARCHAR |  | If a message sent from a web-based chart system patient is re-routed from its intended destination, then the ID of the original recipient is stored in the field. Most commonly this occurs when a system user does not accept messages directly from web-based chart system patients. In this case, the message will be re-routed to a pool, but the employee ID of the system user will be stored here. The ID of the final destination is stored in MODIFIED_TO. |
| 13 | `RQSTD_PHARMACY_ID` | NUMERIC |  | The unique ID of the pharmacy selected by the patient from the drop down list when sending a Medication Renewal Request message. |
| 14 | `RQSTD_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 15 | `UPDATE_DATE` | DATETIME (Local) |  | The date and time that this web-based chart system message record was pulled into enterprise reporting. |
| 16 | `REQUEST_SUBJECT` | VARCHAR |  | This field is only used for medical advice request messages and indicates the subject selected by the patient from the drop down list. |
| 17 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 19 | `RESP_INFO` | VARCHAR |  | Some response types will include additional information, such as a phone number. If such data exists for the chosen response method, it will be stored in this field. |
| 20 | `SUBJECT` | VARCHAR |  | The subject line of the web-based chart system message. |
| 21 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 22 | `EOW_READ_STATUS_C_NAME` | VARCHAR |  | The read status category number for the web-based chart system message. |
| 23 | `BILL_ACCT_ID` | NUMERIC |  | The unique ID of the guarantor account associated with this web-based chart system message. |
| 24 | `BILL_ACCT_TYPE_C_NAME` | VARCHAR |  | The billing account type category number for the web-based chart system message. Only billing-specific customer service messages have a value specified for this column. |
| 25 | `BILL_ACCT_HAR_ID` | NUMERIC |  | The unique ID of the hospital account associated with this web-based chart system message. |
| 26 | `RELATED_MESSAGE_ID` | VARCHAR |  | The unique ID of the parent message of the original message chain. This applies only when the system is configured to allow patients to reply to messages associated with closed encounters by creating a new message chain. This item is populated for the message that starts a new chain. |
| 27 | `WPR_OWNER_WPR_ID` | VARCHAR |  | The unique ID of the web-based chart system patient who owns this message. |
| 28 | `CR_TX_CARD_ID` | NUMERIC |  | The unique ID of the credit card used for this transaction. |
| 29 | `CR_TX_MYPT_ID` | VARCHAR |  | The unique ID of the web-based chart system patient associated with this transaction. |
| 30 | `CR_TX_AMOUNT_AUTH` | NUMERIC |  | The amount authorized for this transaction. |
| 31 | `PAT_HX_QUESR_ID` | VARCHAR |  | The unique ID of the history questionnaire associated with this message. |
| 32 | `PAT_HX_QUESR_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 33 | `HX_QUESR_CONTEXT_C_NAME` | VARCHAR |  | The history questionnaire context category number for the web-based chart system message. |
| 34 | `HX_QUESR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 35 | `HX_QUESR_ENCPROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 36 | `HX_QUESR_APPT_DAT` | INTEGER |  | The appointment contact date (DAT) if the questionnaire is linked to an appointment. |
| 37 | `HX_QUESR_FILED_YN` | VARCHAR |  | Indicates whether the history questionnaire has been filed for this web-based chart system message. Y indicates that the history questionnaire has been filed. N or a null value indicates that the history questionnaire has not been filed. |
| 38 | `DELIVERY_DTTM` | DATETIME (UTC) |  | The instant that this message is scheduled for delivery to the patient. This item may not be populated. In the event that this item is not populated, then the instant the message is created is used to determine when the patient can view the message. |
| 39 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The category title of the status of the message. If not populated, then the message is active; Soft deleted is set when a message is revoked. |
| 40 | `CR_TX_TYPE_C_NAME` | VARCHAR |  | Stores the type of transaction (E-Visit or Copay). |
| 41 | `HX_QUESR_REVIEW_YN` | VARCHAR |  | Indicates whether the history questionnaire has been viewed by a provider in edit mode for this web-based chart system message. Y indicates that the history questionnaire has been viewed, N or a null value indicates that the history questionnaire has not been viewed. |
| 42 | `HX_QUESR_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the appt contact if questionnaire is linked to an appt. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 43 | `OUTREACH_RUN_ID` | NUMERIC |  | This is the campaign outreach configuration template associated with this message. |
| 44 | `RENEWAL_REQ_SRC_C_NAME` | VARCHAR |  | This item stores the request source of a medication renewal request. The default is 2-Web. |
| 45 | `REQ_PHARM_FREE_TEXT` | VARCHAR |  | If the selected pharmacy was entered by the user as free-text, then it is stored here. |
| 46 | `HX_QUESR_EDIT_MYPT_ID` | VARCHAR |  | Stores the Patient Access Account (WPR) record for the user who last made changes to an in progress history questionnaire |
| 47 | `HX_QUESR_EDIT_INST_DTTM` | DATETIME (UTC) |  | Stores the time at which changes were last made to an in progress history questionnaire |
| 48 | `REFERRAL_ID` | NUMERIC | FK→ | The unique ID of the referral this message is associated with. |
| 49 | `COMM_ID` | NUMERIC | shared | The customer service record ID corresponding to the message |
| 50 | `AUTH_REQUEST_ID` | NUMERIC | FK→ | The authorization request this message is associated with. |
| 51 | `INFO_REQ_CSN_ID` | NUMERIC |  | The Information Request this message is associated with. |
| 52 | `NON_HX_QUESR_WITH_HX_DATA_YN` | VARCHAR |  | 1 - If WMG stores history data even though the WMG type is not 22 - HISTORY Questionnaire. |
| 53 | `OUTREACH_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the outreach contact that sent the message. |
| 54 | `HX_QUESR_FILED_USER_ID` | VARCHAR |  | The ID of the user who marked the history submission as done. |
| 55 | `HX_QUESR_FILED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 56 | `HX_QUESR_FILED_LOCAL_DTTM` | DATETIME (Local) |  | The instant (in local time) that the history questionnaire submission was marked as done. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |
| `HX_QUESR_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

## Joined in — referenced by (37)

| From | Column | Confidence |
|------|--------|------------|
| [APPT_TKT_ID](APPT_TKT_ID.md) | `MESSAGE_ID` | high |
| [HX_QUESR](HX_QUESR.md) | `MESSAGE_ID` | high |
| [IB_MESSAGE_THREAD](IB_MESSAGE_THREAD.md) | `MESSAGE_ID` | high |
| [MSG_TXT](MSG_TXT.md) | `MESSAGE_ID` | high |
| [MYC_CONVO_MSGS](MYC_CONVO_MSGS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_ADL_QTNS](MYC_MESG_ADL_QTNS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_ALC_DPW](MYC_MESG_ALC_DPW.md) | `MESSAGE_ID` | high |
| [MYC_MESG_ALC_QTNS](MYC_MESG_ALC_QTNS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_ATTACH](MYC_MESG_ATTACH.md) | `MESSAGE_ID` | high |
| [MYC_MESG_CHILD](MYC_MESG_CHILD.md) | `MESSAGE_ID` | high |
| [MYC_MESG_CNCL_RSN](MYC_MESG_CNCL_RSN.md) | `MESSAGE_ID` | high |
| [MYC_MESG_DRG_QTNS](MYC_MESG_DRG_QTNS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_DRG_TYPES](MYC_MESG_DRG_TYPES.md) | `MESSAGE_ID` | high |
| [MYC_MESG_FM_TOPIC](MYC_MESG_FM_TOPIC.md) | `MESSAGE_ID` | high |
| [MYC_MESG_MED_QTNS](MYC_MESG_MED_QTNS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_ORD_ITEMS](MYC_MESG_ORD_ITEMS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_QUESR](MYC_MESG_QUESR.md) | `MESSAGE_ID` | high |
| [MYC_MESG_QUESR_ANS](MYC_MESG_QUESR_ANS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_QUESR_SRC](MYC_MESG_QUESR_SRC.md) | `MESSAGE_ID` | high |
| [MYC_MESG_RCP_STAFF](MYC_MESG_RCP_STAFF.md) | `MESSAGE_ID` | high |
| [MYC_MESG_RECIPIENTS_OUT](MYC_MESG_RECIPIENTS_OUT.md) | `MESSAGE_ID` | high |
| [MYC_MESG_RTF_TEXT](MYC_MESG_RTF_TEXT.md) | `MESSAGE_ID` | high |
| [MYC_MESG_SEX_BCP](MYC_MESG_SEX_BCP.md) | `MESSAGE_ID` | high |
| [MYC_MESG_SEX_PRTNR](MYC_MESG_SEX_PRTNR.md) | `MESSAGE_ID` | high |
| [MYC_MESG_SEX_QTNS](MYC_MESG_SEX_QTNS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_SUBQ_TYPE](MYC_MESG_SUBQ_TYPE.md) | `MESSAGE_ID` | high |
| [MYC_MESG_SURG_QTNS](MYC_MESG_SURG_QTNS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_TASK](MYC_MESG_TASK.md) | `MESSAGE_ID` | high |
| [MYC_MESG_TOB_QTNS](MYC_MESG_TOB_QTNS.md) | `MESSAGE_ID` | high |
| [MYC_MESG_TOB_TYPES](MYC_MESG_TOB_TYPES.md) | `MESSAGE_ID` | high |
| [MYC_MESG_TOPC_DATA](MYC_MESG_TOPC_DATA.md) | `MESSAGE_ID` | high |
| [MYC_MESG_TRANS_INF](MYC_MESG_TRANS_INF.md) | `MESSAGE_ID` | high |
| [MYC_MESG_VIEWERS](MYC_MESG_VIEWERS.md) | `MESSAGE_ID` | high |
| [MYC_WMG_AUDIT](MYC_WMG_AUDIT.md) | `MESSAGE_ID` | high |
| [SPEC_CHG_TRGR_VOID](SPEC_CHG_TRGR_VOID.md) | `MESSAGE_ID` | high |
| [UNIV_CHG_LN_MSG_HX](UNIV_CHG_LN_MSG_HX.md) | `MESSAGE_ID` | high |
| [WMG_REC_STATUS_HX](WMG_REC_STATUS_HX.md) | `MESSAGE_ID` | high |

