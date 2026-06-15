# OR_CASE_3

> The OR_CASE_3 table enables you to report on surgical and procedural case data. This table has the same basic structure as OR_CASE and OR_CASE_2, but was created as a second table to prevent OR_CASE and OR_CASE_2 from getting any larger.

**Overflow of:** [OR_CASE](OR_CASE.md)  
**Primary key:** `CASE_ID`  
**Columns:** 99  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the case request record. |
| 2 | `SETUP_TIME_MOD_YN` | VARCHAR |  | This item tracks whether the setup time for a case has been modified by the user. |
| 3 | `DFLT_SETUP_MINS` | INTEGER |  | This item stores the setup time defaulted by the system. |
| 4 | `DFLT_CLEANUP_MINS` | INTEGER |  | This item stores the clean up time defaulted by the system. |
| 5 | `DFLT_PREP_MINS` | INTEGER |  | This item stores the patient prep time defaulted by the system. |
| 6 | `DFLT_WRAPUP_MINS` | INTEGER |  | This item stores the wrap-up time defaulted by the system. |
| 7 | `CLEANUP_TIME_MOD_YN` | VARCHAR |  | This item tracks whether the clean up time for a case has been modified by the user. |
| 8 | `WRAPUP_TIME_MOD_YN` | VARCHAR |  | This item tracks whether the wrap-up time for a case has been modified by the user. |
| 9 | `CASE_LEN_MOD_YN` | VARCHAR |  | This item indicates whether the length of a procedure or panel has been modified by a user. |
| 10 | `LEN_MOD_USER_ID` | VARCHAR |  | This item tracks the last user to modify a length of a procedure or panel such that a length doesn't use the defaulted length. |
| 11 | `LEN_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `PAN1_PAN_DLFT_SNG_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there is only a single procedure in this panel. |
| 13 | `PAN1_PAN_DLFT_MLT_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple procedures on this panel. |
| 14 | `PAN1_PAN_DLFT_PAN_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple panels on this case. |
| 15 | `PAN2_PAN_DLFT_SNG_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there is only a single procedure in this panel. |
| 16 | `PAN2_PAN_DLFT_MLT_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple procedures on this panel. |
| 17 | `PAN2_PAN_DLFT_PAN_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple panels on this case. |
| 18 | `PAN3_PAN_DLFT_SNG_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there is only a single procedure in this panel. |
| 19 | `PAN3_PAN_DLFT_MLT_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple procedures on this panel. |
| 20 | `PAN3_PAN_DLFT_PAN_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple panels on this case. |
| 21 | `PAN4_PAN_DLFT_SNG_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there is only a single procedure in this panel. |
| 22 | `PAN4_PAN_DLFT_MLT_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple procedures on this panel. |
| 23 | `PAN4_PAN_DLFT_PAN_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple panels on this case. |
| 24 | `PAN5_PAN_DLFT_SNG_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there is only a single procedure in this panel. |
| 25 | `PAN5_PAN_DLFT_MLT_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple procedures on this panel. |
| 26 | `PAN5_PAN_DLFT_PAN_TYP_C_NAME` | VARCHAR |  | This item stores the defaulting method used for generating procedure time estimates for this panel when there are multiple panels on this case. |
| 27 | `PAN1_REQ_PROC_MINS` | INTEGER |  | This item holds the requested total number of minutes for all the procedures in a panel. |
| 28 | `PAN2_REQ_PROC_MINS` | INTEGER |  | This item holds the requested total number of minutes for all the procedures in a panel. |
| 29 | `PAN3_REQ_PROC_MINS` | INTEGER |  | This item holds the requested total number of minutes for all the procedures in a panel. |
| 30 | `PAN4_REQ_PROC_MINS` | INTEGER |  | This item holds the requested total number of minutes for all the procedures in a panel. |
| 31 | `PAN5_REQ_PROC_MINS` | INTEGER |  | This item holds the requested total number of minutes for all the procedures in a panel. |
| 32 | `PAN1_REQ_PROC_CMTS` | VARCHAR |  | This item holds the comments regarding the requested total procedure length in minutes. |
| 33 | `PAN2_REQ_PROC_CMTS` | VARCHAR |  | This item holds the comments regarding the requested total procedure length in minutes. |
| 34 | `PAN3_REQ_PROC_CMTS` | VARCHAR |  | This item holds the comments regarding the requested total procedure length in minutes. |
| 35 | `PAN4_REQ_PROC_CMTS` | VARCHAR |  | This item holds the comments regarding the requested total procedure length in minutes. |
| 36 | `PAN5_REQ_PROC_CMTS` | VARCHAR |  | This item holds the comments regarding the requested total procedure length in minutes. |
| 37 | `PAN1_REQ_PROC_ACT_C_NAME` | VARCHAR | org | This item stores the action taken in regards to the requested total procedure length in minutes for this panel. |
| 38 | `PAN2_REQ_PROC_ACT_C_NAME` | VARCHAR |  | This item stores the action taken in regards to the requested total procedure length in minutes for this panel. |
| 39 | `PAN3_REQ_PROC_ACT_C_NAME` | VARCHAR |  | This item stores the action taken in regards to the requested total procedure length in minutes for this panel. |
| 40 | `PAN4_REQ_PROC_ACT_C_NAME` | VARCHAR |  | This item stores the action taken in regards to the requested total procedure length in minutes for this panel. |
| 41 | `PAN5_REQ_PROC_ACT_C_NAME` | VARCHAR |  | This item stores the action taken in regards to the requested total procedure length in minutes for this panel. |
| 42 | `PAN1_PANEL_CONFIDENCE_C_NAME` | VARCHAR |  | This item stores the confidence in Epic's estimated panel length for panel 1 |
| 43 | `PAN2_PANEL_CONFIDENCE_C_NAME` | VARCHAR |  | This item stores the confidence in Epic's estimated panel length for panel 2 |
| 44 | `PAN3_PANEL_CONFIDENCE_C_NAME` | VARCHAR |  | This item stores the confidence in Epic's estimated panel length for panel 3 |
| 45 | `PAN4_PANEL_CONFIDENCE_C_NAME` | VARCHAR |  | This item stores the confidence in Epic's estimated panel length for panel 4 |
| 46 | `PAN5_PANEL_CONFIDENCE_C_NAME` | VARCHAR |  | This item stores the confidence in Epic's estimated panel length for panel 5 |
| 47 | `PAT_CONF_CASE_YN` | VARCHAR |  | Whether the patient confirmed their case or not. Set to Yes by 2-way text confirmation or by OR staff. |
| 48 | `CASE_CONF_UTC_DTTM` | DATETIME (UTC) |  | The most recent instant of a patient's case confirmation. Part of the patient case confirmation workflow. Updated each time the patient confirms and reset to null when case is rescheduled to different date or OR location. |
| 49 | `CASE_CONF_PAT_ID` | VARCHAR | FK→ | The patient ID of the patient if they texted to confirm their own case. |
| 50 | `CONF_PAT_RELATIONSHIP_ID` | NUMERIC |  | The Guardian (RLA networked ID) that confirmed the patient's case through text. |
| 51 | `CASE_CONF_USER_ID` | VARCHAR |  | The employee ID (EMP networked) that confirmed the patient's case. |
| 52 | `CASE_CONF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 53 | `PAN1_TOTAL_PROC_MIN` | INTEGER |  | The total number of minutes required for all of the procedures on this panel. |
| 54 | `PAN1_DFLT_PROC_MINS` | INTEGER |  | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| 55 | `PAN1_PROC_MIN_MOD_YN` | VARCHAR |  | Whether the total number of minutes required for all of the procedures on this panel has been modified from the defaulted value calculated by the system. This does not track whether the lengths of any of the individual procedures on the panel have been modified. |
| 56 | `PAN1_PROC_START` | INTEGER |  | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| 57 | `PAN1_PRC_STRT_MOD_YN` | VARCHAR |  | Whether the time at which this panel's procedures should begin has been manually edited by a user. |
| 58 | `PAN1_REQ_MINS_USER_ID` | VARCHAR |  | The id of the user who requested a total procedure length for this panel in minutes. |
| 59 | `PAN1_REQ_MINS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 60 | `PAN2_TOTAL_PROC_MIN` | INTEGER |  | The total number of minutes required for all of the procedures on this panel. |
| 61 | `PAN2_DFLT_PROC_MINS` | INTEGER |  | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| 62 | `PAN2_PROC_MIN_MOD_YN` | VARCHAR |  | Whether the total number of minutes required for all of the procedures on this panel has been modified from the defaulted value calculated by the system. This does not track whether the lengths of any of the individual procedures on the panel have been modified. |
| 63 | `PAN2_PROC_START` | INTEGER |  | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| 64 | `PAN2_PRC_STRT_MOD_YN` | VARCHAR |  | Whether the time at which this panel's procedures should begin has been manually edited by a user. |
| 65 | `PAN2_REQ_MINS_USER_ID` | VARCHAR |  | The id of the user who requested a total procedure length for this panel in minutes. |
| 66 | `PAN2_REQ_MINS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 67 | `PAN3_TOTAL_PROC_MIN` | INTEGER |  | The total number of minutes required for all of the procedures on this panel. |
| 68 | `PAN3_DFLT_PROC_MINS` | INTEGER |  | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| 69 | `PAN3_PROC_MIN_MOD_YN` | VARCHAR |  | Whether the total number of minutes required for all of the procedures on this panel has been modified from the defaulted value calculated by the system. This does not track whether the lengths of any of the individual procedures on the panel have been modified. |
| 70 | `PAN3_PROC_START` | INTEGER |  | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| 71 | `PAN3_PRC_STRT_MOD_YN` | VARCHAR |  | Whether the time at which this panel's procedures should begin has been manually edited by a user. |
| 72 | `PAN3_REQ_MINS_USER_ID` | VARCHAR |  | The id of the user who requested a total procedure length for this panel in minutes. |
| 73 | `PAN3_REQ_MINS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 74 | `PAN4_TOTAL_PROC_MIN` | INTEGER |  | The total number of minutes required for all of the procedures on this panel. |
| 75 | `PAN4_DFLT_PROC_MINS` | INTEGER |  | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| 76 | `PAN4_PROC_MIN_MOD_YN` | VARCHAR |  | Whether the total number of minutes required for all of the procedures on this panel has been modified from the defaulted value calculated by the system. This does not track whether the lengths of any of the individual procedures on the panel have been modified. |
| 77 | `PAN4_PROC_START` | INTEGER |  | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| 78 | `PAN4_PRC_STRT_MOD_YN` | VARCHAR |  | Whether the time at which this panel's procedures should begin has been manually edited by a user. |
| 79 | `PAN4_REQ_MINS_USER_ID` | VARCHAR |  | The id of the user who requested a total procedure length for this panel in minutes. |
| 80 | `PAN4_REQ_MINS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 81 | `PAN5_TOTAL_PROC_MIN` | INTEGER |  | The total number of minutes required for all of the procedures on this panel. |
| 82 | `PAN5_DFLT_PROC_MINS` | INTEGER |  | The total number of minutes required for all of the procedures on this panel as calculated by the system using procedure length estimates, preference cards, and procedure records. |
| 83 | `PAN5_PROC_MIN_MOD_YN` | VARCHAR |  | Whether the total number of minutes required for all of the procedures on this panel has been modified from the defaulted value calculated by the system. This does not track whether the lengths of any of the individual procedures on the panel have been modified. |
| 84 | `PAN5_PROC_START` | INTEGER |  | The time at which this panel's procedures should begin. This is measured in minutes relative to the beginning of the case. |
| 85 | `PAN5_PRC_STRT_MOD_YN` | VARCHAR |  | Whether the time at which this panel's procedures should begin has been manually edited by a user. |
| 86 | `PAN5_REQ_MINS_USER_ID` | VARCHAR |  | The id of the user who requested a total procedure length for this panel in minutes. |
| 87 | `PAN5_REQ_MINS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 88 | `CASE_CONF_MYPT_ID` | VARCHAR |  | The MyChart user (WPR networked ID) that confirmed the patient's case through text. |
| 89 | `INSTR_PICKING_STATUS_C_NAME` | VARCHAR |  | Status of picking instruments for the case |
| 90 | `CS_CASE_ELIGIBLE_YN` | VARCHAR |  | Indicates whether a case is eligible for being suggested for earlier dates. 'Y' indicates that the case is eligible for suggestions. 'N' or NULL indicate that the case will not be eligible and won't be suggested. |
| 91 | `START_AT_OR_AFTER_OVERRIDE_TM` | DATETIME (Local) |  | Case should be scheduled on or after this time. |
| 92 | `START_AT_OR_BEFORE_OVERRIDE_TM` | DATETIME (Local) |  | Case should be scheduled on or after this time. |
| 93 | `SCHEDULE_SOURCE_MKTPL_YN` | VARCHAR |  | Has this surgical case ever been put on the schedule via the OR Marketplace? This item will be "yes" if so, even if the case's scheduling was later changed by a different workflow, and "no" or NULL otherwise. This item is determined by the values in I ORC 650. |
| 94 | `AUTH_PROV_ADDR` | VARCHAR |  | Stores the address ID for the authorizing provider for the case. |
| 95 | `PAT_REQUEST_CANCEL_YN` | VARCHAR |  | Indicates whether the patient requested to cancel their case. |
| 96 | `CASE_REQUEST_CANCEL_UTC_DTTM` | DATETIME (UTC) |  | The most recent instant of a patient's request to cancel a case. Part of the patient case confirmation workflow. Updated each time the patient confirms and reset to null when the case is rescheduled to different date or OR location. |
| 97 | `CASE_REQUEST_CANCEL_PAT_ID` | VARCHAR | FK→ | The patient who requested to cancel the case. |
| 98 | `REQ_CANCEL_PAT_RELATIONSHIP_ID` | NUMERIC |  | The guardian who requested to cancel the case. |
| 99 | `CS_CASE_PDS_ELIGIBLE_YN` | VARCHAR |  | Stores whether or not the case is eligible for patient-driven CRS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CASE_CONF_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `CASE_REQUEST_CANCEL_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in

Inbound joins are tracked on the logical base [OR_CASE](OR_CASE.md).

