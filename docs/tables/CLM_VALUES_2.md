# CLM_VALUES_2

> All values associated with a claim are stored in the Claim External Value record. The CLM_VALUES_2 table holds claim-level values set by the system during claims processing or by user edits.

**Overflow of:** [CLM_VALUES](CLM_VALUES.md)  
**Primary key:** `RECORD_ID`  
**Columns:** 97

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim values record. |
| 2 | `ADMSN_TYP` | VARCHAR |  | The admission type for the claim. |
| 3 | `ADMSN_SRC` | VARCHAR |  | The admission source for the claim. |
| 4 | `DISCHRG_DISP` | VARCHAR |  | The patient's discharge status, also referred to as the discharge disposition. |
| 5 | `RFL_NUM` | VARCHAR |  | The referral number for the claim. |
| 6 | `AUTH_NUM` | VARCHAR |  | The prior authorization number for the claim. |
| 7 | `SPEC_PROG_IND` | VARCHAR |  | The indicator that the services on the claim were rendered under one of a list of special programs. |
| 8 | `CLM_DELAY_RSN` | VARCHAR |  | The reason code explaining why the claim was submitted after the payer's normal filing deadline. |
| 9 | `AUTH_EXCEPT_CD` | VARCHAR |  | The code explaining why services that normally need authorization were performed without the necessary authorization. |
| 10 | `PAT_AMT_PAID` | NUMERIC |  | The amount already paid by the patient. |
| 11 | `PAT_AMT_DUE` | NUMERIC |  | The amount estimated to be the patient's responsibility. |
| 12 | `AUTO_ACDNT_STATE` | VARCHAR |  | The state in which an automobile accident occurred. |
| 13 | `AUTO_ACDNT_CNTRY` | VARCHAR |  | The country in which an automobile accident occurred. It is only populated when the accident occurred outside the United States. |
| 14 | `MAMM_CERT_NUM` | VARCHAR |  | The provider's certification number when the claim contains mammography services. |
| 15 | `CLIA_NUM` | VARCHAR |  | The Clinical Laboratory Improvement Amendment (CLIA) number when the claim contains lab services. |
| 16 | `DEMO_PRJ_ID` | VARCHAR |  | The identifier for claims billed under atypical rules (e.g., pilot programs, clinical trials). |
| 17 | `SPINAL_MAN_COND_CD` | VARCHAR |  | The patient's condition when the claim contains chiropractic services. |
| 18 | `EPSDT_CERT_APPLIES` | VARCHAR |  | The indicator that identifies whether an Early and Periodic Screening, Diagnostic, and Treatment (EPSDT) referral was given to the patient. |
| 19 | `ORTHO_TOT_MO` | INTEGER |  | The total number of months of orthodontic treatment. |
| 20 | `ORTHO_MO_REMAIN` | INTEGER |  | The number of months of orthodontic treatment remaining for a transfer patient. |
| 21 | `ADMSN_DX_QUAL` | VARCHAR |  | The qualifier that identifies the code set for the admission diagnosis for the claim. |
| 22 | `ADMSN_DX` | VARCHAR |  | The admission diagnosis for the claim. |
| 23 | `DRG` | VARCHAR |  | The Diagnosis Related Group (DRG) determined for the claim. |
| 24 | `ANES_SURG_PROC` | VARCHAR |  | The HCPCS code of the surgical procedure performed under anesthesia when the code needs to be reported on the anesthesia claim. |
| 25 | `OUTSIDE_LAB` | VARCHAR |  | The indicator that the claim includes purchased services rendered by an independent provider. |
| 26 | `OUTSIDE_LAB_CHG` | NUMERIC |  | The price of the purchased services. |
| 27 | `CLM_FROM_DT` | DATETIME |  | The earliest date represented on the claim. This date could be the minimum service date for an outpatient or professional claim or the admission date for an inpatient claim. |
| 28 | `CLM_TO_DT` | DATETIME |  | The latest date represented on the claim. This date could be the maximum service date for an outpatient or professional claim or the discharge date for an inpatient claim. |
| 29 | `ADMSN_DT` | DATETIME |  | The admission date on the claim. For outpatient claims, this date represents the visit or start of care date. |
| 30 | `ADMSN_TM` | DATETIME (Local) |  | The time at which the patient was admitted to the facility. This time is only available for institutional claims. Note that the value is the exact time, including both the hour and minutes. |
| 31 | `DISCHG_DT` | DATETIME |  | The discharge date on the claim. |
| 32 | `DISCHG_TM` | DATETIME (Local) |  | The time at which the patient was discharged. This time is only available for institutional claims. Note that the value is the exact time, including both the hour and minutes. |
| 33 | `ILL_INJ_DT` | DATETIME |  | The date in which the patient was injured or when the current illness was first noticed. |
| 34 | `INIT_TREAT_DT` | DATETIME |  | The initial treatment date when the claim represents a series of visits (e.g., physical therapy, spinal manipulation, dialysis, pregnancy). |
| 35 | `LST_SEEN_DT` | DATETIME |  | The date the patient was last seen by the attending or supervising provider. |
| 36 | `ACUTE_MANIF_DT` | DATETIME |  | The date acute symptoms first manifested. |
| 37 | `ACDNT_DT` | DATETIME |  | The date the automobile accident occurred. |
| 38 | `LMP_DT` | DATETIME |  | The date of the last menstrual period. |
| 39 | `LST_XRAY_DT` | DATETIME |  | The date of the last X-Ray. |
| 40 | `HEAR_VIS_RX_DT` | DATETIME |  | The date on which the prescription was written for hearing devices or vision frames and lenses. |
| 41 | `DISAB_START_DT` | DATETIME |  | The earliest date on which the patient was disabled and could not work. |
| 42 | `DISAB_END_DT` | DATETIME |  | The latest date on which the patient was disabled and could not work. |
| 43 | `LST_WK_DT` | DATETIME |  | The last date on which the patient was able to perform his or her duties at work. |
| 44 | `AUTH_RETURN_WK_DT` | DATETIME |  | The date on which the patient can return to work. |
| 45 | `ASSUM_CARE_DT` | DATETIME |  | The date on which care was assumed by another provider during post-operative care. |
| 46 | `RELINQ_CARE_DT` | DATETIME |  | The date on which the provider of the claim ceased post-operative care. |
| 47 | `ORTHO_BAND_DT` | DATETIME |  | The date orthodontic appliances were placed. |
| 48 | `DENT_SRV_DT` | DATETIME |  | The date on which dental services were performed. |
| 49 | `SIMILAR_ILL_DT` | DATETIME |  | The earliest date on which symptoms of the same or similar illness were noticed. |
| 50 | `AMB_PAT_WT` | NUMERIC |  | The patient's weight (in pounds) when the patient is transported by an ambulance. |
| 51 | `AMB_TRANS_RSN_CD` | VARCHAR |  | The code explaining why the patient was transported by ambulance. |
| 52 | `AMB_TRANS_DIST` | NUMERIC |  | The distance (in miles) the patient was transported. |
| 53 | `AMB_RND_TRIP_DESC` | VARCHAR |  | The note explaining the need for round trip transportation. |
| 54 | `AMB_STRETCHER_DESC` | VARCHAR |  | The note explaining the need for a stretcher. |
| 55 | `CNTRCT_TYP` | VARCHAR |  | The code representing the type of contract between the provider and the payer. |
| 56 | `CNTRCT_AMT` | NUMERIC |  | The amount assigned by the contract between the provider and the payer. |
| 57 | `CNTRCT_PCT` | NUMERIC |  | The contract percentage for the claim assigned by the contract between the provider and the payer. |
| 58 | `CNTRCT_CD` | VARCHAR |  | The code representing the claim type under the contract between the provider and the payer. |
| 59 | `CNTRCT_DISCNT_PCT` | NUMERIC |  | The discount percentage assigned by the contract between the provider and the payer. |
| 60 | `CNTRCT_VERS_ID` | VARCHAR |  | The version of the contract used on the claim. |
| 61 | `ATT_PROV_NAM_LAST` | VARCHAR |  | The attending provider's last name. |
| 62 | `ATT_PROV_NAM_FIRST` | VARCHAR |  | The attending provider's first name. |
| 63 | `ATT_PROV_NAM_MID` | VARCHAR |  | The attending provider's middle name. |
| 64 | `ATT_PROV_NAM_SUF` | VARCHAR |  | The suffix to the attending provider's name (e.g., Jr, III). |
| 65 | `ATT_PROV_NPI` | VARCHAR |  | The attending provider's National Provider Identifier (NPI). |
| 66 | `ATT_PROV_TAXONOMY` | VARCHAR |  | The attending provider's taxonomy code. |
| 67 | `OPER_PROV_NAM_LAST` | VARCHAR |  | The operating provider's last name. |
| 68 | `OPER_PROV_NAM_FIRST` | VARCHAR |  | The operating provider's first name. |
| 69 | `OPER_PROV_NAM_MID` | VARCHAR |  | The operating provider's middle name. |
| 70 | `OPER_PROV_NAM_SUF` | VARCHAR |  | The suffix to the operating provider's name (e.g., Jr, III). |
| 71 | `OPER_PROV_NPI` | VARCHAR |  | The operating provider's National Provider Identifier (NPI). |
| 72 | `OTH_PROV_NAM_LAST` | VARCHAR |  | The other operating provider's last name. |
| 73 | `OTH_PROV_NAM_FIRST` | VARCHAR |  | The other operating provider's first name. |
| 74 | `OTH_PROV_NAM_MID` | VARCHAR |  | The other operating provider's middle name. |
| 75 | `OTH_PROV_NAM_SUF` | VARCHAR |  | The suffix to the other operating provider's name (e.g., Jr, III). |
| 76 | `OTH_PROV_NPI` | VARCHAR |  | The other operating provider's National Provider Identifier (NPI). |
| 77 | `REND_PROV_TYP` | VARCHAR |  | The rendering provider on the claim is a person or a non-person. |
| 78 | `REND_PROV_NAM_LAST` | VARCHAR |  | The rendering provider's last name (if a person) or the organization name (if a non-person). |
| 79 | `REND_PROV_NAM_FIRST` | VARCHAR |  | The rendering provider's first name. It is only populated when the provider is a person. |
| 80 | `REND_PROV_NAM_MID` | VARCHAR |  | The rendering provider's middle name. It is only populated when the provider is a person. |
| 81 | `REND_PROV_NAM_SUF` | VARCHAR |  | The suffix to the rendering provider's name (e.g., Jr, III). It is only populated when the provider is a person. |
| 82 | `REND_PROV_NPI` | VARCHAR |  | The rendering provider's National Provider Identifier (NPI). |
| 83 | `REND_PROV_TAXONOMY` | VARCHAR |  | The rendering provider's taxonomy code. |
| 84 | `REF_PROV_NAM_LAST` | VARCHAR |  | The referring provider's last name. |
| 85 | `REF_PROV_NAM_FIRST` | VARCHAR |  | The referring provider's first name. |
| 86 | `REF_PROV_NAM_MID` | VARCHAR |  | The referring provider's middle name. |
| 87 | `REF_PROV_NAM_SUF` | VARCHAR |  | The suffix to the referring provider's name (e.g., Jr, III). |
| 88 | `REF_PROV_NPI` | VARCHAR |  | The referring provider's National Provider Identifier (NPI). |
| 89 | `REF_PROV_TAXONOMY` | VARCHAR |  | The referring provider's taxonomy code. |
| 90 | `SUP_PROV_NAM_LAST` | VARCHAR |  | The supervising provider's last name. |
| 91 | `SUP_PROV_NAM_FIRST` | VARCHAR |  | The supervising provider's first name. |
| 92 | `SUP_PROV_NAM_MID` | VARCHAR |  | The supervising provider's middle name. |
| 93 | `SUP_PROV_NAM_SUF` | VARCHAR |  | The suffix to the supervising provider's name (e.g., Jr, III). |
| 94 | `SUP_PROV_NPI` | VARCHAR |  | The supervising provider's National Provider Identifier (NPI). |
| 95 | `ASST_SURG_NAM_LAST` | VARCHAR |  | The assistant dental surgeon's last name. |
| 96 | `ASST_SURG_NAM_FIRST` | VARCHAR |  | The assistant dental surgeon's first name. |
| 97 | `ASST_SURG_NAM_MID` | VARCHAR |  | The assistant dental surgeon's middle name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

