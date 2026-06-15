# TXP_ORGAN_DONOR

> Transplant organ donor information.

**Primary key:** `DONOR_ID`  
**Columns:** 52  
**Org-specific columns:** 7  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DONOR_ID` | NUMERIC | PK | The organ donor record id. |
| 2 | `DONOR_UNOS_ID` | VARCHAR |  | The organ donor's UNOS ID. |
| 3 | `DONOR_ABO_C_NAME` | VARCHAR |  | The organ donor's blood type. |
| 4 | `BIRTH_DATE` | DATETIME |  | The organ donor's date of birth. |
| 5 | `DEATH_DATE` | DATETIME |  | The organ donor's date of death. |
| 6 | `AGE` | NUMERIC |  | The organ donor's age at death. |
| 7 | `SEX_C_NAME` | VARCHAR | org | The organ donor's gender. |
| 8 | `HEIGHT_INCHES` | NUMERIC |  | The organ donor's height in inches. |
| 9 | `WEIGHT_OZ` | NUMERIC |  | The organ donor's weight in ounces. |
| 10 | `ETHNIC_GROUP_C_NAME` | VARCHAR | org | The organ donor's ethnic group. |
| 11 | `HAD_HYPERTENSION_C_NAME` | VARCHAR |  | Specifies whether the organ donor had hypertension. |
| 12 | `HYPERTENSION_YEARS` | INTEGER |  | Specifies the number of years the organ donor had hypertension. |
| 13 | `HAD_DIABETES_C_NAME` | VARCHAR |  | Specifies whether the organ donor had diabetes. |
| 14 | `DIABETES_YEARS` | INTEGER |  | Specifies the number of years the organ donor had diabetes. |
| 15 | `HAD_CANCER_C_NAME` | VARCHAR |  | Specifies whether the organ donor had cancer. |
| 16 | `TOBACCO_USE_C_NAME` | VARCHAR |  | Specifies the organ donor's use of tobacco. |
| 17 | `TOBACCO_QUIT_DATE` | DATETIME |  | Specifies the date the organ donor quit using tobacco. |
| 18 | `TOBACCO_PACKS_PER_DAY` | INTEGER |  | Specifies the organ donor's tobacco use in packs per day. |
| 19 | `TOBACCO_YEARS` | INTEGER |  | Specifies the number of years the organ donor used tobacco. |
| 20 | `TOBACCO_COMMENT` | VARCHAR |  | Specifies comments about organ donor's use of tobacco. |
| 21 | `ALCOHOL_USE_C_NAME` | VARCHAR |  | Specifies the organ donor's use of alcohol. |
| 22 | `ALCOHOL_OZ_PER_WEEK` | NUMERIC |  | Specifies the organ donor's alcohol consumption in ounces per week. |
| 23 | `ALCOHOL_COMMENT` | VARCHAR |  | Specifies comments about organ donor's use of alcohol. |
| 24 | `DRUG_USE_C_NAME` | VARCHAR |  | Specifies organ donor's illicit use of drugs. |
| 25 | `DRUG_COMMENTS` | VARCHAR |  | Specifies comments about organ donor's illicit use of drugs. |
| 26 | `DEATH_CAUSE_C_NAME` | VARCHAR | org | Specifies the cause of death of organ donor. |
| 27 | `DEATH_CAUSE_OTHER` | VARCHAR |  | Specifies cause of death of organ donor (free text). |
| 28 | `RISK_PERCENTAGE` | INTEGER |  | The kidney donor's risk profile percentage. |
| 29 | `DONOR_TYPE_C_NAME` | VARCHAR | org | Specifies organ donor type. |
| 30 | `DONOR_CLASS_C_NAME` | VARCHAR | org | Specifies organ donor class. |
| 31 | `CDC_HIGH_RISK_YN` | VARCHAR |  | Specifies whether the donor has risk factors for blood-borne disease transmission. |
| 32 | `OPO_HIGH_RISK_YN` | VARCHAR |  | Specifies whether the donor is qualified as a OPO high risk donor. |
| 33 | `HOSPITAL_DAYS` | NUMERIC |  | Specifies the number of days the donor was admitted before death. |
| 34 | `ICU_DAYS` | NUMERIC |  | Specifies the number of days the donor was in ICU before death. |
| 35 | `GIVEN_CPR_C_NAME` | VARCHAR |  | Specifies whether CPR was performed on the donor before death. |
| 36 | `CPR_DUR_MINUTES` | INTEGER |  | Specifies the number of minutes CPR was performed on the donor before death. |
| 37 | `DOB_ESTIMATED_C_NAME` | VARCHAR |  | Specifies whether the donor's date of birth was estimated. |
| 38 | `GIVEN_PRESSOR_C_NAME` | VARCHAR |  | Specifies whether pressors were given to the donor. |
| 39 | `GIVEN_PITRESSIN_C_NAME` | VARCHAR |  | Specifies whether the donor was given Pitressin. |
| 40 | `LOWEST_SYSTOLIC_BP` | INTEGER |  | Specifies the donor's lowest systolic value of blood pressure. |
| 41 | `LOWEST_DIASTOLIC_BP` | INTEGER |  | Specifies the donor's lowest diastolic value of blood pressure. |
| 42 | `BP_LOW_DURATION` | VARCHAR |  | Specifies the length in time the donor experienced the lowest recorded blood pressure. |
| 43 | `URINE_MEASURED_C_NAME` | VARCHAR |  | Specifies whether the donor's urine output was measured. |
| 44 | `URINE_AVERAGE_VOLUME` | INTEGER |  | Specifies the donor's average urine output volume in mL. |
| 45 | `URINE_LAST_HOUR_VOLUME` | INTEGER |  | Specifies the donor's urine output volume in mL for the last hour before death. |
| 46 | `URINE_TOTAL_VOLUME` | INTEGER |  | Specifies the donor's total urine output volume in mL. |
| 47 | `DONOR_OPO_C_NAME` | VARCHAR | org | The organ procurement organization where the donor organ was recovered. |
| 48 | `DNR_RECOVERY_FAC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 49 | `DNR_RECOV_FAC_OTHER` | VARCHAR |  | The facility (free text) that recovered the donor organ. |
| 50 | `DNR_DOWN_MINUTES` | INTEGER |  | Specifies donor downtime in minutes. |
| 51 | `AGE_RANGE_C_NAME` | VARCHAR | org | The age range of the organ donor. |
| 52 | `AGE_UNITS_C_NAME` | VARCHAR |  | Units for the age of the requisition grouper |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [ORGAN_DNR_CITIZENSHIP](ORGAN_DNR_CITIZENSHIP.md) | `DONOR_ID` | high |
| [ORGAN_DONOR_RISK_CRITERIA](ORGAN_DONOR_RISK_CRITERIA.md) | `DONOR_ID` | high |
| [TXP_DNR_VASOMED_INFO](TXP_DNR_VASOMED_INFO.md) | `DONOR_ID` | high |

