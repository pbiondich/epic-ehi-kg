# TPL_INFO

> This table contains basic information about a treatment plan or a pathway, such as the plan/pathway name, the user who created the plan/pathway, when it was created, which protocol it was created from, the starting cycle number or step, etc.

**Primary key:** `TREATMENT_PLAN_ID`  
**Columns:** 68  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The treatment plan ID. |
| 2 | `TREATMENT_PLAN_NAME` | VARCHAR |  | The name of the treatment plan in this row. |
| 3 | `PLAN_STATUS_C_NAME` | VARCHAR |  | The status of the treatment plan in this row, for example Active or Inactive. |
| 4 | `PLAN_REC_TYP_C_NAME` | VARCHAR |  | The record type of the treatment plan in this row, for example Treatment Plan or Simple Plan. |
| 5 | `PLAN_START_DATE` | DATETIME |  | The start date in external format of the treatment plan in this row. For treatment plans this is the date of the first cycle within the plan. |
| 6 | `ZERO_BASED_YN` | VARCHAR |  | The yes/no flag signaling whether the days start at day 0 or day 1. |
| 7 | `PROTOCOL_ID` | NUMERIC | shared | The ID of the protocol that generated the treatment plan in this row. |
| 8 | `PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 9 | `PROTOCOL_DAT` | VARCHAR |  | The contact date (DAT) of the protocol that generated the treatment plan in this row. |
| 10 | `CREATED_USER_ID` | VARCHAR |  | The user ID of the person who created the treatment plan in this row. |
| 11 | `CREATED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `CREATED_ON_TM` | DATETIME (Attached) |  | The date/time in external format that the treatment plan in this row was created. |
| 13 | `PLAN_VERIF_DATE_TM` | DATETIME (Local) |  | The date/time in external format when the treatment plan in this row was last verified. |
| 14 | `PLAN_VERIF_USER_ID` | VARCHAR |  | The user ID of the person who last verified the treatment plan in this row. |
| 15 | `PLAN_VERIF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `DC_REASON_C_NAME` | VARCHAR | org | The reason for discontinuing the treatment plan in this row. |
| 17 | `DISPLAY_NAME` | VARCHAR |  | The treatment plan display name entered by the user. |
| 18 | `FIRST_CYCLE_NUM` | INTEGER |  | The cycle number of the first cycle in the treatment plan. |
| 19 | `START_CYCLE_NUM` | INTEGER |  | The cycle number of the cycle marked as the 'start cycle' in the treatment plan. |
| 20 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient who is associated with this treatment plan or pathway. |
| 21 | `PATHWAY_DISC_RESN_C_NAME` | VARCHAR | org | Stores the reason for discontinuing the pathway. |
| 22 | `REV_NEXT_DUE` | VARCHAR |  | The contact date (DAT) or treatment number when review reminders begin to display to users. |
| 23 | `REV_EXPIRES` | VARCHAR |  | The contact date (DAT) or treatment number after which this plan will be considered unreviewed. |
| 24 | `TRT_GOAL_C_NAME` | VARCHAR | org | Stores the treatment goal for the treatment plan. |
| 25 | `TPL_PROVIDER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 26 | `PLAN_VERSION` | INTEGER |  | Stores the lowest Version in which the plan was edited. This data is used to determine what features will be enabled for the plan. |
| 27 | `REFERRAL_ID` | NUMERIC | FK→ | Stores the ID of a referral which is used for prior authorization. |
| 28 | `DEVIATION_USER_ID` | VARCHAR |  | The user who signed off on the treatment plan deviation |
| 29 | `DEVIATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `DEVIATION_DTTM` | DATETIME (UTC) |  | The instant when the treatment plan was given a signoff for deviation |
| 31 | `DEVIATION_REASON_C_NAME` | VARCHAR | org | The reason to specify why the plan deviation from protocol |
| 32 | `DEVIATION_COMMENT` | VARCHAR |  | The comment to give more information about the deviation reason. This only extracts the first 4000 characters. |
| 33 | `LAST_DEVIATION_DTTM` | DATETIME (UTC) |  | Stores the instant when the plan last deviated from the protocol |
| 34 | `DEVIATION_REQUESTOR_ID` | VARCHAR |  | Stores the user who marked the plan as needing approval for deviation |
| 35 | `DEVIATION_REQUESTOR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 36 | `NEXT_PLANNED_DATE` | DATETIME |  | Next planned treatment date for a plan. |
| 37 | `INFUSION_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 38 | `PROTOCOL_CONTACT_DATE_REAL` | FLOAT |  | The contact date real of the protocol that generated the treatment plan in this row. The contact date real is a unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 39 | `HOLD_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when this plan was put on hold, if it is on hold. |
| 40 | `HOLD_USER_ID` | VARCHAR |  | The user who put this plan on hold, if it is on hold. |
| 41 | `HOLD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 42 | `HOLD_REASON_C_NAME` | VARCHAR | org | The reason why this plan was put on hold. |
| 43 | `HOLD_COMMENT` | VARCHAR |  | The comment entered when this plan was put on hold. |
| 44 | `PROGRAM_NUMBER` | INTEGER |  | This item contains the program number for a treatment plan |
| 45 | `REGIMEN_NUMBER` | INTEGER |  | This item contains the regimen number for a treatment plan |
| 46 | `LINE_OF_TREATMENT_C_NAME` | VARCHAR | org | Stores the line of treatment for the treatment plan. |
| 47 | `PROTOCOL_SUGGESTION_SOURCE_C_NAME` | VARCHAR |  | Indicates which type of protocol suggestion, if any, led to the creation of this treatment plan. |
| 48 | `PROTOCOL_LINK_CSN` | NUMERIC |  | For a treatment plan created from a linked protocol (PTP) record, this column stores the contact serial number (CSN) of the PTP contact linking the clinical protocol contact to a billing protocol contact. |
| 49 | `CREATION_STATE_C_NAME` | VARCHAR |  | This item stores the creation status of a therapy plan based on whether the plan or added plan has been signed or activated. |
| 50 | `STUDY_CURRENT_VERSION_IDENT` | VARCHAR |  | The current study version identifier of the treatment plan. |
| 51 | `PRIOR_AUTH_PRIMARY_COVERAGE_ID` | NUMERIC |  | This item stores the primary coverage ID that is used to generate the Referral in the treatment or therapy plan. |
| 52 | `BMT_AMEND_USER_ID` | VARCHAR |  | the user who amended the plan which resulted in the creation of a new treatment plan. |
| 53 | `BMT_AMEND_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 54 | `BMT_PLAN_AMEND_INST_DTTM` | DATETIME (UTC) |  | The instant that the plan was amended. |
| 55 | `REFERRAL_STATUS_CHNG_UTC_DTTM` | DATETIME (UTC) |  | This item stores the most recent instant when the treatment plan referral status changed due to changes made to the treatment plan. |
| 56 | `DISCON_COMMENT` | VARCHAR |  | It stores the discontinue comments entered by the user. |
| 57 | `DISCON_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the discontinue plan instant. |
| 58 | `DISCON_PLAN_USER_ID` | VARCHAR |  | This item store the user who discontinued the plan. |
| 59 | `DISCON_PLAN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 60 | `LAST_USER_ACTION_UTC_DTTM` | DATETIME (UTC) |  | Stores the last instant that a user interacted directly with the plan. This item will not be updated when the plan is updated by an action outside the plan or by a background process. |
| 61 | `RECONCILIATION_EVENT_ID` | VARCHAR |  | This item contains the ID of the event used to track reconciliation actions for this plan |
| 62 | `NEEDS_RECONCILIATION_YN` | VARCHAR |  | This item contains whether or not the plan needs reconciliation |
| 63 | `NEXT_UNAUTH_TREATMENT_DAY_ID` | NUMERIC |  | This item stores the treatment day ID of the next unauthorized day in the treatment plan. |
| 64 | `IS_PLAN_DELETED_YN` | VARCHAR |  | Virtual item that determines if a treatment plan (TPL) has been deleted or not for EHI export purpose. A treatment plan is considered deleted if it has a discontinued reason (I TPL 120) that's defined as entered in error (I LSD 77800), or if it's a BMT plan and its associated HSB record is deleted (I HSB 50). A dental treatment plan is never considered deleted. |
| 65 | `TREATMENT_START_DATE` | DATETIME |  | The date of the first treatment cycle in a treatment plan. |
| 66 | `REFERRING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 67 | `PLAN_NOTE_ID` | VARCHAR |  | The unique ID of the note record that contains the notes for a treatment or therapy plan. |
| 68 | `EFF_END_DATE` | DATETIME |  | The effective end date for a treatment plan. If a plan is still active this will be the date the last cycle ends and if it is discontinued it will be the date of the last started treatment day. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

