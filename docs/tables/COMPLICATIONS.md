# COMPLICATIONS

> The COMPLICATIONS table contains information related to problems that are considered complications. Only problems that have at least one column populated from this table are included in this table. All of the problems in this table will still be found in PROBLEM_LIST.

**Primary key:** `PROBLEM_LIST_ID`  
**Columns:** 55  
**Org-specific columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `INFECTION_SITE_C_NAME` | VARCHAR | org | This item tracks the location of an infection in the patient's body. |
| 3 | `INFECTION_SITE_OTH` | VARCHAR |  | This item allows free-text documentation of an infection site. |
| 4 | `ANTIBIOTICS_YN` | VARCHAR |  | This item indicates whether the patient was on an antibiotic medication prior to the diagnosis. |
| 5 | `RECURRENT_YN` | VARCHAR |  | This item indicates whether the diagnosis is recurrent. |
| 6 | `COLONOSCOPY_YN` | VARCHAR |  | This item indicates whether the patient has had a colonoscopy related to the diagnosis. |
| 7 | `MRI_DONE_YN` | VARCHAR |  | This item indicates whether the patient has had an MRI related to the diagnosis. |
| 8 | `MRI_FINDINGS_C_NAME` | VARCHAR | org | This item tracks the results of the MRI procedure related to the diagnosis. |
| 9 | `FOLEY_PRESENT_YN` | VARCHAR |  | This item indicates whether the patient had an indwelling Foley catheter at the time of diagnosis. |
| 10 | `HARDWARE_YN` | VARCHAR |  | This item indicates whether the patient had a hardware implant at the time of diagnosis. |
| 11 | `STENT_PRESENT_YN` | VARCHAR |  | This item indicates whether the patient had a stent at the time of diagnosis. |
| 12 | `INFILTRATION_TYPE_C_NAME` | VARCHAR | org | This item tracks the type of pulmonary infiltrate due to pneumonia. |
| 13 | `LINE_PRIMARY_YN` | VARCHAR |  | This item indicates whether the infection is a primary bloodstream infection of the central line. |
| 14 | `OTH_PRIMARY_YN` | VARCHAR |  | This item indicates whether the infection is a primary bloodstream infection, but not of the central line. |
| 15 | `PD_RELATED_YN` | VARCHAR |  | This item indicates whether the diagnosis is related to peritoneal dialysis (PD). |
| 16 | `SBP_RELATED_YN` | VARCHAR |  | This item indicates whether the diagnosis is related to spontaneous bacterial peritonitis (SBP). |
| 17 | `ANTICOAG_PRE_DX_OTH` | VARCHAR |  | This item allows free-text documentation of anticoagulation therapy medications taken prior to the diagnosis. |
| 18 | `BANFF_SCORE_C_NAME` | VARCHAR | org | This item tracks graft organ rejection grade. |
| 19 | `BIOPSY_DT` | DATETIME |  | This item displays the result date of the biopsy test related to the diagnosis. |
| 20 | `DSA_YN` | VARCHAR |  | This item indicates whether the patient has donor-specific antibodies. |
| 21 | `FATAL_YN` | VARCHAR |  | This item indicates whether the diagnosis was the patient's cause of death. |
| 22 | `MODE_OF_DX_OTH` | VARCHAR |  | This item allows free-text documentation of diagnostic techniques. |
| 23 | `OR_DRAIN_YN` | VARCHAR |  | This item indicates whether the patient required surgical drainage. |
| 24 | `RETURN_TO_OR_YN` | VARCHAR |  | This item indicates whether the patient returned to the OR. |
| 25 | `FOLEY_REMOVE_YN` | VARCHAR |  | This item indicates whether the Foley catheter was removed. |
| 26 | `FOLEY_REINSERT_YN` | VARCHAR |  | This item indicates whether the Foley catheter was reinserted. |
| 27 | `FOLEY_SELF_YN` | VARCHAR |  | This item indicates whether the patient inserted the Foley catheter. |
| 28 | `GU_CONSULT_YN` | VARCHAR |  | This item indicates whether the patient had a urology consult related to the diagnosis. |
| 29 | `C4D_POS_YN` | VARCHAR |  | This item indicates whether the patient tested positive for the C4d antibody. |
| 30 | `C4D_TYPE_C_NAME` | VARCHAR | org | This item tracks the type of C4d-positive result. |
| 31 | `CATH_REMOVE_DT` | DATETIME |  | This item displays the initial removal date of the Foley catheter. |
| 32 | `TRANSFUSION_YN` | VARCHAR |  | This item indicates whether the patient received a blood transfusion related to the diagnosis. |
| 33 | `BLOOD_UNITS_NUM` | INTEGER |  | This item displays how many units of blood the patient received during the blood transfusion. |
| 34 | `STEATOSIS_C_NAME` | VARCHAR | org | This item tracks the degree of steatosis (lipid retention) related to the diagnosis. |
| 35 | `PV_VELO_POST_NUM` | NUMERIC |  | This item displays the velocity of the portal vein (in cm/sec) after vessel repair. |
| 36 | `HV_VELO_POST_NUM` | NUMERIC |  | This item displays the velocity of the hepatic vein (in cm/sec) after vessel repair. |
| 37 | `HEPAT_RUPTURE_YN` | VARCHAR |  | This item indicates whether the patient had a hepatic artery rupture related to the diagnosis. |
| 38 | `HEPATITIS_GRADE_C_NAME` | VARCHAR | org | This item tracks the grade of the patient's hepatitis infection. |
| 39 | `HEPATITIS_STAGE_C_NAME` | VARCHAR | org | This item tracks the stage of the patient's hepatitis infection. |
| 40 | `PRERESIST_INDEX_NUM` | NUMERIC |  | This item display the pre-resistive index of the hepatic artery. |
| 41 | `POSTRESIS_INDEX_NUM` | NUMERIC |  | This item displays the post-resistive index of the hepatic artery. |
| 42 | `INFILTRAT_TYPE_OTH` | VARCHAR |  | This item allows free-text documentation of an infiltration type. |
| 43 | `HEP_ARTERY_STATUS_C_NAME` | VARCHAR | org | This item tracks the current status of the hepatic artery. |
| 44 | `HEP_ART_STATUS_OTH` | VARCHAR |  | This item allows free-text documentation of a hepatic artery status. |
| 45 | `HV_VELO_PRE_NUM` | NUMERIC |  | This item displays the velocity of the hepatic vein (in cm/sec) before vessel repair. |
| 46 | `PV_VELO_PRE_NUM` | NUMERIC |  | This item displays the velocity of the portal vein (in cm/sec) before vessel repair. |
| 47 | `AORTIC_PERF_VOL_NUM` | NUMERIC |  | This item displays the volume of aortic perfusion in mL. |
| 48 | `PORTAL_PERF_VOL_NUM` | NUMERIC |  | This item displays the volume of portal perfusion in mL. |
| 49 | `BIL_LEAK_SITE_OTH` | VARCHAR |  | This items allows free-text documentation of a biliary leak site. |
| 50 | `PANC_LEAK_SITE_OTH` | VARCHAR |  | This item allows free-text documentation of a pancreatic leak site. |
| 51 | `HEM_SOURCE_OTH` | VARCHAR |  | This item allows free-text documentation of the hemorrhage source. |
| 52 | `COMPN_DOC_STAT_C_NAME` | VARCHAR | org | The status of the complication details documentation. |
| 53 | `COMPN_REVIEW_SPEC_C_NAME` | VARCHAR | org | Specialty that reviewed the complication |
| 54 | `COMPN_REVIEW_DATE` | DATETIME |  | Date the complication was reviewed |
| 55 | `COMPN_REVIEW_STAT_C_NAME` | VARCHAR | org | The review status of the complication |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

