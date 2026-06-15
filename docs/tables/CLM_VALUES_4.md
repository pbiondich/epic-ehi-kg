# CLM_VALUES_4

> All values associated with a claim are stored in the Claim External Value record. The CLM_VALUES_4 table holds claim-level values set by the system during claims processing or by user edits.

**Overflow of:** [CLM_VALUES](CLM_VALUES.md)  
**Primary key:** `RECORD_ID`  
**Columns:** 66

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record. |
| 2 | `REP_CLM_NUM` | VARCHAR |  | The repriced claim reference number. |
| 3 | `ADJ_REP_CLM_NUM` | VARCHAR |  | The adjusted repriced claim number. |
| 4 | `CLM_TRANS_INTMD` | VARCHAR |  | The identifier for claim transmission intermediaries. |
| 5 | `CLM_PRO_APP_NUM` | VARCHAR |  | The Peer Review Organization (PRO) Approval Number for the claim. |
| 6 | `CLM_PRICING_METHDLG` | VARCHAR |  | The claim pricing methodology. |
| 7 | `CLM_REP_ALWD_AMT` | NUMERIC |  | The claim re-pricing allowed amount. |
| 8 | `CLM_REP_SVNG_AMT` | NUMERIC |  | The claim Repriced Saving Amount. |
| 9 | `CLM_REP_ORGID` | VARCHAR |  | The Repricing Organization Identifier for the claim. |
| 10 | `REP_PDIEM_FLTRT_AMT` | NUMERIC |  | The Repricing Per Diem or Flat Rate Amount for the claim. |
| 11 | `REP_APRVD_DRG_CODE` | VARCHAR |  | The Repriced Approved Diagnosis Related Group Code for the claim. |
| 12 | `REP_APPRVD_AMT` | NUMERIC |  | The Repriced Approved Amount for the claim. |
| 13 | `REP_APRVD_REV_CODE` | VARCHAR |  | The Repriced Approved Revenue Code for the claim. |
| 14 | `REP_ASU_MSRMNT_CODE` | VARCHAR |  | The basis of measurement (e.g., Days, Units) for Repriced Approved Service Unit Count. |
| 15 | `REP_APR_SERV_CNT` | NUMERIC |  | The Repriced Approved Service Unit Count for the claim. |
| 16 | `PAYTO_PLAN_TAXID` | VARCHAR |  | The Pay-To Plan Tax Identification Number. |
| 17 | `FIRST_CNCT_DT` | DATETIME |  | The Property and Casualty Date of First Contact. |
| 18 | `REPRICER_RECVD_DT` | DATETIME |  | The Repricer Received Date. |
| 19 | `MCARE_XOVER_IND` | VARCHAR |  | The Mandatory Medicare Crossover Indicator. |
| 20 | `CARE_PLN_NUM` | VARCHAR |  | The Care Plan Oversight Number. |
| 21 | `HOMEBOUND_COND_QUAL` | VARCHAR |  | The Homebound Condition Qualifier. |
| 22 | `HOMEBOUND_COND_CD` | VARCHAR |  | The Homebound Condition Code. |
| 23 | `DENTAL_SVC_FROM_DT` | DATETIME |  | The Dental Service From Date. It will only be populated when using a dental form. |
| 24 | `DENTAL_SVC_TO_DT` | DATETIME |  | The Dental Service To Date. It will only be populated when using a dental form. |
| 25 | `DENTAL_SVC_DT_QUAL` | VARCHAR |  | The dental date range qualifier. It will only be populated on a dental form. |
| 26 | `ORTHO_TREAT_IND` | VARCHAR |  | The Orthodontic Treatment Indicator. This column will only have data when a dental claim has orthodontic services without any months of orthodontic treatment being reported. |
| 27 | `DENT_PREDET_CODE` | VARCHAR |  | The code identifying whether a claim is a pre-authorization dental claim. If the claim is a predetermination of benefits claim (pre-auth), this column will be populated with "PB". If the claim is a statement of actual services, this column will be null. |
| 28 | `OTH_ACC_EMER_YN` | VARCHAR |  | The indicator that the claim includes emergency services. |
| 29 | `STER_ABOR_YN` | VARCHAR |  | The indicator that a visit was related to a sterilization or abortion. |
| 30 | `PAYEE_NUM` | VARCHAR |  | The payee number for Medicaid. |
| 31 | `CLM_LVL_TOS` | VARCHAR |  | The claim-level type of service code. |
| 32 | `CLM_LVL_EPSDT_YN` | VARCHAR |  | The indicator that the claim was related to an Early and Periodic Screening, Diagnostic, and Treatment (EPSDT) visit. |
| 33 | `CLM_LVL_FAM_PLAN_YN` | VARCHAR |  | The indicator that the claim was related to family planning. |
| 34 | `CLM_LVL_EMER_YN` | VARCHAR |  | The indicator that the claim was related to emergency services. |
| 35 | `PAT_LOCATION_IDENT` | VARCHAR |  | The county code corresponding to the patient address. |
| 36 | `PAT_PERSONAL_IDENT` | VARCHAR |  | The combination of patient name characters and digits from their SSN used by the Statewide Planning and Research Cooperative System (SPARCS) to identify the patient. |
| 37 | `DRG_SOI` | VARCHAR |  | The Severity Of Illness (SOI) of Diagnosis Related Group (DRG) determined for the claim. |
| 38 | `DRG_ROM` | VARCHAR |  | The Risk Of Mortality (ROM) of Diagnosis Related Group (DRG) determined for the claim. |
| 39 | `CAS_SVC_POS_NUM` | INTEGER |  | The position number within the service line in the source claim CEV. |
| 40 | `CLM_RECORD_INDICATOR` | VARCHAR |  | The action to be taken on the claim. |
| 41 | `LINE_OF_BUSINESS_CODE` | VARCHAR |  | The line of business (LOB) code under which claim was paid. |
| 42 | `BENEFIT_ID` | VARCHAR |  | The identifier for a set of parameters, benefits, or coverage criteria used to adjudicate a claim. |
| 43 | `PLAN_TYPE` | VARCHAR |  | The type of plan identifier. |
| 44 | `PRESC_PROV_TAXONOMY` | VARCHAR |  | The prescribing provider taxonomy code. |
| 45 | `ADJUD_DATE` | DATETIME |  | The date the claim was processed. |
| 46 | `ADJUD_TM` | DATETIME (Local) |  | The time the claim was processed. |
| 47 | `REJECT_OVERRIDE_CODE` | VARCHAR |  | The reason for paying a claim when override is used. |
| 48 | `CROSS_REF_ICN` | VARCHAR |  | The ID associated with the original claim for adjustment claims. |
| 49 | `PAYMENT_CLARIFICATION_CODE` | VARCHAR |  | The additional information on the status of the payment of the claim. |
| 50 | `ADJUSTMENT_TYPE` | VARCHAR |  | The type of adjustment whether debit or credit. |
| 51 | `STER_ABOR_CODE` | VARCHAR |  | The single-letter sterilization/abortion code appearing in field 22D on the eMedNY 150003 claim form |
| 52 | `POSSIBLE_DISABILITY_YN` | VARCHAR |  | The indicator that the service was for treatment of a condition which appeared to be of a disabling nature for field 22F on the eMedNY 150003. |
| 53 | `PMT_SRC_MCR_INVOLVE` | VARCHAR |  | The single-digit source code indicator that indicates Medicare's involvement in paying for these charges for field 23B box M on the eMedNY 150003 claim form. |
| 54 | `PMT_SRC_OTHR_INVOLV` | VARCHAR |  | The single-digit code indicating whether the patient has a coverage besides Medicare and Medicaid for field 23B box O on the eMedNY 150003 claim form. |
| 55 | `PMT_SRC_INS_CODE` | VARCHAR |  | The two-digit insurance code for the commercial coverage, if any, for field 23B box O on the eMedNY 150003 claim form. |
| 56 | `LOCATOR_CODE` | VARCHAR |  | The locator code assigned by Medicaid for the address where the service was performed for field 25C on the eMedNY 150003 paper claim form. |
| 57 | `MEM_SUBMIT_PMT_RELEASE_DATE` | DATETIME |  | The date the member submitted claim became payable, which could differ from the check date. |
| 58 | `CHECK_DATE` | DATETIME |  | The claim check date. |
| 59 | `PAT_DEM_CODE_QUAL` | VARCHAR |  | The patient demographic code qualifier. |
| 60 | `PAT_DEM_CODE` | VARCHAR |  | The patient demographic code. |
| 61 | `DRG_CODE_SET` | VARCHAR |  | The code set of the Diagnosis Related Group (e.g., APR-DRG, MS-DRG). |
| 62 | `CLM_STATUS` | VARCHAR |  | The submitter's claim status (e.g., clean, denied). |
| 63 | `DRG_CODE_VERSION` | VARCHAR |  | The version of the code set that the Diagnosis Related Group (DRG) code on the claim is associated with (e.g., Version 31, Version 32) |
| 64 | `IS_CLINICALLY_INVALID_IDENT` | VARCHAR |  | The external identifier representing if the claim is clinically invalid or not. |
| 65 | `DRG_CODE_SET_IDENT` | VARCHAR |  | The external identifier representing the Diagnosis Related Group (DRG) code set. |
| 66 | `DRG_CODE_VER_IDENT` | VARCHAR |  | The external identifier representing the Diagnosis Related Group (DRG) version. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

