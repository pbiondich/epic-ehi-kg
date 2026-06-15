# PAT_ENC_7

> This table supplements the PAT_ENC, PAT_ENC_2, PAT_ENC_3, PAT_ENC_4, PAT_ENC_5, and PAT_ENC_6 tables. It contains additional information related to patient encounters or appointments.

**Overflow of:** [PAT_ENC](PAT_ENC.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 38  
**Org-specific columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `NOTIFY_REP_ADMSN_C_NAME` | VARCHAR |  | Indicates whether a patient wants to have a family member or representative notified of their admission. |
| 5 | `REP_NOTIFIED_C_NAME` | VARCHAR | org | Indicates whether a patient's family or representative is notified of their admission. |
| 6 | `NOTIFY_REP_COMMENTS` | VARCHAR |  | Information about notifying a patient's family or representative of their admission. |
| 7 | `NOTIFY_PCP_ADMSN_C_NAME` | VARCHAR |  | Indicates whether a patient wants to have their PCP notified of their admission. |
| 8 | `PCP_NOTIFIED_C_NAME` | VARCHAR | org | Contains if/how the patient's PCP/Care Team has been notified of the patient's admission. The relevant Epic configuration setup in the event notification configuration record determines whether this item refers to the PCP or to the Care Team. |
| 9 | `NOTIFY_PCP_COMMENTS` | VARCHAR |  | Information about notifying a patient's PCP of their admission. |
| 10 | `ROC_PLANNING_PAT_ENC_CSN_ID` | NUMERIC |  | Stores the unique contact serial number of the resumption of care planning contact linked to this contact |
| 11 | `NUM_PREV_EPSD_C_NAME` | VARCHAR |  | Stores the number of previous consecutive episodes category ID for the patient |
| 12 | `SPEC_ORD_RSLT_NOT_AUTO_RLS_YN` | VARCHAR |  | It stores whether the order results of all the specimen orders created in the Specimens navigator section are automatically released to MyChart. |
| 13 | `RECENTLY_AT_SCHOOL_C_NAME` | VARCHAR | org | Whether the patient has recently been physically present at the school they work at or attend |
| 14 | `LMP_COMMENT` | VARCHAR |  | Free-text comments about the last menstrual period |
| 15 | `CONTACT_NUM` | INTEGER |  | The system-assigned number used to uniquely identify each of a given patient's encounters. |
| 16 | `ABN_REQUIRED_YN` | VARCHAR |  | Indicates whether an ABN required for this patient encounter. |
| 17 | `IS_ABN_SIGNED_C_NAME` | VARCHAR | org | Indicates whether the ABN has been signed for this encounter. |
| 18 | `MSP_IS_MEDICARE_HMO_C_NAME` | VARCHAR | org | Indicates whether the patient is covered by a Medicare HMO for this encounter. Used for MSPQ. |
| 19 | `REG_COMMENTS_DATE` | DATETIME |  | The date corresponding to the comment in PAT_ENC_REG_CMT table for this encounter. |
| 20 | `AUTO_MSG_DISABLED_YN` | VARCHAR |  | Whether messages that are automatically sent to a patient's companions should be disabled. |
| 21 | `DONT_AUTO_LINK_YN` | VARCHAR |  | Whether auto-linking should be disabled for a given encounter. |
| 22 | `RSN_FOR_NO_INC_MSG_C_NAME` | VARCHAR |  | The reason for no inc. message Category ID for the patient encounter. Indicates the reason there is no incomplete message to send for the encounter. |
| 23 | `HAS_HORMONE_DATA_YN` | VARCHAR |  | Whether the hormone history information is present on the given encounter. |
| 24 | `MEDS_REQUEST_LWS_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |
| 25 | `EVISIT_SUBMITTED_DTTM` | DATETIME (Local) |  | The instant in system local time at which the patient submitted the E-Visit. If conversion 888449 has not completed, this column might not have data for some submitted E-Visits. Consider using V_PAT_ENC_EVISIT.EVISIT_SUBMITTED_DTTM instead, which will always have a submission time for all submitted E-Visits. Talk to your operational database administrator or Epic representative to determine whether the conversion has finished. |
| 26 | `EVISIT_TURNAROUND_IN_MINUTES` | INTEGER |  | The amount of time, in minutes, between when a patient submitted the E-Visit and when a provider signed the encounter. If the encounter is not an E-Visit, or if the E-Visit was not both submitted and signed, then this column will be NULL. |
| 27 | `PREGNANCY_INTENTION_C_NAME` | VARCHAR | org | The patient's stated willingness to initiate a pregnancy within the subsequent year |
| 28 | `PREGNANCY_COUNSELED_YN` | VARCHAR |  | Whether the patient received counselling on how to achieve pregnancy |
| 29 | `BIRTH_CONTROL_COUNSELED_YN` | VARCHAR |  | Whether the patient wanted to discuss pregnancy prevention |
| 30 | `RSN_NO_BCM_COUNSELING_C_NAME` | VARCHAR | org | The reason why the patient did not want to discuss pregnancy prevention |
| 31 | `INTAKE_RSN_NO_CONTRACEPTIVE_C_NAME` | VARCHAR | org | The reason the patient has not been using contraceptives as of the start of the encounter |
| 32 | `CONTRACEPTIVE_DELIVERY_C_NAME` | VARCHAR | org | The method used to deliver or implement agreed contraceptives |
| 33 | `EXIT_RSN_NO_CONTRACEPTIVE_C_NAME` | VARCHAR |  | The reason for not agreeing during the encounter to implement contraceptives |
| 34 | `IS_VAP_DECLINED_YN` | VARCHAR |  | Indicates whether this Visit Auto Pay proposal has been declined or not. This is when a hyperspace user indicates that the patient has declined Visit Auto Pay. |
| 35 | `EPISODE_UPDATE_EFF_DATE` | DATETIME |  | The date when the information in this episode update encounter will start being used. |
| 36 | `EPISODE_UPD_CREAT_RSN_C_NAME` | VARCHAR | org | The category ID for the reason the episode update encounter was created. |
| 37 | `VISIT_MSG_DECLINE_YN` | VARCHAR |  | Whether the patient has declined visit messaging for this encounter. |
| 38 | `BILL_FOR_DENIAL_YN` | VARCHAR |  | The category ID for the decision on if Medicare should be billed for denial for this encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PAT_ENC](PAT_ENC.md).

