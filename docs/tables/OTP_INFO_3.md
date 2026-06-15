# OTP_INFO_3

> This table contains additional information about patient order templates.

**Overflow of:** [OTP_INFO](OTP_INFO.md)  
**Primary key:** `OTP_ID`  
**Columns:** 58  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK | The order template ID. |
| 2 | `CREATED_FROM_ORD_ID` | NUMERIC |  | If this order template (OTP) was created by adding an external order to a plan, this is the order it was created from. |
| 3 | `WT_MAX_DOSE` | NUMERIC |  | This column stores the saved weight- or body surface area- based maximum dose for the treatment plan. |
| 4 | `WT_MAX_DOSE_UNIT_C_NAME` | VARCHAR | org | This column stores the saved unit for the weight- or body surface area-based maximum dose for the treatment plan. |
| 5 | `MAX_DOSE_SOURCE_C_NAME` | VARCHAR |  | This column returns the source of max dose information for an order template that was used in the treatment plan. |
| 6 | `RX_DO_NOT_DISP_YN` | VARCHAR |  | This is the Patient Order Template (OTP) level setting that indicates if the medication being ordered should be marked as "Do Not Dispense" by default. |
| 7 | `MAX_DAILY_DOSE` | NUMERIC |  | Max daily dose value for the order template (OTP) as entered by the provider. This will be shown only for outpatient orders based on the configuration for Max daily dose highest DEA code (I LSD 35050) and Max daily dose meds grouper (I LSD 35051). |
| 8 | `MAX_DLY_DOSE_UNIT_C_NAME` | VARCHAR |  | Max daily dose unit (associated with I OTP 34195) for the order template as entered by the provider. This will be shown only for outpatient orders based on the configuration of Max daily dose highest DEA code (I LSD 35050) and Max daily dose meds grouper (I LSD 35051). |
| 9 | `MAXDOSE_HARDSTOP_YN` | VARCHAR |  | Indicate whether the max dose limit is hard stop or not. If "Yes", the max dose is hard stop. Otherwise, the max dose is not hard stop. |
| 10 | `CREATED_FROM_OTL_ID_ORDER_DESC` | VARCHAR |  | Description of the procedure. |
| 11 | `MED_REFILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `HOLD_PENDING_PA_YN` | VARCHAR |  | This item determines if a prior authorization request should be sent for a medication order when it is signed. |
| 13 | `SEND_PA_REQ_YN` | VARCHAR |  | This item specifies the payer that a prior authorization request should be sent to when a medication order is signed. |
| 14 | `PA_ORG_ID` | NUMERIC |  | This item specifies the payer that a prior authorization request should be sent to when the order is signed. |
| 15 | `PA_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 16 | `RATE_IS_CALCULATED_YN` | VARCHAR |  | Indicates whether the rate stored in this record is a calculated value |
| 17 | `VOLUME_IS_CALCULATED_YN` | VARCHAR |  | Indicates whether the volume stored in this record is a calculated value |
| 18 | `PREP_STATUS_C_NAME` | VARCHAR |  | Stores the current prep status of an order template |
| 19 | `MOD_FROM_OTP_ID` | NUMERIC |  | If this order template was created by modifying a released order, then this item will store the ID of the original released order template. |
| 20 | `SPEC_DOSE_LMT_HR` | INTEGER |  | The number of hours the dosing limit represents. |
| 21 | `SPEC_MED_TYPE_C_NAME` | VARCHAR |  | This indicates that the record is a special type of medication, such as patient-controlled analgesia (PCA). This will be used to determine what type of dosing should be used for the medication. |
| 22 | `SCHED_DUR` | INTEGER |  | Amount of time (in minutes) the order should contribute to an appointment |
| 23 | `SCHED_DUR_IS_CALC_YN` | VARCHAR |  | Set to "yes" if the scheduling duration (I OTP 16000) was calculated by the system. |
| 24 | `SCHED_DUR_BUFFER` | INTEGER |  | The amount of time (in minutes) to add to the scheduling duration if it was calculated by the system. |
| 25 | `SCHED_TOL_BEF` | INTEGER |  | How far before the expected date can the appointment be safely made. |
| 26 | `SCHED_TOL_AFTR` | INTEGER |  | How long after the expected date can the appointment be safely made. |
| 27 | `SCHED_TOL_NO_RESTR_BEF_YN` | VARCHAR |  | Is "before-tolerance" any day before the expected date? |
| 28 | `SCHED_TOL_NO_RESTR_AFTR_YN` | VARCHAR |  | Is "after-tolerance" any day after the expected date? |
| 29 | `IS_BLOOD_YN` | VARCHAR |  | This column will be Yes if this treatment plan order is a prepare or transfuse blood order that uses the prepare or transfuse amount display item. |
| 30 | `TRANSFUSE_AMOUNT` | INTEGER |  | The amount of blood to transfuse in a treatment plan order. |
| 31 | `TRANSFUSE_AMOUNT_UNIT_C_NAME` | VARCHAR |  | If this is a blood transfusion treatment plan order, this is the unit in which it was ordered. |
| 32 | `PREPARE_AMOUNT` | INTEGER |  | The amount of blood to prepare in a treatment plan order. |
| 33 | `PREPARE_AMOUNT_UNIT_C_NAME` | VARCHAR |  | If this is a blood prepare treatment plan order, this is the unit in which it was ordered. |
| 34 | `WEIGHT_BLD_AMOUNT` | NUMERIC |  | The weight-based amount on this prepare or transfuse patient order template. |
| 35 | `WEIGHT_BLD_UNIT_C_NAME` | VARCHAR |  | The weight-based unit on this prepare or transfuse patient order template. |
| 36 | `RELATIVE_EXPIRATION_DATE_C_NAME` | VARCHAR | org | Holds a category value for the expiration date. This may be subtly different from the expiration date (OTP_INFO.STANDING_EXP_DATE) for things like "in 3 months", which could be S+90, S+91, or S+92 depending on the current date. |
| 37 | `FUTURE_RELATIVE_EXPECTED_DT_C_NAME` | VARCHAR |  | Holds a category value for the expected completion date. This may be subtly different from the expected date (OTP_INFO.FUT_EXPECT_COMP_DT) for things like "in 3 months", which could be S+90, S+91, or S+92 depending on the current date. |
| 38 | `FUTURE_EXPECTED_DATE_COMMENT_C_NAME` | VARCHAR |  | Holds a category value for the comment part of expected date. This will include categories based on scheduling comments like "Before Surgery", "After Consult", etc. |
| 39 | `FUTURE_EXPECTED_DATE_DETAILS` | VARCHAR |  | Holds free-text details entered if the Once (Future) expected date comment (FUTURE_EXPECTED_DATE_COMMENT_C) is "Other (Specify)." |
| 40 | `SAV_PAT_BLOODREQT_YN` | VARCHAR |  | Flags whether signing the blood order will also update the patient's blood special requirements |
| 41 | `APPT_WINDOW_START_TIME` | DATETIME (Local) |  | Preferred appointment window. This is the start of the appointment window. |
| 42 | `APPT_WINDOW_END_TIME` | DATETIME (Local) |  | Preferred appointment window. This is the end of the appointment window. |
| 43 | `LEAVE_TYPE_C_NAME` | VARCHAR | org | Specifies the type of medical leave being ordered. |
| 44 | `LEAVE_START_DATE` | VARCHAR |  | Start date of the medical leave. |
| 45 | `LEAVE_END_DATE` | VARCHAR |  | End date of the medical leave. |
| 46 | `LEAVE_DURATION` | INTEGER |  | Duration of the medical leave in days. |
| 47 | `LEAVE_LIGHTDUTY_YN` | VARCHAR |  | Whether the medical leave also has a light duty period. |
| 48 | `LEAVE_LIGHTDUTY_START_DATE` | VARCHAR |  | Start date of the light duty period. |
| 49 | `LEAVE_LIGHTDUTY_END_DATE` | VARCHAR |  | End date of the light duty period. |
| 50 | `LEAVE_LIGHTDUTY_DURATION` | INTEGER |  | Duration of the light duty period in days. |
| 51 | `LEAVE_EXCUSED_ACTIVITIES_YN` | VARCHAR |  | Whether the patient should be excused from doing specific activities during the leave. |
| 52 | `LEAVE_EXCUSED_START_DATE` | VARCHAR |  | Start date of the excused activities period. |
| 53 | `LEAVE_EXCUSED_END_DATE` | VARCHAR |  | End date of the excuse period. |
| 54 | `LEAVE_EXCUSED_DURATION` | INTEGER |  | Duration of the excuse period in days. |
| 55 | `LEAVE_EXCUSED_COMMENTS` | VARCHAR |  | Comments about the excused activities for the excuse period. |
| 56 | `CONFIDENTIALITY_FLAG_C_NAME` | VARCHAR |  | This item stores whether a medication order should be treated as confidential from the patient's proxies. Medications with this item set to Hide From Patient Proxies are hidden from the patient's proxies in MyChart and from the proxy-friendly After Visit Summary. If set to Not Confidential, or not set, the information is still shown to patient proxies, unless otherwise hidden. This item only applies to non-immunization medication orders. |
| 57 | `PREVENT_RENEWAL_YN` | VARCHAR |  | Determines if renewals for this order should be disallowed. |
| 58 | `NO_RENEW_REASON_C_NAME` | VARCHAR |  | Stores why the "do not review" option was selected. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [OTP_INFO](OTP_INFO.md).

