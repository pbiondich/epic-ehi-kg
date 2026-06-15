# PAT_ENC_HSP_2

> The PAT_ENC_HSP_2 table is the subsequent table for the PAT_ENC_HSP table, which is the primary table for hospital encounter information. Each record in this table is based on a patient contact serial number.

**Overflow of:** [PAT_ENC_HSP](PAT_ENC_HSP.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 54  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `EX_DIS_DT_ENTR_DTTM` | DATETIME (Local) |  | The instant of entry of expected discharge date. |
| 5 | `EX_DIS_TM_ENTR_DTTM` | DATETIME (Local) |  | The instant of entry of expected discharge time. |
| 6 | `CONTRACT_REG_FLAG` | VARCHAR |  | Indicates whether an HOV contact was registered using the Contract Registration workflow. If this workflow was not used, this column is null. |
| 7 | `CONTRACT_CODE_C_NAME` | VARCHAR | org | The contract code category for the encounter. |
| 8 | `ACCEPTS_BLOOD_C_NAME` | VARCHAR | org | The category ID that indicates whether this patient accepts blood. |
| 9 | `ED_ARRIVAL_DETAILS` | VARCHAR |  | Free text information holding any details regarding the ED Arrival. |
| 10 | `CONS_SEDATION_C_NAME` | VARCHAR | org | The category ID of the conscious sedation status for the patient encounter. |
| 11 | `RESTRAINT_SECLUS_C_NAME` | VARCHAR | org | The restraint or seclusion status category ID for this patient encounter. |
| 12 | `MULTI_PREG_YN` | VARCHAR |  | Indicates whether the mother has a multiple pregnancy for this L&D encounter. |
| 13 | `DISASTER_NUM` | VARCHAR |  | This column stores the disaster number, which is a number given by the ambulance company to patients during catastrophes that cause massive patient influxes to the hospital. |
| 14 | `SRC_PATTERN_CSN_ID` | NUMERIC |  | The Contact Serial Number (CSN) of the Admission Pattern record associated with the projected bed usage for this patient encounter. If this projection is manually modified an end user, the column stores null. |
| 15 | `ENC_CLOSED_OR_COMPLETED_DATE` | DATETIME |  | The date that the encounter was closed or completed. |
| 16 | `ED_DISPO_PAT_COND_C_NAME` | VARCHAR | org | The category ID of the patient condition at time of disposition in the ED. |
| 17 | `ADOPTION_TYPE_C_NAME` | VARCHAR | org | Item to store what type of adoption is related to the current L&D contact. |
| 18 | `PRI_PROBLEM_ID` | NUMERIC |  | The unique ID of the principal problem for a patient's hospitalization. |
| 19 | `EXPECTED_DISCHRG_APPROX_TIME_C_NAME` | VARCHAR | org | Current approximate expected discharge time. Each value represents a time range (e.g. Morning, Midday, Afternoon, Evening). |
| 20 | `DISCH_MILEST_KICKOFF_UTC_DTTM` | DATETIME (UTC) |  | Displays the date and time that discharge milestones were initiated. |
| 21 | `DISCH_MILEST_AUTO_MANAGED_YN` | VARCHAR |  | Determines if discharge milestones have had any manual intervention. Discharge Milestones are considered auto-managed if the discharge order is the sole driver for kicking off and discontinuing milestones. |
| 22 | `PREDICTED_LOS` | NUMERIC |  | The Length of Stay value determined by the Predictive Model run. |
| 23 | `EXP_LOS_UPD_SRC_C_NAME` | VARCHAR | org | The source (e.g. Predictive Model, User Entered) from which the Expected Length of Stay was updated. |
| 24 | `ED_ENC_SRC_C_NAME` | VARCHAR |  | This column stores how an ED encounter was created (e.g. via interface, user workflows) |
| 25 | `ED_DEPART_UTC_DTTM` | DATETIME (UTC) |  | The ED Departure date and time in UTC. |
| 26 | `ADT_ARRIVAL_UTC_DTTM` | DATETIME (UTC) |  | The arrival date and time in UTC. |
| 27 | `HOSP_DISCH_UTC_DTTM` | DATETIME (UTC) |  | The hospital discharge date and time in UTC. |
| 28 | `HOSP_ADMSN_UTC_DTTM` | DATETIME (UTC) |  | The hospital admission date and time in UTC. |
| 29 | `INP_ADMSN_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the patient first reached a patient class of Inpatient in UTC. |
| 30 | `ED_HISTORICAL_YN` | VARCHAR |  | ED Historical Encounter is set by cutover and historical encounter interfaces when patient encounters are created for emergency patients. |
| 31 | `PATIENT_TASK_COMPLETION_RATE` | INTEGER |  | Aggregated task progression rates across all active tasks currently assigned to the patient. |
| 32 | `START_MED_REM_DISCHG_YN` | VARCHAR |  | If set to 1-Yes, medication reminders will start automatically after discharge. If set to 0-No or empty, medication reminders will not start automatically after discharge. |
| 33 | `EXPECTED_DISCHARGE_UNKNOWN_YN` | VARCHAR |  | Indicates whether the expected discharge date is unknown for this patient. 'Y' indicates that the expected discharge date is unknown and documented. 'N' indicates that the expected discharge date is known and documented. NULL indicates that no expected discharge info has been saved for this contact. |
| 34 | `DUAL_ADMISSION_CSN` | NUMERIC |  | In a dual admission scenario this will point from the encounter on leave to the admitted encounter. |
| 35 | `LOA_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This column is only populated when the encounter for this row is admitted and the patient currently has an encounter on a leave of absence. This column displays the unique contact serial number of the patient encounter that is on a leave of absence. |
| 36 | `INITIAL_ADT_PAT_STAT_C_NAME` | VARCHAR |  | The ADT type of encounter category ID initially assigned for the encounter. |
| 37 | `NOTIFICATION_SENT_FIRST_IP_YN` | VARCHAR |  | Indicates whether the Event Notification message was sent when the patient was upgraded to an IP class. 'Y' indicates that the message was sent. 'N' or NULL indicate that the message was not sent. Note that this message is only sent once, even though the date and time the patient became IP can be changed. |
| 38 | `NOTIFICATION_SENT_OBS_ADMSN_YN` | VARCHAR |  | Indicates whether the Event Notification message was sent when the patient was upgraded to an observation patient class. 'Y' indicates that the message was sent. 'N' or NULL indicate that the message was not sent. Note that this message is only sent once, even though the date and time the patient became observation can be changed. |
| 39 | `IB_ALERT_LENGTH_OF_STAY_MSG_ID` | VARCHAR |  | The unique ID of the In Basket Message that was sent to alert that a patient has gone past the approved length of stay. |
| 40 | `INITIAL_ADMIT_CONF_STAT_C_NAME` | VARCHAR |  | The encounter status category ID initially assigned to this encounter. |
| 41 | `TRANSFER_COMMENTS` | VARCHAR |  | The transfer comments entered by the user during the most recent transfer. |
| 42 | `MED_READINESS_DTTM` | DATETIME (Local) |  | The medical readiness date and time for this patient encounter. This date and time may be expected or confirmed, depending on whether the patient is medically ready or not. |
| 43 | `MED_READINESS_TIMEFRAM_C_NAME` | VARCHAR |  | The medical readiness timeframe category ID for the patient encounter |
| 44 | `MED_READINESS_YN` | VARCHAR |  | Indicates whether this patient encounter is medically ready for discharge. 'Y' indicates that this encounter has been marked medically ready for discharge. 'N' or NULL indicates that it has not been marked medically ready for discharge. |
| 45 | `MED_READINESS_INST_ENTRY_DTTM` | DATETIME (UTC) |  | The instant at which this patient's medical readiness information was last updated |
| 46 | `MED_READINESS_USER_ID` | VARCHAR |  | The unique ID of the user who last updated medical readiness information for this patient encounter |
| 47 | `MED_READINESS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 48 | `MED_READINESS_SOURCE_C_NAME` | VARCHAR |  | The medical readiness source category ID for this patient encounter |
| 49 | `EXPECTED_DISCH_DISP_C_NAME` | VARCHAR | org | The patient's expected discharge disposition. |
| 50 | `EXP_DISCH_DISP_USER_ID` | VARCHAR |  | This item logs the last user that changed the expected discharge disposition. |
| 51 | `EXP_DISCH_DISP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 52 | `EXP_DISCH_DISP_ENTRY_UTC_DTTM` | DATETIME (UTC) |  | The instant of entry of expected discharge disposition. |
| 53 | `PRIMARY_LINKED_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number of the primary linked hospital encounter. Encounters are considered linked if the start of encounter B occurs after the start of encounter A, but within 6 hours after the discharge of encounter A (including before the discharge of encounter A). Any encounters that would be linked to encounter B by that definition are instead linked to encounter A. This means that there is exactly one primary encounter for every series of linked encounters and that the primary linked encounter is the one within a series that has the earliest start time. |
| 54 | `TODO_ADM_DISCLAIMER_ACTIVE_YN` | VARCHAR |  | This item tracks if the To Do admission disclaimer should be shown or not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LOA_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PRIMARY_LINKED_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

