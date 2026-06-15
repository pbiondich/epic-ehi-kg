# OB_HSB_DELIVERY

> This table contains information about the delivery for this pregnancy, as entered in Stork's Delivery Summary activity.

**Overflow family:** [OB_HSB_DELIVERY_2](OB_HSB_DELIVERY_2.md)  
**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 80  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID assigned to the episode record (HSB .1). |
| 2 | `OB_DEL_2ND_STAGE_HR` | INTEGER |  | This column stores the length of the second stage of labor in number of hours. |
| 3 | `OB_DEL_1ST_STAGE_HR` | INTEGER |  | This column stores the length of the first stage of labor in number of hours. |
| 4 | `OB_DEL_1ST_STAGE_M` | INTEGER |  | This column stores the length of the first stage of labor in the number of minutes, and is added to OB_DEL_1ST_STAGE_HR to produce the total time. |
| 5 | `OB_DEL_2ND_STAGE_M` | INTEGER |  | This column stores the length of the second stage of labor in the number of minutes, and is added to OB_DEL_2ND_STAGE_HR to produce the total time. |
| 6 | `OB_DEL_3RD_STAGE_M` | INTEGER |  | This column stores the length of the third stage of labor in the number of minutes, and is added to OB_DEL_3RD_STAGE_HR to produce the total time. |
| 7 | `OB_DEL_BLOOD_LOSS` | INTEGER |  | Stores the amount of blood lost in the delivery, in milliliters. |
| 8 | `OB_DEL_COMPL_CMT` | VARCHAR |  | Stores the comments for any complications associated with this delivery. |
| 9 | `OB_DEL_REP_PACKETS` | INTEGER |  | Stores the number of suture packets used on a patient during laceration/episiotomy repair from delivery. |
| 10 | `OB_DELIVERY_DATE` | DATETIME |  | This item holds the date when this pregnancy was completed. This is the latest date of delivery of all the newborns associated with the pregnancy. This column should not be used to determine the birth date of the baby. |
| 11 | `OB_DEL_3RD_STAGE_HR` | INTEGER |  | This column stores the length of the third stage of labor in number of hours. |
| 12 | `OB_DEL_CRV_RPE_DTTM` | DATETIME (Local) |  | Stores the date and time when cervical ripening occurred. |
| 13 | `OB_DEL_DIL_CMP_DTTM` | DATETIME (Local) |  | Stores the date and time that dilation was complete and/or the mother entered the second stage of labor for this pregnancy. |
| 14 | `OB_DEL_ONSET_DTTM` | DATETIME (Local) |  | Stores the date and time that labor began for this pregnancy. |
| 15 | `OB_DEL_PRES_REF_C_NAME` | VARCHAR | org | Stores the presentation reference point category number for the delivery. The data for this column are entered in the Delivery Summary activity and stored in the delivery records. |
| 16 | `OB_DEL_PRES_LR_C_NAME` | VARCHAR | org | Stores the laterality of presentation (left-right) category number for the delivery. Data for this column are entered in the Delivery Summary activity and stored in the delivery records. |
| 17 | `OB_DEL_PRES_AP_C_NAME` | VARCHAR | org | Stores the anterior or posterior position of presentation category number. The data for this column are entered in the Delivery Summary activity and stored in the delivery records. |
| 18 | `OB_DEL_CHEST_CIRC` | NUMERIC |  | Stores the baby's chest circumference measurement at birth, in inches. |
| 19 | `OB_DEL_ANALGES_CMNT` | VARCHAR |  | Stores the analgesia comments recorded in the Delivery Summary. This information is stored in the delivery records. |
| 20 | `OB_DEL_PLCENTA_DTTM` | DATETIME (UTC) |  | Stores the date and time the placenta was delivered. This data is stored in UTC time rather than local time. You may need to convert this data for display in reports. For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.OB_DEL_PLCENTA_LOC_DTTM. |
| 21 | `OB_DEL_DELIV_MD_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `OB_DEL_APGAR_SK_1_C_NAME` | VARCHAR | org | Stores the baby's skin color Apgar score at one minute after birth. This information is stored in the delivery records. |
| 23 | `OB_DEL_APGAR_SK_5_C_NAME` | VARCHAR |  | Stores the baby's skin color Apgar score at five minutes after birth. This information is stored in the delivery records. |
| 24 | `OB_DEL_APGAR_SK10_C_NAME` | VARCHAR |  | Stores the baby's skin color Apgar score at ten minutes after birth. This information is stored in the delivery records. |
| 25 | `OB_DEL_APGAR_HR_1_C_NAME` | VARCHAR |  | Stores the baby's heart rate Apgar score at one minute after birth. This information is stored in the delivery records. |
| 26 | `OB_DEL_APGAR_HR_5_C_NAME` | VARCHAR |  | Stores the baby's heart rate Apgar score at five minutes after birth. This information is stored in the delivery records. |
| 27 | `OB_DEL_APGAR_HR10_C_NAME` | VARCHAR |  | Stores the baby's heart rate Apgar score at ten minutes after birth. This information is stored in the delivery records. |
| 28 | `OB_DEL_APGAR_GR_1_C_NAME` | VARCHAR |  | Stores the baby's grimace Apgar score at one minute after birth. This information is stored in the delivery records. |
| 29 | `OB_DEL_APGAR_GR_5_C_NAME` | VARCHAR |  | Stores the baby's grimace Apgar score at five minutes after birth. This information is stored in the delivery records. |
| 30 | `OB_DEL_APGAR_GR10_C_NAME` | VARCHAR |  | Stores the baby's grimace Apgar score at ten minutes after birth. This information is stored in the delivery records. |
| 31 | `OB_DEL_APGAR_MU_1_C_NAME` | VARCHAR |  | Stores the baby's muscle tone Apgar score at one minute after birth. This information is stored in the delivery records. |
| 32 | `OB_DEL_APGAR_MU_5_C_NAME` | VARCHAR |  | Stores the baby's muscle tone Apgar score at five minutes after birth. This information is stored in the delivery records. |
| 33 | `OB_DEL_APGAR_MU10_C_NAME` | VARCHAR |  | Stores the baby's muscle tone Apgar score at ten minutes after birth. This information is stored in the delivery records. |
| 34 | `OB_DEL_APGAR_BR_1_C_NAME` | VARCHAR |  | Stores the baby's breathing Apgar score at one minute after birth. This information is stored in the delivery records. |
| 35 | `OB_DEL_APGAR_BR_5_C_NAME` | VARCHAR |  | Stores the baby's breathing Apgar score at five minutes after birth. This information is stored in the delivery records. |
| 36 | `OB_DEL_APGAR_BR10_C_NAME` | VARCHAR |  | Stores the baby's breathing Apgar score at ten minutes after birth. This information is stored in the delivery records. |
| 37 | `OB_DEL_BIRTH_LENGTH` | NUMERIC |  | Stores the infant's length at birth, in inches. |
| 38 | `OB_DEL_BIRTH_WT` | NUMERIC |  | Stores the infant's weight at birth in ounces. |
| 39 | `OB_DEL_HEAD_CIRCUM` | NUMERIC |  | Stores the infant's head circumference at birth, in inches. This information is entered in the Delivery Summary activity and is stored in the delivery records. |
| 40 | `OB_DEL_APGAR_1_C_NAME` | VARCHAR | org | Stores the baby's total Apgar score at one minute after birth. This information is stored in the delivery records. |
| 41 | `OB_DEL_APGAR_5_C_NAME` | VARCHAR |  | Stores the baby's total Apgar score at five minutes after birth. This information is stored in the delivery records. |
| 42 | `OB_DEL_APGAR_10_C_NAME` | VARCHAR |  | Stores the baby's total Apgar score at ten minutes after birth. This information is stored in the delivery records. |
| 43 | `OB_DEL_DELIV_METH_C_NAME` | VARCHAR | org | Stores the delivery method at birth. The data for this column are entered in the Delivery Summary activity and stored in the delivery records. |
| 44 | `OB_DEL_ANOMALIES` | VARCHAR |  | Stores the observed fetal anomalies. This information is stored in the delivery records. |
| 45 | `OB_DEL_BIRTH_DTTM` | DATETIME (UTC) |  | Stores the date and time of delivery for a delivery record. For values that are not fully confident (for example, if just the year was documented), the confidence is stored in the OB_HX_OUTC_FUZZY_C column. For those values, this column contains the UTC representation of midnight on the earliest date that the value could represent, relative to the time zone where the delivery was documented. This data is stored in UTC time rather than local time. You may need to convert this data for display in reports. For deliveries documented in the Delivery Summary, the local time can be found in PATIENT.BIRTH_DATE. |
| 46 | `OB_DEL_DEPT_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 47 | `PUSHING_START_DTTM` | DATETIME (UTC) |  | The instant when the mother starts to push for the first time. This data is stored in UTC time rather than local time. You may need to convert this data for display in reports. For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.PUSHING_START_LOC_DTTM. |
| 48 | `ROM_TO_DELIVER` | INTEGER |  | This item displays the amount of time (in seconds) from rupture of membranes until the patient delivers. For pregnancy episodes, if there are multiples, it will calculate the length of time from the earliest rupture instant documented on a delivery record through to the latest delivery instant. |
| 49 | `OB_DEL_STEROIDS_C_NAME` | VARCHAR |  | This column displays whether the mother received steroids for fetal lung maturation prior to delivery. This column links to the category table ZC_OB_DEL_STEROIDS. The column is looking for documentation in the Delivery Summary. |
| 50 | `MOTHER_ANTIBIO_YN` | VARCHAR |  | This column displays 'Y' or 'N' depending on whether or not the mother received antibiotics during labor. The column is looking for documentation in the Delivery Summary. |
| 51 | `FORCEPS_DEL_ATT_YN` | VARCHAR |  | This column displays 'Y' or 'N' depending on whether or not a forceps delivery was attempted during this labor. The column is looking for documentation in the Delivery Summary. |
| 52 | `VACUUM_DEL_ATT_YN` | VARCHAR |  | This column displays 'Y' or 'N' depending on whether or not a vacuum delivery was attempted during this labor. The column is looking for documentation in the Delivery Summary. |
| 53 | `LABOR_ATTEMPT_YN` | VARCHAR |  | This column displays 'Y' or 'N' depending on whether or not a trial of labor was attempted. This can apply to both vaginal and c-section deliveries. The column is looking for documentation in the Delivery Summary. |
| 54 | `OB_DEL_APGAR_15_C_NAME` | VARCHAR |  | Stores the baby's total Apgar score at fifteen minutes after birth. This information is stored in the delivery records. |
| 55 | `OB_DEL_APGAR_20_C_NAME` | VARCHAR |  | Stores the baby's total Apgar score at twenty minutes after birth. This information is stored in the delivery records. |
| 56 | `OB_DEL_APGAR_SK15_C_NAME` | VARCHAR |  | Stores the baby's skin color Apgar score at fifteen minutes after birth. This information is stored in the delivery records. |
| 57 | `OB_DEL_APGAR_HR15_C_NAME` | VARCHAR |  | Stores the baby's heart rate Apgar score at fifteen minutes after birth. This information is stored in the delivery records. |
| 58 | `OB_DEL_APGAR_GR15_C_NAME` | VARCHAR |  | Stores the baby's grimace Apgar score at fifteen minutes after birth. This information is stored in the delivery records. |
| 59 | `OB_DEL_APGAR_MU15_C_NAME` | VARCHAR |  | Stores the baby's muscle tone Apgar score at fifteen minutes after birth. This information is stored in the delivery records. |
| 60 | `OB_DEL_APGAR_BR15_C_NAME` | VARCHAR |  | Stores the baby's breathing Apgar score at fifteen minutes after birth. This information is stored in the delivery records. |
| 61 | `OB_DEL_APGAR_SK20_C_NAME` | VARCHAR |  | Stores the baby's skin color Apgar score at twenty minutes after birth. This information is stored in the delivery records. |
| 62 | `OB_DEL_APGAR_HR20_C_NAME` | VARCHAR |  | Stores the baby's heart rate Apgar score at twenty minutes after birth. This information is stored in the delivery records. |
| 63 | `OB_DEL_APGAR_GR20_C_NAME` | VARCHAR |  | Stores the baby's grimace Apgar score at twenty minutes after birth. This information is stored in the delivery records. |
| 64 | `OB_DEL_APGAR_MU20_C_NAME` | VARCHAR |  | Stores the baby's muscle tone Apgar score at twenty minutes after birth. This information is stored in the delivery records. |
| 65 | `OB_DEL_APGAR_BR20_C_NAME` | VARCHAR |  | Stores the baby's breathing Apgar score at twenty minutes after birth. This information is stored in the delivery records. |
| 66 | `OB_HX_GEST_AGE` | INTEGER |  | Stores the pregnancy gestational age (GA) in days for an outcome in OB history. |
| 67 | `OB_HX_DEL_SITE_C_NAME` | VARCHAR | org | Stores the delivery site for an outcome in OB history. |
| 68 | `OB_HX_CLINICIAN_FT` | VARCHAR |  | Stores the delivering clinician for an outcome in OB history. This is free text. |
| 69 | `OB_HX_INFANT_SEX_C_NAME` | VARCHAR | org | Stores the sex of the baby. |
| 70 | `OB_HX_OUTC_FUZZY_C_NAME` | VARCHAR |  | This item stores the confidence of the outcome date in OB_DEL_BIRTH_DTTM. If anything less than a full date and time was documented for the outcome date (for example, if just the year was documented), this column indicates how granular the documented value was. |
| 71 | `OB_HX_OUTCOME_C_NAME` | VARCHAR |  | Stores the outcome type for an outcome documented in OB history for a patient. |
| 72 | `CONT_START_PAT_DTTM` | DATETIME (Local) |  | This column stores the date and time the contractions started according to the patient. |
| 73 | `DILATION_START_DTTM` | DATETIME (Local) |  | This column stores the date and time that active dilation started for the patient. |
| 74 | `SKIN_TO_SKIN_DTTM` | DATETIME (Local) |  | Stores the date and time that skin to skin with the baby was initiated. |
| 75 | `CORD_CLAMP_DTTM` | DATETIME (UTC) |  | This column stores the instant the umbilical cord was clamped. For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.CORD_CLAMP_LOC_DTTM. |
| 76 | `INDUCTION_DTTM` | DATETIME (Local) |  | This column stores date and time of induction for delivery. |
| 77 | `DECISION_DTTM` | DATETIME (UTC) |  | This column stores the instant the decision was made for an emergent c-section. For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.DECISION_LOC_DTTM. |
| 78 | `BREAST_FEED_ST_DTTM` | DATETIME (UTC) |  | This column stores the instant that breastfeeding was initiated. For deliveries documented in the Delivery Summary, the local time can be found in OB_HSB_DELIVERY_2.BREAST_FEED_ST_LOC_DTTM. |
| 79 | `SKIN_TO_SKIN_END_DTTM` | DATETIME (Local) |  | Stores the date that skin to skin was completed. |
| 80 | `ABDOMINAL_GIRTH` | NUMERIC |  | The measurement of the baby's abdominal girth. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

