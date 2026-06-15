# OTP_INFO_4

> This table contains additional information about patient order templates.

**Overflow of:** [OTP_INFO](OTP_INFO.md)  
**Primary key:** `OTP_ID`  
**Columns:** 32  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK | The unique identifier (.1 item) for the patient order template record. |
| 2 | `DOSE_ADJ_ACCEPTED_YN` | VARCHAR |  | Stores whether the dose adjustment is accepted |
| 3 | `OTP_SIGN_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the patient CSN that the order template was signed in. |
| 4 | `INTENDED_DISPENSE_DAYS_SUPPLY` | INTEGER |  | Indicates the intended number of days supplied by each dispense of a prescription. |
| 5 | `IS_OTP_DELETED_YN` | VARCHAR |  | Whether an order template (OTP) has been deleted or not for EHI export purposes. An order template is considered deleted if it's associated to a deleted treatment day (VI TRG 10010), it's not yet signed or released (I OTP 140), and it's either listed as deleted in a treatment day (I TRG 1060), or (for therapy plan OTPs) is no longer linked to a specific treatment day. |
| 6 | `NO_REIMBURS_CODESET` | VARCHAR |  | Holds the code set of the selected reimbursement code. |
| 7 | `SEND_TO_PHARM_REASON_C_NAME` | VARCHAR | org | Reasons for sending a prescription directly to a pharmacy. For Australia e-prescribing. |
| 8 | `RX_MOBILE_NUM` | VARCHAR |  | Patient's mobile phone number. For Australia e-prescribing. |
| 9 | `MED_DIRECTIONS` | VARCHAR |  | The directions for the linked medication for the order template in this row. |
| 10 | `VERB_ORD_CMT` | VARCHAR |  | The verbal order comment for the order template in this row. |
| 11 | `NON_PREF_PROV_LVL_REASON_C_NAME` | VARCHAR | org | Stores the reason why a non preferred level provider was chosen |
| 12 | `MED_ORDERED_VOLUME` | VARCHAR |  | The volume as ordered linked to the order template. This volume can be in mL or in weight-based units. |
| 13 | `MED_ORDERED_VOLUME_UNIT_C_NAME` | VARCHAR | org | The volume unit as ordered linked to the order template. This volume unit can be in mL or in weight-based units. |
| 14 | `USES_TOD_IN_PAT_SIG_C_NAME` | VARCHAR |  | If the patient sig contains time of day indicators like "morning", "noon", "evening", or "bedtime". 1 if yes it does and I ORD 7661 will contain which times are included. 2 if no it doesn't, and that was determined either from an unsupported frequency or explicitly marking "no" when placing the composer. Null if the order was placed prior to this item, and therefore it isn't known. |
| 15 | `IMS_DISP_AT_SIGN_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 16 | `ADDL_WISH_DELIVER_YN` | VARCHAR |  | The additional wishes selection for deliver. Currently only used by the Netherlands. |
| 17 | `ADDL_WISH_MEDICATION_C_NAME` | VARCHAR |  | The additional wishes selection for the medication roll. Currently only used by the Netherlands. |
| 18 | `DENTAL_ASSOCIATED_TEETH` | VARCHAR |  | Corresponds to the associated teeth on a patient order template record. |
| 19 | `DURABLE_OTP_ID` | NUMERIC |  | For an OTP not created by day delinking, its item 545 is the same as its id. For an OTP created by day delinking, its item 545 is copied from item 545 of the OTP that it delinked from. |
| 20 | `OP_PRN_STATUS_YN` | VARCHAR |  | PRN status of a procedure order (OP order mode only). |
| 21 | `OP_PRN_STATUS_CMT` | VARCHAR |  | Comments about PRN status of a procedure order (OP order mode only). |
| 22 | `OP_FU_WITH_C_NAME` | VARCHAR |  | Who or what entity is responsible for a follow-up. |
| 23 | `LAST_CALC_DISP_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 24 | `OUTPAT_FLEX_TYPE_C_NAME` | VARCHAR |  | The procedure flexibility type with category values of "Now," "Anytime," "Date range," and "Target date." |
| 25 | `OUTPAT_LATEST_DATE_COMMENT` | VARCHAR |  | Stores the latest date that a procedure should be scheduled at. |
| 26 | `OUTPAT_LATEST_DATE_COMMENT_C_NAME` | VARCHAR | org | The category values used for the Once procedure latest date (OTP 664). |
| 27 | `RAD_THERAPY_TREATMENT_GOAL_C_NAME` | VARCHAR | org | This item stores the goal for prescribed radiation therapy treatment. |
| 28 | `RAD_THP_SEL_EPISODE_OPTION_C_NAME` | VARCHAR |  | Indicates if the procedure should generate a new radiation therapy episode, update an existing episode, or have no interaction with an episode. |
| 29 | `ASSOCIATED_RAD_THP_EPISODE_ID` | NUMERIC |  | The existing radiation therapy episode this order should be associated with. The radiation therapy details documented in the order will be added to the episode. |
| 30 | `CLINICAL_SEX_PARAM_C_NAME` | VARCHAR |  | The "Sex Parameter for Clinical Use" (sex categorization that aligns most with the patient in the context of the current order) category ID for the order template. |
| 31 | `CLINICAL_SEX_PARAM_COMMENT` | VARCHAR |  | The "Sex Parameter for Clinical Use" (sex categorization that aligns most with the patient in the context of the current order) comments entered in the Order Composer. |
| 32 | `CLINICAL_SEX_PARAM_UTC_DTTM` | DATETIME (UTC) |  | Last update date and time in UTC for Sex Parameter for Clinical Use, the sex categorization that aligns most with the patient in the context of the current order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_SIGN_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

## Joined in

Inbound joins are tracked on the logical base [OTP_INFO](OTP_INFO.md).

