# IMPLANT_OT_2

> This table contains implant information that changes over time.

**Overflow of:** [IMPLANT_OT](IMPLANT_OT.md)  
**Primary key:** `IMPLANT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 102  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `SENSOR_MONITORED_HEART_RATE` | INTEGER |  | Sensor monitored heart rate. |
| 5 | `PA_SYSTOLIC_PRESSURE` | INTEGER |  | Pulmonary Artery Systolic Pressure |
| 6 | `PA_SYSTOLIC_PRESSURE_TREND` | INTEGER |  | Pulmonary Artery Systolic Pressure Trend |
| 7 | `PA_DIASTOLIC_PRESSURE` | INTEGER |  | Pulmonary Artery Diastolic Pressure |
| 8 | `PA_DIASTOLIC_PRESSURE_TREND` | INTEGER |  | Pulmonary Artery Diastolic Pressure Trend |
| 9 | `PA_MEAN_PRESSURE` | INTEGER |  | Pulmonary Artery Mean Pressure |
| 10 | `PA_MEAN_PRESSURE_TREND` | INTEGER |  | Pulmonary Artery Mean Pressure Trend |
| 11 | `PATH_OF_CONGESTION_C_NAME` | VARCHAR | org | Stores the category value for the pathophysiology of congestion |
| 12 | `ATRIAL_PACED_PERCENTAGE` | NUMERIC |  | This item stores the Atrial Paced Percentage for an ICD check workflow |
| 13 | `ATRIAL_SENSE` | NUMERIC |  | This item stores the Atrial Sense for an ICD check workflow |
| 14 | `ICD_RSN_GENRTR_UPGRADE_C_NAME` | VARCHAR | org | The category ID for the reason for the ICD generator upgrade. Choices include ICD to CRT-D and Single ICD to dual ICD. |
| 15 | `ICD_EXPLANT_TREAT_REC_C_NAME` | VARCHAR | org | The category ID for the planned treatment post explant of the ICD/CRT-D device at the time of the procedure. Choices include downgrade and no reimplant. |
| 16 | `ICD_CS_LV_SUCCESS_V22_C_NAME` | VARCHAR | org | The category ID indicating whether a coronary sinus/left ventricular (CS/LV) lead was successfully implanted during an ICD implant or ICD change procedure. Other choices include not attempted, attempted but not successful, and previously implanted. |
| 17 | `PSA_SLEW` | NUMERIC |  | The slew rate of the pacing system analyzer. |
| 18 | `PSA_PACING_IMP` | NUMERIC |  | The impedance of the pacing system analyzer. |
| 19 | `MEASUREMENT_ABOVE_THRESHOLD_YN` | VARCHAR |  | A measurement was higher than the instruments could record. |
| 20 | `PSA_PULSE_WIDTH` | NUMERIC |  | The pulse width of the pacing system analyzer. |
| 21 | `PREV_PROC_DATE` | DATETIME |  | The date when a previous procedure was performed on the implant/joint. |
| 22 | `HUMERUS_STATUS_C_NAME` | VARCHAR | org | The humerus implant status category ID for the implant. |
| 23 | `GLENOID_STATUS_C_NAME` | VARCHAR | org | The glenoid implant status category ID for the implant. |
| 24 | `LEAD_REMOVAL_ATTEMPT_YN` | VARCHAR |  | This item stores whether there was an attempt to remove the lead after disconnecting. |
| 25 | `LEAD_REMOVAL_YN` | VARCHAR |  | Stores whether the pacemaker lead was removed completely or incompletely |
| 26 | `PSA_THRESHOLD_UNABLE_YN` | VARCHAR |  | This item stores whether the PSA capture threshold was unable to be obtained |
| 27 | `PSA_GREATER_THAN_YN` | VARCHAR |  | This item stores whether the measurement was higher than the instruments could record. |
| 28 | `PSA_AMP_PACED_YN` | VARCHAR |  | This item stores whether the lead PSA amplitude was retrieved as a paced measurement. |
| 29 | `PSA_AMP_NA_YN` | VARCHAR |  | This item stores whether the lead PSA amplitude is not obtained because the patient is pacemaker dependent. |
| 30 | `LEAD_SLEW_GREATER_YN` | VARCHAR |  | Stores whether the pacemaker lead Pacing System Analyzer slew rate is greater than the maximum amount. |
| 31 | `LEAD_REMOVAL_CMT` | VARCHAR |  | A comment associated with the extent of removal of a lead to store extra information about the removal. |
| 32 | `PACE_VF_DET_RATE_BPM` | NUMERIC |  | The VF Detection Rate for Pacemaker Implants in beats per minute (BPM). |
| 33 | `PACE_FAST_VF_DET_RATE_BPM` | NUMERIC |  | The Fast VF Detection Rate for Pacemaker Implants in beats per minute (BPM). |
| 34 | `PACE_VT_DET_RATE_BPM` | NUMERIC |  | The VT Detection Rate for Pacemaker Implants in beats per minute (BPM). |
| 35 | `IMP_NUM_ATP_VFZONE` | NUMERIC |  | The number of VF Zone Therapy ATP for an Implant. |
| 36 | `IMP_NUM_ATP_FAST_VFZONE` | NUMERIC |  | The number of Fast VF Zone Therapy ATP for an ICD. |
| 37 | `IMP_NUM_ATP_VFZONE_ICD` | NUMERIC |  | The number of VF Zone Therapy ATP for an ICD. |
| 38 | `IMP_NUM_ATP_FAST_VT_ICD` | NUMERIC |  | The number of Fast VT Therapy ATP for an ICD. |
| 39 | `IMP_NUM_ATP_VT_ICD` | NUMERIC |  | The number of VT Therapy ATP for an ICD. |
| 40 | `IMP_NUM_SHOCK_VFZONE_ICD` | NUMERIC |  | The number of VF Zone Therapy Shocks for an ICD. |
| 41 | `IMP_NUM_SHOCK_VT_ICD` | NUMERIC |  | The number of VT Therapy Shocks for an ICD. |
| 42 | `IMP_NUM_SHOCK_FAST_VT_ICD` | NUMERIC |  | The number of Fast VT Therapy Shocks for an ICD. |
| 43 | `ASSOCIATED_PROC_ID` | VARCHAR |  | Associates an implant record with one of the procedures on the procedure log. |
| 44 | `ASSOCIATED_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 45 | `LIR_RESPONSE_C_NAME` | VARCHAR |  | This item tracks the response received from the national implant registry (LIR) after an attempted submission. |
| 46 | `LEAD1_INSERTION_YN` | VARCHAR |  | Indicates whether or not the first lead was inserted. |
| 47 | `LEAD2_INSERTION_YN` | VARCHAR |  | Indicates whether or not the second lead was inserted. |
| 48 | `LEAD3_INSERTION_YN` | VARCHAR |  | Indicates whether or not the third lead was inserted. |
| 49 | `LEAD1_LOCALIZATION_C_NAME` | VARCHAR | org | Indicates the location of the first lead localization. |
| 50 | `LEAD2_LOCALIZATION_C_NAME` | VARCHAR |  | Indicates the location of the second lead localization. |
| 51 | `LEAD3_LOCALIZATION_C_NAME` | VARCHAR |  | Indicates the location of the third lead localization. |
| 52 | `LEAD1_POLARITY_C_NAME` | VARCHAR | org | Indicates the type of polarity for the first lead. |
| 53 | `LEAD2_POLARITY_C_NAME` | VARCHAR |  | Indicates the type of polarity for the second lead. |
| 54 | `LEAD3_POLARITY_C_NAME` | VARCHAR |  | Indicates the type of polarity for the third lead. |
| 55 | `LEAD1_SCREWED_YN` | VARCHAR |  | Indicates whether or not the first lead was screwed to the heart or some other area. |
| 56 | `LEAD2_SCREWED_YN` | VARCHAR |  | Indicates whether or not the second lead was screwed to the heart or some other area. |
| 57 | `LEAD3_SCREWED_YN` | VARCHAR |  | Indicates whether or not the third lead was screwed to the heart or some other area. |
| 58 | `LEAD1_STIMULATION_THRESHOLD` | NUMERIC |  | Indicates the first lead's stimulation threshold in volts. |
| 59 | `LEAD2_STIMULATION_THRESHOLD` | NUMERIC |  | Indicates the second lead's stimulation threshold in volts. |
| 60 | `LEAD3_STIMULATION_THRESHOLD` | NUMERIC |  | Indicates the third lead's stimulation threshold in volts. |
| 61 | `LEAD1_STIMULATION_DURATION` | INTEGER |  | Indicates the first lead's stimulation duration in milliseconds. |
| 62 | `LEAD2_STIMULATION_DURATION` | INTEGER |  | Indicates the second lead's stimulation duration in milliseconds. |
| 63 | `LEAD3_STIMULATION_DURATION` | INTEGER |  | Indicates the third lead's stimulation duration in milliseconds. |
| 64 | `LEAD2_DETECTION_THRESHOLD` | NUMERIC |  | Indicates the second lead's detection threshold in millivolts. |
| 65 | `LEAD3_DETECTION_THRESHOLD` | NUMERIC |  | Indicates the third lead's detection threshold in millivolts. |
| 66 | `LEAD1_PULSE_AMPLITUDE` | NUMERIC |  | Indicates the first lead's pulse amplitude in volts. |
| 67 | `LEAD2_PULSE_AMPLITUDE` | NUMERIC |  | Indicates the second lead's pulse amplitude in volts. |
| 68 | `LEAD3_PULSE_AMPLITUDE` | NUMERIC |  | Indicates the third lead's pulse amplitude in volts. |
| 69 | `LEAD1_IMPULSION_DURATION_MS` | INTEGER |  | Indicates the first lead's impulsion duration in milliseconds. |
| 70 | `LEAD2_IMPULSION_DURATION_MS` | INTEGER |  | Indicates the second lead's impulsion duration in milliseconds. |
| 71 | `LEAD3_IMPULSION_DURATION_MS` | INTEGER |  | Indicates the third lead's impulsion duration in milliseconds. |
| 72 | `LEAD1_SENSIBILITY_MV` | NUMERIC |  | Indicates the first lead's sensibility in millivolts. |
| 73 | `LEAD2_SENSIBILITY_MV` | NUMERIC |  | Indicates the second lead's sensibility in millivolts. |
| 74 | `LEAD3_SENSIBILITY_MV` | NUMERIC |  | Indicate the third lead's sensibility in millivolts. |
| 75 | `REASON_FOR_EXTRACT` | VARCHAR |  | Indicates the reason for extract. |
| 76 | `PACEMAKER_IMP_TYPE_C_NAME` | VARCHAR | org | Indicates the type of pacemaker. To document if this is a temporary pacemaker, use item IMP 56210 - TEMPORARY PACEMAKER? instead. |
| 77 | `DEFIBRILLATOR_TYPE_C_NAME` | VARCHAR | org | Indicates the type of defibrillator. |
| 78 | `IMPEDANCE_OF_FIBRILLATION` | NUMERIC |  | Indicates the fibrillation impedance in ohms. |
| 79 | `THERAPY_ZONE_VENT_FIB_AC_YN` | VARCHAR |  | Indicates if the therapy zone for ventricular fibrillation was activated. |
| 80 | `THERAPY_ZONE_VENT_TACHY1_MS` | INTEGER |  | Indicates the therapy zone for the first ventricular tachycardia in milliseconds. |
| 81 | `THERAPY_ZONE_VENT_TACHY1_AC_YN` | VARCHAR |  | Indicates if the therapy zone for the first ventricular tachycardia was activated. |
| 82 | `THERAPY_ZONE_VENT_TACHY2_MS` | INTEGER |  | Indicates the therapy zone for the second ventricular tachycardia in milliseconds. |
| 83 | `THERAPY_ZONE_VENT_TACHY2_AC_YN` | VARCHAR |  | Indicates if the therapy zone for the second ventricular tachycardia was activated. |
| 84 | `THERAPY_ZONE_COMMENT` | VARCHAR |  | Comments on the therapy zone. |
| 85 | `PRESTATION1_C_NAME` | VARCHAR | org | Type of device 1. |
| 86 | `PRESTATION2_C_NAME` | VARCHAR | org | Type of device 2. |
| 87 | `IMP_BATTERY_STATUS` | VARCHAR |  | This column stores the description of the implant's current battery status. |
| 88 | `IMP_REPLACEMENT_DATE` | DATETIME |  | This column stores the recommended replacement date of the implant. |
| 89 | `SYMPTOM_EPISODES_COUNT` | INTEGER |  | This column stores the number of symptom episodes recorded by the implant. |
| 90 | `TACHY_EPISODES_COUNT` | INTEGER |  | This column stores the number of tachyarrhythmia episodes recorded by the implant. |
| 91 | `PAUSE_EPISODES_COUNT` | INTEGER |  | This column stores the number of pause episodes recorded by the implant. |
| 92 | `BRADY_EPISODES_COUNT` | INTEGER |  | This column stores the number of brady episodes recorded by the implant. |
| 93 | `ATRIAL_TACHY_EPISODES_COUNT` | INTEGER |  | This column stores the number of number of atrial tachyarrhythmias recorded by the implant. |
| 94 | `AFIB_EPISODES_COUNT` | INTEGER |  | This column stores the number of number of atrial fibrillations recorded by the implant. |
| 95 | `PERCENTAGE_TIME_AFIB` | NUMERIC |  | This column stores the number of percentage of time in atrial fibrillation recorded by the implant. |
| 96 | `PACE_ICD_AV_DELAY_COMMENT` | VARCHAR |  | Comment to describe the AV delay of the pacemaker. |
| 97 | `PACEMAKER_POCKET_LOC_CMT` | VARCHAR |  | Comment to describe the pocket location of the pacemaker. |
| 98 | `DFT_CHARGE_TIME_SEC` | NUMERIC |  | Indicates the charge time of the DFT energy in seconds. |
| 99 | `DFT_PERFORMED_YN` | VARCHAR |  | Indicates whether a DFT was performed. |
| 100 | `DFT_HIGH_VOLTAGE_IMPEDANCE_OHM` | INTEGER |  | Indicates the DFT high voltage impedance in Ohms. |
| 101 | `DFT_SUCCESSFUL_YN` | VARCHAR |  | Indicates if the DFT was successful. |
| 102 | `LEAD_REMOVAL_METHOD_C_NAME` | VARCHAR | org | This item stores the method in which the lead was removed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

