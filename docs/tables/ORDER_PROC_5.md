# ORDER_PROC_5

> The ORDER_PROC_5 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same basic structure as ORDER_PROC, but was created as a fifth table to prevent ORDER_PROC_4 from getting any larger.

**Overflow of:** [ORDER_PROC](ORDER_PROC.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 71  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `FUTURE_RELATIVE_EXPECTED_DT_C_NAME` | VARCHAR | org | Holds a category value for the expected completion date. This may be subtly different from the expected date (ORDER_PROC.FUT_EXPECT_COMP_DT) for things like "in 3 months", which could be Start Date+90 days (S+90), Start date+91 days (S+91), or Start date + 92 days (S+92) depending on the current date. |
| 3 | `FUTURE_EXPECTED_DATE_COMMENT_C_NAME` | VARCHAR |  | Holds a category value for the comment part of expected date. This will include categories based on scheduling comments like "Before Surgery", "After Consult", etc. |
| 4 | `FUTURE_EXPECTED_DATE_DETAILS` | VARCHAR |  | This item holds the free-text details entered if the Once (Future) expected date comment (FUTURE_EXPECTED_DATE_COMMENT_C) is "Other (Specify)." |
| 5 | `MODIFY_TRACK_C_NAME` | VARCHAR |  | Flag used to denote if the order was modified or reordered. |
| 6 | `INCOMPLETE_CHILD_ORDERS` | INTEGER |  | Store the number of child orders which have not yet reached completed/canceled status. meaning they are either not yet released or are currently active. |
| 7 | `ORDER_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant when the order was created in UTC. |
| 8 | `MINUTES_BTWN_SCHED_AND_COLL` | INTEGER |  | The number of minutes between the scheduled and collected instants for a lab. Negative values indicate early collection. |
| 9 | `APPT_WINDOW_START_TIME` | DATETIME (Local) |  | This is the start of the appointment window for the preferred appointment window. |
| 10 | `OVERREAD_SRC_ORD_ID` | NUMERIC |  | Stores the order record ID that is marked for imaging overread. |
| 11 | `APPT_WINDOW_END_TIME` | DATETIME (Local) |  | This is the end of the appointment window for the preferred appointment window. |
| 12 | `PROC_ESTIMATE_ID` | NUMERIC |  | A link to a patient estimate record that contains patient cost estimate information for procedure orders. |
| 13 | `SHOULD_GENERATE_PAT_EST_YN` | VARCHAR |  | A flag used for pended orders that indicates that the order should generate a patient estimate record when it is fully signed. |
| 14 | `FINANCIAL_CLEARANCE_STATUS_C_NAME` | VARCHAR | org | Records the financial clearance status of an order |
| 15 | `FINANCIAL_CLEARANCE_UTC_DTTM` | DATETIME (UTC) |  | Records the UTC instant an order was financially cleared |
| 16 | `FNDAVTR_DOC_INFO_ID` | VARCHAR |  | Stores the Document ID of the image for the findings avatar |
| 17 | `IMG_PUBLIC_RSLT_DTTM` | DATETIME (Local) |  | The instant in local time at which the imaging result was made public, as defined by the order's study status (e.g. physician finalized the exam) as configured by the imaging analyst team (I RDF 192). |
| 18 | `ORDER_RECEIVED_DTTM` | DATETIME (Local) |  | The date and time the order was received. |
| 19 | `ACTV_EXCLUDE_FROM_CDS_REASON_C_NAME` | VARCHAR |  | The Exclude From Decision Support reason for the order. It will be either 1 - Unsuccessful Attempt represents an order that was not successfully completed. or 2 - Documented on Wrong Patient represents the order's result information was documented on the incorrect patient. |
| 20 | `ACTV_EXCLUDE_FROM_CDS_UTC_DTTM` | DATETIME (UTC) |  | The instance in UTC when the "Exclude From Decision Support" was updated on the order record. |
| 21 | `ACTV_EXCLUDE_FROM_CDS_DTTM` | DATETIME (Local) |  | The instance when the "Exclude From Decision Support" was updated on the order record. |
| 22 | `LEAVE_TYPE_C_NAME` | VARCHAR | org | The type of medical leave being ordered. |
| 23 | `LEAVE_START_DATE` | DATETIME |  | Start date of the medical leave. |
| 24 | `LEAVE_END_DATE` | DATETIME |  | End date of the medical leave. |
| 25 | `LEAVE_DURATION` | INTEGER |  | Duration of the medical leave in days. |
| 26 | `LEAVE_LIGHTDUTY_YN` | VARCHAR |  | Whether the medical leave also has a light duty period. |
| 27 | `LEAVE_LIGHTDUTY_START_DATE` | DATETIME |  | Start date of the light duty period. |
| 28 | `LEAVE_LIGHTDUTY_END_DATE` | DATETIME |  | End date of the light duty period. |
| 29 | `LEAVE_LIGHTDUTY_DURATION` | INTEGER |  | Duration of the light duty period in days. |
| 30 | `LEAVE_EXCUSED_ACTIVITIES_YN` | VARCHAR |  | Whether the patient should be excused from doing specific activities during the leave. |
| 31 | `LEAVE_EXCUSED_START_DATE` | DATETIME |  | Start date of the excused activities period. |
| 32 | `LEAVE_EXCUSED_END_DATE` | DATETIME |  | End date of the excuse period. |
| 33 | `LEAVE_EXCUSED_DURATION` | INTEGER |  | Duration of the excuse period in days. |
| 34 | `LEAVE_EXCUSED_COMMENTS` | VARCHAR |  | Comments about the excused activities for the excuse period. |
| 35 | `DELIVERY_REQUEST_ORDER_ID` | NUMERIC |  | The order ID of the blood component order this order record is requesting a delivery from. |
| 36 | `DELIVERY_REQUEST_AMOUNT` | INTEGER |  | The number of units being requested from the blood component order record. |
| 37 | `ORIGINATING_ORD_ID` | NUMERIC |  | This column contains the originating order ID. It is related conceptually to ORDER_PROC_2.ORIGINAL_ORDER_ID, but rather than pointing back to the previous order ID at the same level in the order tree hierarchy, this column will point back to the initial order created by the ordering end user. Use this column to find out information about the initial order, or to determine if an order went through a change procedure workflow which generated new order records. |
| 38 | `PROC_CHANGED_YN` | VARCHAR |  | This column determines whether the orderable procedure was changed as part of a change procedure workflow that generated new order records. The column will be set to 1 - Yes if a new procedure was selected during the change procedure workflow step. If the procedure was kept and other details were changed, this column will be populated with 0 - No. If the order did not go through a change procedure workflow which generated new order records, this column will be null. |
| 39 | `ACTIVE_PROC_TYPE_C_NAME` | VARCHAR |  | This item holds the category type of the active procedure order. Only active procedure type orders will be contained in this item. Medications are excluded. The categories separate order type in parent/child/Now and IP/OP order type. |
| 40 | `DELIVERY_REQUEST_UNIT_C_NAME` | VARCHAR | org | The unit category of the blood component order record being requested. |
| 41 | `BILL_AREA_ID` | NUMERIC | FK→ | The bill area this order is associated with. |
| 42 | `BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 43 | `ADT_ORDER_TYPE_C_NAME` | VARCHAR |  | The ADT (admission, discharge, transfer) order type category ID for the order, indicating what type of patient movement this order is intended for. |
| 44 | `BI_PRELIM_OUTCOME_C_NAME` | VARCHAR |  | Stores preliminary FP/FN/TP/FN/etc info for a breast imaging study. May not contain the most current data until the MQSA report has been run. |
| 45 | `RAD_EXAM_END_UTC_DTTM` | DATETIME (UTC) |  | The date and time an order's exam is ended in the Universal Time Coordinated (UTC) format. |
| 46 | `PAT_AGE_AT_EXAM` | INTEGER |  | The age of the patient (in years) as of the date of the exam. If the exam has ended, this will be the age as of end exam. If not, this will be the age as of the scheduled appointment date. If an appointment has not been scheduled for this exam, this value will be null. |
| 47 | `PRIORITIZED_UTC_DTTM` | DATETIME (UTC) |  | Stores the prioritized instant for the result in UTC |
| 48 | `RESULT_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | Stores the last update instant for a result in UTC |
| 49 | `PROC_SVC_TYPE_CODE_C_NAME` | VARCHAR |  | This item contains a procedure service type (surgery, imaging, dental, etc.) that overrides the service type from a referral or coverage source. |
| 50 | `PERFORMED_IN_ISO_YN` | VARCHAR |  | Stores whether the imaging exam was performed in isolation. |
| 51 | `RFL_FIRST_APPOINTMENT_BY_DATE` | DATETIME |  | The date that the first appointment for the referral should occur by. |
| 52 | `RFL_LIVING_SITUATION_C_NAME` | VARCHAR | org | Describes who the patient or child lives with for this psychology referral order. |
| 53 | `RFL_CHILD_SERVICE_C_NAME` | VARCHAR | org | Indicates the child welfare service role in connection with child psychology services for the psychology referral order. |
| 54 | `RFL_PARENTAL_RESP_C_NAME` | VARCHAR | org | Indicates which entity has parental responsibility for the patient for the psychology referral order. |
| 55 | `RFL_CONSENT_TO_TREAT_STAT_C_NAME` | VARCHAR | org | Indicates the status of obtaining the patient's consent in connection with the referral's transfer of medical record information for the psychology referral order. |
| 56 | `RFL_CASE_WORKER_NAME` | VARCHAR |  | The case manager of the child psychology case for this psychology referral order. |
| 57 | `LUNG_OUTCOME_C_NAME` | VARCHAR |  | The positive/negative outcome for a lung imaging study. |
| 58 | `MAM_INDICATION_C_NAME` | VARCHAR |  | Indication for mammography exam specific to NMD version 2. Category values that can be mapped to BI-RADS indication for exam. |
| 59 | `HAS_LAB_SPEC_YN` | VARCHAR |  | Indicates whether the order or any of the linked performable orders have a lab specimen. 'Y' indicates that the order or one of the linked performable orders has a lab specimen. 'N' indicates that the order does not have a linked lab specimen and no linked performable order has a lab specimen. |
| 60 | `HAS_RSLT_CNCT_YN` | VARCHAR |  | Indicates whether the order has a resulted contact. 'Y' indicates that the order has at least one contact of type 2-Resulted. 'N' indicates that the order does not have any contacts of type 2-Resulted. |
| 61 | `HAS_CORR_YN` | VARCHAR |  | Indicates whether the order has a correction. 'Y' indicates that the order has at least one contact with procedure result status equal to 4-Edited or 5-Edited Result - FINAL. 'N' indicates that the order does not have any contacts with procedure result status equal to 4-Edited or 5-Edited Result - FINAL. |
| 62 | `LAB_REDRAW_REASON_C_NAME` | VARCHAR | org | The last redraw reason category ID for the order. |
| 63 | `PANEL_RELEASE_DTTM` | DATETIME (Local) |  | If this order is a performable order on a test panel, this item stores the local date and time when the associated orderable was released. This column will only be populated for performable orders on test panels. It will not be populated for the orderable order on test panels. |
| 64 | `PANEL_RELEASE_UTC_DTTM` | DATETIME (UTC) |  | If this order is a performable order on a test panel, this item contains the UTC date and time when the associated orderable was released. This column will only be populated for performable orders on test panels. It will not be populated for the orderable order on test panels. |
| 65 | `LAST_RSLT_LAB_ID` | NUMERIC |  | The unique ID of the resulting lab from the last contact where the procedure result status is not null. |
| 66 | `LAST_RSLT_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 67 | `MAM_TECH_IMG_DOC_REV_DTTM` | DATETIME (UTC) |  | Stores the instant when the last technologist image documentation was reviewed. |
| 68 | `MAM_TECH_IMG_DOC_REV_USER_ID` | VARCHAR |  | Stores the user ID of the last person to review the technologist imaging documentation. |
| 69 | `MAM_TECH_IMG_DOC_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 70 | `NMD_3_MAM_INDICATION_C_NAME` | VARCHAR |  | Indication for mammography exam specific to NMD version 3. Category values that can be mapped to BI-RADS indication for exam. . |
| 71 | `OUTPAT_START_DATE` | DATETIME |  | The start date of the recurring order. When the first instance of the order should happen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BILL_AREA_ID` | [V_BIL_ALL](V_BIL_ALL.md) | sole_pk | high |

## Joined in

Inbound joins are tracked on the logical base [ORDER_PROC](ORDER_PROC.md).

