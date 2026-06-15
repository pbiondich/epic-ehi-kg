# IMPLANT_OT

> This table contains implant information that changes over time.

**Overflow family:** [IMPLANT_OT_2](IMPLANT_OT_2.md), [IMPLANT_OT_3](IMPLANT_OT_3.md)  
**Primary key:** `IMPLANT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 96  
**Org-specific columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_NUMBER` | INTEGER |  | The contact number of the implant record. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `LINKED_ORDER_ID` | NUMERIC |  | A link to the order record with relevant information for the implant on a contact (e.g. the interrogation report for a pacemaker). |
| 7 | `PACE_MODE_C_NAME` | VARCHAR | org | The category ID for the pacing mode of an implanted pacemaker. |
| 8 | `PACE_LOW_RATE` | INTEGER |  | A pacemaker's lower pacing rate. |
| 9 | `PACE_UPPER_RATE` | INTEGER |  | A pacemaker's upper pacing rate. |
| 10 | `PACE_VT_RATE` | INTEGER |  | The VT detection rate of an implanted pacemaker. |
| 11 | `PACE_VF_RATE` | INTEGER |  | The VF detection rate of an implanted pacemaker. |
| 12 | `PACE_LEAD_SECURE_C_NAME` | VARCHAR | org | The category ID for the method used to secure the leads to the pacemaker. |
| 13 | `LEAD_SENSE_MV` | NUMERIC |  | The sensing threshold of the lead in mV. |
| 14 | `LEAD_LOC_C_NAME` | VARCHAR | org | The category ID for the anatomical location of the lead. |
| 15 | `LEAD_CAPTURE_V` | NUMERIC |  | The capture threshold of the lead in V. |
| 16 | `LEAD_CAPTURE_MA` | NUMERIC |  | The capture threshold of the lead in mA. |
| 17 | `LEAD_PACING_OHM` | INTEGER |  | The pacing impedance of the lead in Ohms. |
| 18 | `LEAD_SLEW_RATE` | INTEGER |  | The slew rate of the lead. |
| 19 | `LEAD_EXTRACT_RES_C_NAME` | VARCHAR | org | The category ID for the result of extracting the lead. |
| 20 | `ICD_HIGH_VOLT_OHMS` | INTEGER |  | The high voltage impedance of the ICD in Ohms. |
| 21 | `CNCT_LOG_ID` | VARCHAR |  | The log where this specific contact on the implant was used. For example, if an implant was implanted in log 100, this will contain the value 100 for that contact. If it is then adjusted in another log, that contact will point to that log. |
| 22 | `ICD_BATT_VOLT_V` | NUMERIC |  | Records the battery voltage of a generator in volts. |
| 23 | `PACE_FAST_VT_RATE` | INTEGER |  | The Fast VT detection rate of an implanted pacemaker. |
| 24 | `LEAD_SHOCK_OHM` | INTEGER |  | The shock impedance of the lead in Ohms. |
| 25 | `CNCT_SURGERY_CSN_ID` | NUMERIC |  | The Contact Serial Number (CSN) of the log where this specific contact on the implant was used. For example, if an implant was implanted in log 100 having CSN 120, this will contain the value 120 for that contact. If it is then adjusted in another log, that contact will point to the CSN of that log. |
| 26 | `STATUS_C_NAME` | VARCHAR | org | The category ID for the implant status as of a given contact. |
| 27 | `REASON_EVAL` | VARCHAR |  | Reason why device is being evaluated. Potential reasons would include: pre-op eval, post-op eval |
| 28 | `ICD_PRESENT_RHYTH_C_NAME` | VARCHAR | org | The category ID for the ICD behavior prior to making adjustments. |
| 29 | `ICD_UNDERLY_RHYTHM` | VARCHAR |  | Stores free text documenting underlying rhythm. |
| 30 | `ICD_MNTR_OFF_PROC_C_NAME` | VARCHAR | org | The category ID for the ICD monitoring status for procedure. |
| 31 | `ICD_VOLT_CMT` | VARCHAR |  | Free text comment to document comments regarding the voltage setting for the ICD. |
| 32 | `ICD_CHARGE_TIME` | NUMERIC |  | Numeric value of time in seconds it takes for device to charge to full power. |
| 33 | `LEAD_PSA_WAVE` | NUMERIC |  | Numeric measurement through lead when not attached to the device. |
| 34 | `LEAD_PSA_THRESH` | NUMERIC |  | Numeric measurement of the threshold through lead when not attached to the device. |
| 35 | `LEAD_PSA_DEVICE_WAV` | NUMERIC |  | Numeric measurement of the Lead through the device connection |
| 36 | `LEAD_P_WAVE` | NUMERIC |  | Numeric value associated with lead for the P wave when connected to the device. |
| 37 | `LEAD_P_WAVE_CMT` | VARCHAR |  | Free-text comment associated with Lead P Wave. |
| 38 | `LEAD_R_WAVE` | NUMERIC |  | Numeric value associated with lead for the R wave when connected to the device. |
| 39 | `LEAD_R_WAVE_CMT` | VARCHAR |  | Free-text comment associated with Lead R Wave. |
| 40 | `ICD_MODE_SWITCH` | NUMERIC |  | Stores the mode switch parameter of ICD |
| 41 | `ICD_MODE_SWTCH_CMT` | VARCHAR |  | Free-text comment associated with ICD Mode Switch value. |
| 42 | `ICD_V_TACH_THERAPY` | VARCHAR |  | Stores programmed therapies to treat potentially fatal rhythms |
| 43 | `ICD_FST_V_TCH_THERA` | VARCHAR |  | Summary of programmed therapies to treat potentially fatal rhythms in a rate zone. |
| 44 | `ICD_V_TACH_MONT_ZON` | NUMERIC |  | Detection rate for device to record arrhythmia |
| 45 | `ICD_V_FIB_THERAPIES` | VARCHAR |  | Summary of programmed therapies to treat potentially fatal rhythms in this rate zone |
| 46 | `ICD_PARAMETER_CMT` | VARCHAR |  | Stores the comment for ICD parameters |
| 47 | `LEAD_PSA_CAP_THRESH` | NUMERIC |  | Stores the test for lead functionality separate from the device |
| 48 | `PSA_CURRENT` | NUMERIC |  | Stores the test for lead current separate from device |
| 49 | `P_WAVE_CMT` | VARCHAR |  | Comments for non-numeric P wave documentation |
| 50 | `R_WAVE_CMT` | VARCHAR |  | Comments for non-numeric R wave documentation |
| 51 | `THRESHOLD_CMT` | VARCHAR |  | Stores the comments for non-numeric documentation for threshold testing |
| 52 | `LEAD_CAPTURE_MS` | NUMERIC |  | The capture threshold of the lead in ms. |
| 53 | `LEAD_ACCESS_LOC_C_NAME` | VARCHAR | org | The category ID for the vein accessed for lead implant. |
| 54 | `ICD_MONITOROFF_C_NAME` | VARCHAR | org | The category ID that indicates if the device was turned off for comfort of care. |
| 55 | `ICD_EVENT_DT` | DATETIME |  | The date of an event or therapy delivered by the device. |
| 56 | `ICD_EVENTDELIV_C_NAME` | VARCHAR | org | The category ID for the events/therapy that the ICD device delivered. |
| 57 | `NUM_ATP` | INTEGER |  | Number of ATPs. |
| 58 | `NUM_SHOCK` | INTEGER |  | Number of shocks. |
| 59 | `RHYTHM_C_NAME` | VARCHAR | org | The category ID for the rhythm that the device attempted to correct. |
| 60 | `APPROP_THERAPY_YN` | VARCHAR |  | Indicates if the therapy was appropriate. |
| 61 | `ATRIAL_IMPD` | INTEGER |  | Atrial impedance in ohms. |
| 62 | `RV_IMPD` | INTEGER |  | Right ventricle impedance in ohms. |
| 63 | `LV_IMPD` | INTEGER |  | LV impedance in ohms. |
| 64 | `RV_COIL_IMPD` | INTEGER |  | Right ventricle coil impedance in ohms. |
| 65 | `SVC_COIL_IMPD` | INTEGER |  | SVC coil impedance in ohms. |
| 66 | `ICD_SWITCH_PERC` | NUMERIC |  | Mode switch percentage. |
| 67 | `DFT_ENERGY` | INTEGER |  | Minimum Defibrillation Threshold (DFT) energy in Joules. |
| 68 | `AS_VS` | NUMERIC |  | AS-VS percentage paced. |
| 69 | `AS_VP` | NUMERIC |  | AS-VP percentage paced. |
| 70 | `AP_VP` | NUMERIC |  | AP-VP percentage paced. |
| 71 | `AP_VS` | NUMERIC |  | AP-VS percentage paced. |
| 72 | `VSR` | NUMERIC |  | VSR percentage paced. |
| 73 | `BIV_PACED` | NUMERIC |  | Bi-ventricular paced percentage. |
| 74 | `VENT_PACED` | NUMERIC |  | Ventricular paced percentage. |
| 75 | `VENT_SENSE` | NUMERIC |  | Ventricular sense. |
| 76 | `LV_PACED` | NUMERIC |  | LV paced percentage. |
| 77 | `LEAD_DIAM` | INTEGER |  | Diameter of lead. |
| 78 | `LEAD_LENGTH` | INTEGER |  | Length of lead. |
| 79 | `MAGNET_RATE` | NUMERIC |  | Stores the pacemaker magnet rate |
| 80 | `REASON_PLACEMENT_C_NAME` | VARCHAR | org | The category ID for the reason for the placement of an implant. |
| 81 | `PROGRAMMABLE_YN` | VARCHAR |  | Indicates whether the implant is programmable. |
| 82 | `NONPROG_SETTINGS_C_NAME` | VARCHAR | org | The category ID for the settings of a non-programmable implant. |
| 83 | `SHUNT_SETTINGS_C_NAME` | VARCHAR | org | The category ID for the settings related to a shunt. |
| 84 | `DIAPHRAGMATIC_CAP_V` | NUMERIC |  | The diaphragmatic capture threshold of the lead in V. |
| 85 | `MATERIAL_C_NAME` | VARCHAR | org | The category ID for the type of breast implant material or lumen type, populated via SmartForm, when describing an implant. |
| 86 | `LOCATION_C_NAME` | VARCHAR | org | The category ID for the breast implant location, populated via SmartForm, when describing an implant. |
| 87 | `CONTOUR_C_NAME` | VARCHAR | org | The category ID for the breast implant contour, populated via SmartForm, when describing an implant. |
| 88 | `RADIAL_FOLDS_YN` | VARCHAR |  | Indicates whether there is an intracapsular radial folds silicone finding for a breast implant. This is populated via SmartForm (R LQF 52002) and is a non-defaulted, unrequired field. |
| 89 | `SUBCAPSULAR_LINE_YN` | VARCHAR |  | Indicates whether there is an intracapsular subcapsular line silicone finding for a breast implant. This is populated via SmartForm (R LQF 52002) and is a non-defaulted, unrequired field. |
| 90 | `LINGUINE_SIGN_YN` | VARCHAR |  | Indicates whether there is an intracapsular linguine sign silicone finding for a breast implant. This is populated via SmartForm (R LQF 52002) and is a non-defaulted, unrequired field. |
| 91 | `EXTRACAPSULAR_SILICONE_C_NAME` | VARCHAR | org | The category ID for the breast implant extracapsular silicone findings, populated via SmartForm, when describing an implant. |
| 92 | `WATER_DROPLETS_C_NAME` | VARCHAR | org | The category ID for the flag describing the presence of water droplets associated with breast implants. This is populated via SmartForm when describing an implant. |
| 93 | `PERI_IMP_FLUID_C_NAME` | VARCHAR |  | The category ID for the flag describing the presence of peri-implant fluid associated with breast implants. This is populated via SmartForm when describing an implant. |
| 94 | `KEYHOLE_SIGN_YN` | VARCHAR |  | Indicates whether there is an intracapsular keyhole sign silicone finding for a breast implant. This is populated via SmartForm (R LQF 52002) and is a non-defaulted, unrequired field. |
| 95 | `GUDID_MRI_SAFETY_INFO` | VARCHAR |  | This column stores the MRI safety information obtained from the Global Unique Device Identification Database (GUDID) for an implant. |
| 96 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | This item stores the Contact Serial Number (CSN) of the patient encounter where this specific contact on the implant was created. For example, for an implant was edited in an office visit encounter with CSN 120, this item will contain a value of 120 for that contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

