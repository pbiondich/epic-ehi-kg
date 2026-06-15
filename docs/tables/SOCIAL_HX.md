# SOCIAL_HX

> The SOCIAL_HX table contains social history data for each history encounter stored in your system. This table has one row per history encounter.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 92  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 2 | `CIGARETTES_YN` | VARCHAR | org | Y if the patient uses cigarettes. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 3 | `PIPES_YN` | VARCHAR |  | Y if the patient smokes a pipe. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 4 | `CIGARS_YN` | VARCHAR |  | Y if the patient uses cigars. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 5 | `SNUFF_YN` | VARCHAR |  | Y if the patient uses snuff. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 6 | `CHEW_YN` | VARCHAR |  | Y if the patient uses chewing tobacco. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 7 | `ALCOHOL_OZ_PER_WK` | VARCHAR |  | The fluid ounces of alcohol the patient consumes per week. |
| 8 | `ALCOHOL_COMMENT` | VARCHAR |  | Free-text comments regarding the patient’s use of alcohol. |
| 9 | `IV_DRUG_USER_YN` | VARCHAR | org | Y if the patient is an IV drug user. N if the patient is not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 10 | `ILLICIT_DRUG_FREQ` | VARCHAR |  | The times per week the patient uses or used illicit drugs. |
| 11 | `ILLICIT_DRUG_CMT` | VARCHAR |  | Free-text comments regarding the patient’s use of illicit drugs. |
| 12 | `FEMALE_PARTNER_YN` | VARCHAR | org | Y if the patient has a female sexual partner. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 13 | `MALE_PARTNER_YN` | VARCHAR |  | Y if the patient has a male sexual partner. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 14 | `CONDOM_YN` | VARCHAR | org | Y if the patient uses a condom during sexual activity. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 15 | `PILL_YN` | VARCHAR |  | Y if the patient uses birth control pills. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 16 | `DIAPHRAGM_YN` | VARCHAR |  | Y if the patient uses a diaphragm. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 17 | `IUD_YN` | VARCHAR |  | Y if the patient uses an IUD. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 18 | `SURGICAL_YN` | VARCHAR |  | Y if the patient uses a surgical method of birth control such as hysterectomy, vasectomy, or tubal-ligation. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 19 | `SPERMICIDE_YN` | VARCHAR |  | Y if the patient uses spermicide. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 20 | `IMPLANT_YN` | VARCHAR |  | Y if the patient uses an implant as a form of birth control. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 21 | `RHYTHM_YN` | VARCHAR |  | Y if the patient uses the rhythm method as a form of birth control. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 22 | `INJECTION_YN` | VARCHAR |  | Y if the patient uses an injection as a form of birth control. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 23 | `SPONGE_YN` | VARCHAR |  | Y if the patient uses a sponge as a form of birth control. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 24 | `INSERTS_YN` | VARCHAR |  | Y if the patient uses inserts as a form of birth control. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 25 | `ABSTINENCE_YN` | VARCHAR |  | Y if the patient practices abstinence. N if the patient does not. NOTE: Uses the EPIC_IN_ITEM function to determine if a given value exists in a multiple response item. If the category value for this selection exists in the multiple response item, then it returns "Y", otherwise it returns "N". |
| 26 | `SEX_COMMENT` | VARCHAR |  | Free-text comments regarding the patient’s sexual activity. |
| 27 | `YEARS_EDUCATION` | VARCHAR |  | The number of years of education the patient has completed. Note: This is a free text field. |
| 28 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 29 | `TOB_SRC_C_NAME` | VARCHAR | org | Source for Tobacco History |
| 30 | `ALCOHOL_SRC_C_NAME` | VARCHAR |  | This columns stores the person (e.g. provider, patient, legal guardian) who provided alcohol use information for this encounter. |
| 31 | `DRUG_SRC_C_NAME` | VARCHAR |  | This columns stores the person (e.g. provider, patient, legal guardian) who provided illicit drug use information for this encounter. |
| 32 | `SEX_SRC_C_NAME` | VARCHAR |  | This columns stores the person (e.g. provider, patient, legal guardian) who provided sexual activity information for this encounter. |
| 33 | `HX_LNK_ENC_CSN` | NUMERIC | FK→ | The Contact Serial Number of the encounter in which the history was created/edited. If the history was created/edited outside of the context of an encounter, then this column will be blank. |
| 34 | `ALCOHOL_USE_C_NAME` | VARCHAR |  | The category value associated with the patient's alcohol use. Data may include, Yes, No, or Not Asked. |
| 35 | `ILL_DRUG_USER_C_NAME` | VARCHAR |  | The category value associated with the patient's use of illicit drugs. Data may include, Yes, No, or Not Asked. |
| 36 | `SEXUALLY_ACTIVE_C_NAME` | VARCHAR |  | The category value associated with the patient's sexual activity. Data may include Yes, No, Not Asked, or Not Now |
| 37 | `TOBACCO_USER_C_NAME` | VARCHAR |  | The category value associated with the patient's tobacco use. Data may include, Yes, Never, Not Asked or Quit. |
| 38 | `SMOKELESS_TOB_USE_C` | INTEGER |  | Stores the patient's usage of smokeless tobacco. Data may include, Current User, Former User, Never Used or Unknown. |
| 39 | `SMOKELESS_QUIT_DATE` | DATETIME |  | The date on which the patient quit using smokeless tobacco. |
| 40 | `SMOKING_TOB_USE_C` | INTEGER |  | Stores the patient's usage of smoking tobacco. Data may include, Current Everyday Smoker, Current Some Day Smoker, Former Smoker, Never Smoker, Unknown If Ever Smoked or Smoker, Current Status Unknown. |
| 41 | `UNKNOWN_FAM_HX_YN` | VARCHAR |  | Y if the patient's family history is unknown by the patient. N otherwise. |
| 42 | `EDU_LEVEL_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about level of education. Response is categorical, and corresponds to highest level of school attended. |
| 43 | `FIN_RESOURCE_STRAIN_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about financial resource strain. |
| 44 | `IPV_EMOTIONAL_ABUSE_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about emotional abuse from an intimate partner. |
| 45 | `IPV_FEAR_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about fear of an intimate partner. |
| 46 | `IPV_SEXUAL_ABUSE_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about sexual abuse from an intimate partner. |
| 47 | `IPV_PHYSICAL_ABUSE_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about physical abuse from an intimate partner. |
| 48 | `ALCOHOL_FREQ_C_NAME` | VARCHAR |  | This item stores responses for the social drivers of health question about frequency of drinking alcohol. |
| 49 | `ALCOHOL_DRINKS_PER_DAY_C_NAME` | VARCHAR |  | This item stores responses for the social drivers of health questions about number of standard drinks consumed in a typical day. |
| 50 | `ALCOHOL_BINGE_C_NAME` | VARCHAR |  | This item stores responses for the social drivers of health questions about binge drinking. |
| 51 | `LIVING_W_SPOUSE_C_NAME` | VARCHAR |  | This item stores the response to social drivers of health question about whether or not the patient is currently living with spouse or partner. |
| 52 | `DAILY_STRESS_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about daily stress. |
| 53 | `PHONE_COMMUNICATION_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about how often the patient socializes with friends or family over the phone. |
| 54 | `SOCIALIZATION_FREQ_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about how often the patient socializes with friends or family in person. |
| 55 | `CHURCH_ATTENDANCE_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about how often the patient attends religious services. |
| 56 | `CLUBMTG_ATTENDANCE_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about how often the patient attends club or other organization meetings in a year. |
| 57 | `CLUB_MEMBER_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about whether the patient is a member of any clubs or organizations. |
| 58 | `PHYS_ACT_DAYS_PER_WEEK_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about how many days a week the patient exercises. |
| 59 | `PHYS_ACT_MIN_PER_SESS_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about how many minutes the patient exercises on days that they exercise. |
| 60 | `FOOD_INSECURITY_SCARCE_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about whether or not the patient had run out of food and was not able to buy more. |
| 61 | `FOOD_INSECURITY_WORRY_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about whether the patient worried about food running out in the past year or not. |
| 62 | `MED_TRANSPORT_NEEDS_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about whether the patient had difficulty regarding transportation for medical appointments and medicine. |
| 63 | `OTHER_TRANSPORT_NEEDS_C_NAME` | VARCHAR |  | This item stores responses to the social drivers of health question about whether the patient had difficulty regarding transportation for things other than medical appointments and medicine. |
| 64 | `SOC_PHONE_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Social Connections Phone history. |
| 65 | `SOC_TOGETHER_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Social Connections Get Together history. |
| 66 | `SOC_CHURCH_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Social Connections Church history. |
| 67 | `SOC_MEETINGS_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Social Connections Meetings history. |
| 68 | `SOC_MEMBER_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Social Connections Membership history. |
| 69 | `SOC_LIVING_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Social Connections Living history. |
| 70 | `PHYS_DPW_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Physical Activity Days per Week history. |
| 71 | `PHYS_MPS_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Physical Activity Minutes Per Session history. |
| 72 | `STRESS_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Stress history. |
| 73 | `EDUCATION_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Education history. |
| 74 | `FINANCIAL_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Financial history. |
| 75 | `IPV_EMOTIONAL_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Intimate Partner Violence (IPV) emotional history. |
| 76 | `IPV_FEAR_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's IPV Fear history. |
| 77 | `IPV_SEXABUSE_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's IPV Sexual Abuse history. |
| 78 | `IPV_PHYSABUSE_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's physical abuse history. |
| 79 | `ALC_FREQ_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Alcohol Frequency history. |
| 80 | `ALC_STD_DRINK_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Alcohol Standard Drinks history. |
| 81 | `ALC_BINGE_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Alcohol Binge history. |
| 82 | `FOOD_WORRY_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Food Worry history. |
| 83 | `FOOD_SCARCITY_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Food Scarcity history. |
| 84 | `TRANS_MED_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Transport Medical history. |
| 85 | `TRANS_NONMED_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for a patient's Transport Non-medical history. |
| 86 | `FAM_PAT_ADPT_PAR_1` | INTEGER |  | Stores the family history ID of the patient's adoptive parent. A patient can have two adoptive parents. The ID of the other parent is in FAM_PAT_ADPT_PAR_2. |
| 87 | `FAM_PAT_ADPT_PAR_2` | INTEGER |  | Stores the family history ID of the patient's adoptive parent. A patient can have two adoptive parents. The ID of the other parent is in FAM_PAT_ADPT_PAR_1. |
| 88 | `TOB_HX_ADDL_PACKYEARS` | NUMERIC |  | Number to add to the total number of pack years calculated for the patient's tobacco history. |
| 89 | `TOB_HX_SMOKE_EXPOSURE_CMT` | VARCHAR |  | Store the comment for passive tobacco smoke exposure. |
| 90 | `PASSIVE_SMOKE_EXPOSURE_C_NAME` | VARCHAR |  | Document the patient's passive smoke exposure. |
| 91 | `FAMHX_PAT_IS_ADOPTED_C_NAME` | VARCHAR |  | The Adoption Status category ID for the patient. |
| 92 | `AVERAGE_PPD` | NUMERIC |  | Holds the average packs per day a patient has smoked from their earliest start date to their latest quit date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HX_LNK_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

