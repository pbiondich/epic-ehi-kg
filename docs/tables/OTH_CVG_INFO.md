# OTH_CVG_INFO

> All values associated with a claim are stored in the Claim External Value record. The OTH_CVG_INFO table holds information about the patient's other coverages that have been or will be billed for the services on the claim.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 58

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `OTH_CVG_SEQ_CD` | VARCHAR |  | This item holds the code identifying the filing order for the other coverage (primary, secondary, tertiary, etc). |
| 4 | `OTH_CVG_PAT_MEM_ID` | VARCHAR |  | This item holds the member ID for the patient on the other coverage. |
| 5 | `OTH_CVG_GRP_NUM` | VARCHAR |  | This item holds the group number entered in the other coverage record. |
| 6 | `OTH_CVG_GRP_NAM` | VARCHAR |  | This item holds the group name entered in the other coverage record. |
| 7 | `OTH_CVG_INS_TYP` | VARCHAR |  | This item holds the insurance type code for the other coverage. |
| 8 | `OTH_CVG_FILING_IND` | VARCHAR |  | This item holds an indicator identifying the type of claim if the claim was submitted to the other coverage. |
| 9 | `OTH_CVG_AUTH_PMT` | VARCHAR |  | This item holds the indicator that the insured of the other coverage assigns benefits to the provider. |
| 10 | `OTH_CVG_SIG_SRC` | VARCHAR |  | This item indicates that the release forms were signed on the patient's behalf. |
| 11 | `OTH_CVG_REL_INFO` | VARCHAR |  | This item holds the indicator that the insured of the other coverage has authorized the release of information to the payer. |
| 12 | `OTH_CVG_AMT_PAID` | NUMERIC |  | This item holds the amount already paid by the payer of the other coverage. |
| 13 | `OTH_CVG_PAT_DUE` | NUMERIC |  | This item holds the amount identified by the payer of the other coverage to be the patient's responsibility. |
| 14 | `OTH_CVG_NON_CVD` | NUMERIC |  | This item holds the amount identified as non-covered by the payer of the other coverage. |
| 15 | `OTH_PYR_NAM` | VARCHAR |  | This item holds the payer name for the other coverage. |
| 16 | `OTH_PYR_QUAL` | VARCHAR |  | This item holds a qualifier describing the ID used to identify the other payer. |
| 17 | `OTH_PYR_ID` | VARCHAR |  | This item holds the ID of the other payer. |
| 18 | `OTH_PYR_PMT_DT` | DATETIME |  | This item holds the date of the other payer's payment. |
| 19 | `OTH_PYR_AUTH_NUM` | VARCHAR |  | This item holds the other payer's authorization number. |
| 20 | `OTH_PYR_RFL_NUM` | VARCHAR |  | This item holds the other payer's referral number. |
| 21 | `OTH_PYR_ICN` | VARCHAR |  | This item holds the other payer's internal control number (ICN). |
| 22 | `OTH_PYR_ADDR_1` | VARCHAR |  | This item holds the first line of the other payer's street address. |
| 23 | `OTH_PYR_ADDR_2` | VARCHAR |  | This item holds the second line of the other payer's street address. |
| 24 | `OTH_PYR_CITY` | VARCHAR |  | This item holds the other payer's city. |
| 25 | `OTH_PYR_STATE` | VARCHAR |  | This item holds the other payer's state. |
| 26 | `OTH_PYR_ZIP` | VARCHAR |  | This item holds the other payer's ZIP code. |
| 27 | `OTH_PYR_CNTRY` | VARCHAR |  | This item holds the other payer's country. It is only populated if the address is outside the United States. |
| 28 | `OTH_PYR_CNTRY_SUB` | VARCHAR |  | This item holds the other payer's country subdivision (state, province, etc). It is only populated if the address is outside the United States. |
| 29 | `OTH_CVG_CVD_DAY` | INTEGER |  | This item holds the number of covered days identified on the other coverage's payment. |
| 30 | `OTH_CVG_PSYCH_DAY` | INTEGER |  | This item holds the number of psychiatric days identified on the other coverage's payment. |
| 31 | `OTH_CVG_DRG_AMT` | NUMERIC |  | This item holds the Diagnosis Related Group (DRG) amount identified on the other coverage's payment. |
| 32 | `OTH_CVG_DSH_AMT` | NUMERIC |  | This item holds the disproportionate share (DSH) amount identified on the other coverage's payment. |
| 33 | `OTH_CVG_MSP_AMT` | NUMERIC |  | This item holds the Medicare Secondary Payor (MSP) pass-through amount identified on the other coverage's payment. |
| 34 | `OTH_CVG_PPS_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) capital amount identified on the other coverage's payment. |
| 35 | `OTH_CVG_FSP_DRG_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) capital federal specific portion (FSP) Diagnosis Related Group (DRG) amount identified on the other coverage's payment. |
| 36 | `OTH_CVG_HSP_DRG_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) capital hospital specific portion (HSP) Diagnosis Related Group (DRG) amount identified on the other coverage's payment. |
| 37 | `OTH_CVG_DSH_DRG_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) capital disproportionate share (DSH) Diagnosis Related Group (DRG) amount identified on the other coverage's payment. |
| 38 | `OTH_CVG_CAP_AMT` | NUMERIC |  | This item holds the old capital amount identified on the other coverage's payment. |
| 39 | `OTH_CVG_IME_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) capital indirect medical education (IME) amount identified on the other coverage's payment. |
| 40 | `OTH_CVG_OHS_DRG_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) operating hospital specific portion (HSP) Diagnosis Related Group (DRG) amount identified on the other coverage's payment. |
| 41 | `OTH_CVG_COST_DAY` | INTEGER |  | This item holds the cost report days identified on the other coverage's payment. |
| 42 | `OTH_CVG_OFS_DRG_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) operating federal specific portion (FSP) Diagnosis Related Group (DRG) amount identified on the other coverage's payment. |
| 43 | `OTH_CVG_OUTLIER_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) capital outlier amount identified on the other coverage's payment. |
| 44 | `OTH_CVG_TEACH_AMT` | NUMERIC |  | This item holds the claim indirect teaching amount identified on the other coverage's payment. |
| 45 | `OTH_CVG_IP_PROF_AMT` | NUMERIC |  | This item holds the amount of the professional component billed on an inpatient claim but not payable as identified on the other coverage's payment. |
| 46 | `OTH_CVG_EXCEPT_AMT` | NUMERIC |  | This item holds the Prospective Payment System (PPS) capital exception amount identified on the other coverage's payment. |
| 47 | `OTH_CVG_REIMB_RATE` | NUMERIC |  | This item holds the reimbursement rate identified on the other coverage's payment. |
| 48 | `OTH_CVG_HCPCS_AMT` | NUMERIC |  | This item holds the Healthcare Common Procedure Coding System (HCPCS) payable amount identified on the other coverage's payment. |
| 49 | `OTH_CVG_ESRD_AMT` | NUMERIC |  | This item holds the end state renal disease (ESRD) payment amount identified on the other coverage's payment. |
| 50 | `OTH_CVG_OP_PROF_AMT` | NUMERIC |  | This item holds the amount of the professional component billed on an outpatient claim but not payable as identified on the other coverage's payment. |
| 51 | `OTH_CVG_CAS_CEV_ID` | NUMERIC |  | This item holds a pointer to an additional claim external value (CEV) record used to hold reason code (CAS) information for the claim. Only claim level values are stored in this reason code claim external value (CEV) record. |
| 52 | `OTH_PYR_TPL_PYR_CD` | VARCHAR |  | Payer code that identifies payer to Illinois Medicaid. |
| 53 | `OTH_PYR_TPL_STAT_CD` | VARCHAR |  | Status code that identifies how the other payer paid. |
| 54 | `OTH_PYR_TPL_AMOUNT` | NUMERIC |  | Payment amount made by (Third Party Liability) TPL payer. |
| 55 | `OTH_PYR_TPL_DT` | DATETIME |  | Third Party Liability (TPL) payment date. |
| 56 | `OTH_CVG_TRUPAID_AMT` | NUMERIC |  | This item is used to store the true paid amount from the other coverage payer. Does not include any adjustment amount. |
| 57 | `OTH_CVG_ADJPAID_AMT` | NUMERIC |  | This item is used to store the adjustment amount that should count as paid amount from an other coverage payor. |
| 58 | `OTH_PYR_ASST_TYP` | VARCHAR |  | The other payer's assistant dental surgeon entity type qualifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

