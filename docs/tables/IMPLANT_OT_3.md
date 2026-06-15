# IMPLANT_OT_3

> This table contains implant information that changes over time.

**Overflow of:** [IMPLANT_OT](IMPLANT_OT.md)  
**Primary key:** `IMPLANT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 39  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the implant record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `PCMKR_PACE_MODE_CMT` | VARCHAR |  | Free text comment on the pacing mode of an implanted pacemaker |
| 4 | `PCMKR_PV_DELAY_MS` | INTEGER |  | P-V delay in milliseconds |
| 5 | `PCMKR_AV_DELAY_MS` | INTEGER |  | A-V delay in milliseconds |
| 6 | `PCMKR_LV_EARLY_YN` | VARCHAR |  | Indicate if the left ventricle contraction was early |
| 7 | `PCMKR_RV_EARLY_YN` | VARCHAR |  | Indicate if the right ventricle contraction was early |
| 8 | `PCMKR_VV_DELAY` | INTEGER |  | V-V delay in milliseconds |
| 9 | `PCMKR_VV_DELAY_CMT` | VARCHAR |  | Free text comment on the V-V delay |
| 10 | `PCMKR_HYST_C_NAME` | VARCHAR | org | Indicate if hysteresis is active |
| 11 | `PCMKR_HYST_CMT` | VARCHAR |  | Free text comment on hysteresis |
| 12 | `PCMKR_HYST_A_RATE` | INTEGER |  | Indicate the atrial rate for hysteresis |
| 13 | `PCMKR_HYST_RATE_C_NAME` | VARCHAR |  | Indicate the rate-drop for hysteresis |
| 14 | `PCMKR_HYST_RATE_CMT` | VARCHAR |  | Free text comment on rate-drop hysteresis |
| 15 | `PCMKR_GEN_PACE_CMT` | VARCHAR |  | Free text comment on pacing parameters |
| 16 | `PCMKR_RV_SENSE_C_NAME` | VARCHAR | org | Indicate the sensing polarity of the RV lead |
| 17 | `PCMKR_ATR_SENSE_C_NAME` | VARCHAR |  | Indicate the sensing polarity of the atrial lead |
| 18 | `PCMKR_LV_SENSE_C_NAME` | VARCHAR |  | Indicate the sensing polarity of the LV lead |
| 19 | `PCMKR_RV_PACE_C_NAME` | VARCHAR |  | Indicate the pacing polarity of the RV lead |
| 20 | `PCMKR_ATR_PACE_C_NAME` | VARCHAR |  | Indicate the pacing polarity of the atrial lead |
| 21 | `PCMKR_LV_PACE_C_NAME` | VARCHAR |  | Indicate the pacing polarity of the LV lead |
| 22 | `PCMKR_POLARITY_CMT` | VARCHAR |  | Free text comment on lead polarities |
| 23 | `PCMKR_PR_AMPLITUDE` | INTEGER |  | Indicate the amplitude of the P/R wave in millivolts |
| 24 | `PCMKR_MODE_SWTCH_C_NAME` | VARCHAR |  | Indicate if mode switching is active |
| 25 | `PCMKR_MD_SWTCH_CMT` | VARCHAR |  | Free text comment on mode switching |
| 26 | `PCMKR_A_RATE_SWTCH` | INTEGER |  | Indicate the atrial rate for mode switching |
| 27 | `DENT_PLATFRM_SIZE_C_NAME` | VARCHAR |  | Dental implant platform size. |
| 28 | `DENT_DRILL_PROT_C_NAME` | VARCHAR |  | Dental implant drill protocol. |
| 29 | `DENT_CONNECT_TYPE_C_NAME` | VARCHAR |  | Dental implant connection type. |
| 30 | `DENT_COLLAR_SURF_C_NAME` | VARCHAR |  | Dental implant collar surface. |
| 31 | `DENT_IMP_TAPER_C_NAME` | VARCHAR |  | Dental implant taper. |
| 32 | `DENT_DIAMETER` | INTEGER |  | Dental implant diameter. |
| 33 | `DENT_IMP_INS_TORQUE` | INTEGER |  | Dental implant insertion torque. |
| 34 | `DENT_IMP_SITE_RECORD_ID` | NUMERIC |  | Dental implant site. |
| 35 | `DENT_IMP_SITE_RECORD_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 36 | `DENT_IMP_CODE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 37 | `DENT_IMP_BILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 38 | `DENT_IMP_AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 39 | `DENT_GUIDE_USED_YN` | VARCHAR |  | Stores whether a guide was used to place a dental implant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

