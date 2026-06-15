# CLM_VALUES

> All values associated with a claim are stored in the Claim External Value record. The CLM_VALUES table holds claim-level values set by the system during claims processing or by user edits.

**Overflow family:** [CLM_VALUES_2](CLM_VALUES_2.md), [CLM_VALUES_3](CLM_VALUES_3.md), [CLM_VALUES_4](CLM_VALUES_4.md), [CLM_VALUES_5](CLM_VALUES_5.md), [CLM_VALUES_6](CLM_VALUES_6.md)  
**Primary key:** `RECORD_ID`  
**Columns:** 69

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim record. |
| 2 | `BIL_PROV_TYP_QUAL` | VARCHAR |  | The value indicating whether the billing provider on the claim is a person or a non-person. |
| 3 | `BIL_PROV_NAM_LAST` | VARCHAR |  | The billing provider's last name (if a person) or the organization name (if a non-person). |
| 4 | `BIL_PROV_NAM_FIRST` | VARCHAR |  | The billing provider's first name. It is only populated when the billing provider is a person. |
| 5 | `BIL_PROV_NAM_MID` | VARCHAR |  | The billing provider's middle name. It is only populated when the billing provider is a person. |
| 6 | `BIL_PROV_NAM_SUF` | VARCHAR |  | The suffix to the billing provider's name (e.g., Jr, III). It is only populated when the billing provider is a person. |
| 7 | `BIL_PROV_NPI` | VARCHAR |  | The billing provider's National Provider Identifier (NPI). |
| 8 | `BIL_PROV_TAXONOMY` | VARCHAR |  | The billing provider's taxonomy code. |
| 9 | `BIL_PROV_TAXID_QUAL` | VARCHAR |  | The qualifier for the billing provider's tax ID defining the type of ID reported as the tax ID. |
| 10 | `BIL_PROV_TAXID` | VARCHAR |  | The billing provider's tax ID. For individuals, this ID could be the SSN or tax ID. |
| 11 | `BIL_PROV_UPIN` | VARCHAR |  | The billing provider's unique physician identification number (UPIN). It is only populated when the provider is a person. |
| 12 | `BIL_PROV_LIC_NUM` | VARCHAR |  | The billing provider's license number. It is only populated when the billing provider is a person. |
| 13 | `BIL_PROV_ADDR_1` | VARCHAR |  | The first line of the billing provider's street address. |
| 14 | `BIL_PROV_ADDR_2` | VARCHAR |  | The second line of the billing provider's street address. |
| 15 | `BIL_PROV_CITY` | VARCHAR |  | The billing provider's city. |
| 16 | `BIL_PROV_STATE` | VARCHAR |  | The billing provider's state. |
| 17 | `BIL_PROV_ZIP` | VARCHAR |  | The billing provider's ZIP Code. |
| 18 | `BIL_PROV_CNTRY` | VARCHAR |  | The billing provider's country. It is only populated if the address is outside the United States. |
| 19 | `BIL_PROV_CNTRY_SUB` | VARCHAR |  | The billing provider's country subdivision (e.g., state, province). It is only populated if the address is outside the United States. |
| 20 | `CLM_CVG_SEQ_CD` | VARCHAR |  | The code identifying the filing order for the claim (e.g., primary, secondary, tertiary). |
| 21 | `CLM_CVG_PYR_NAM` | VARCHAR |  | The payer name. |
| 22 | `CLM_CVG_GRP_NUM` | VARCHAR |  | The group number entered in the coverage record. |
| 23 | `CLM_CVG_GRP_NAM` | VARCHAR |  | The group name entered in the coverage record. |
| 24 | `CLM_CVG_INS_TYP` | VARCHAR |  | The insurance type code for the claim. |
| 25 | `CLM_CVG_FILING_IND` | VARCHAR |  | The indicator identifying the type of claim. |
| 26 | `CLM_CVG_PYR_ID_TYP` | VARCHAR |  | The qualifier that describes the type of ID used to identify the payer. |
| 27 | `CLM_CVG_PYR_ID` | VARCHAR |  | The primary ID for the payer. |
| 28 | `CLM_CVG_ACPT_ASGN` | VARCHAR |  | The indicator that the provider accepts assignment from the payer. |
| 29 | `CLM_CVG_AUTH_PMT` | VARCHAR |  | The indicator that the insured assigns benefits to the provider. |
| 30 | `CLM_CVG_REL_INFO` | VARCHAR |  | The indicator that the insured has authorized the release of information to the payer. |
| 31 | `PYR_ADDR_1` | VARCHAR |  | The first line of the payer's street address. |
| 32 | `PYR_ADDR_2` | VARCHAR |  | The second line of the payer's street address. |
| 33 | `PYR_CITY` | VARCHAR |  | The payer's city. |
| 34 | `PYR_STATE` | VARCHAR |  | The payer's state. |
| 35 | `PYR_ZIP` | VARCHAR |  | The payer's ZIP Code. |
| 36 | `PYR_CNTRY` | VARCHAR |  | The payer's country. It is only populated if the address is outside the United States. |
| 37 | `PYR_CNTRY_SUB` | VARCHAR |  | The payer's country subdivision (e.g., state, province). It is only populated if the address is outside the United States. |
| 38 | `PAT_NAM_LAST` | VARCHAR |  | The patient's last name. |
| 39 | `PAT_NAM_FIRST` | VARCHAR |  | The patient's first name. |
| 40 | `PAT_NAM_MID` | VARCHAR |  | The patient's middle name. |
| 41 | `PAT_NAM_SUF` | VARCHAR |  | The suffix to the patient's name (e.g., Jr, III). |
| 42 | `PAT_MRN` | VARCHAR |  | The patient's medical record number. |
| 43 | `PAT_CVG_MEM_ID` | VARCHAR |  | The coverage member ID for the patient. |
| 44 | `PAT_REL_TO_INS` | VARCHAR |  | The patient's relationship to the coverage subscriber. |
| 45 | `PAT_BIRTH_DATE` | DATETIME |  | The patient's birthdate. |
| 46 | `PAT_SEX` | VARCHAR |  | The patient's gender. |
| 47 | `PAT_SIG_ON_FILE` | VARCHAR |  | The indicator that the patient has signed the necessary release forms and the forms are on file at the provider. |
| 48 | `PAT_SIG_SRC` | VARCHAR |  | The indicator that the release forms were signed on the patient's behalf. |
| 49 | `PAT_DEATH_DATE` | DATETIME |  | The date of the patient's death. |
| 50 | `PAT_WT` | NUMERIC |  | The patient's weight (in pounds) when needed for the claim. |
| 51 | `PAT_PREG_IND` | VARCHAR |  | The indicator that the patient is pregnant. |
| 52 | `PAT_WK_COMP_NUM` | VARCHAR |  | The identification number used for workers' comp claims. |
| 53 | `PAT_MAR_STAT` | VARCHAR |  | The patient's marital status. |
| 54 | `PAT_EMPY_STAT` | VARCHAR |  | The patient's employment status. |
| 55 | `PAT_PH` | VARCHAR |  | The patient's phone number. |
| 56 | `PAT_ADDR_1` | VARCHAR |  | The first line of the patient's street address. |
| 57 | `PAT_ADDR_2` | VARCHAR |  | The second line of the patient's street address. |
| 58 | `PAT_CITY` | VARCHAR |  | The patient's city. |
| 59 | `PAT_STATE` | VARCHAR |  | The patient's state. |
| 60 | `PAT_ZIP` | VARCHAR |  | The patient's ZIP Code. |
| 61 | `PAT_CNTRY` | VARCHAR |  | The patient's country. It is only populated if the address is outside the United States. |
| 62 | `PAT_CNTRY_SUB` | VARCHAR |  | The patient's country subdivision (e.g., state, province). It is only populated if the address is outside the United States. |
| 63 | `INV_NUM` | VARCHAR |  | The invoice number that uniquely identifies the claim in the billing system. |
| 64 | `ICN` | VARCHAR |  | The payer's internal control number (ICN) that uniquely identifies the claim in the payer's system. |
| 65 | `TTL_CHG_AMT` | NUMERIC |  | The total charge amount for the claim. |
| 66 | `BILL_TYP_FAC_CD` | VARCHAR |  | The facility code portion of the bill type (first and second digits). |
| 67 | `BILL_TYP_FREQ_CD` | VARCHAR |  | The frequency code portion of the bill type (third digit). |
| 68 | `MOMS_MRN` | VARCHAR |  | The mother's medical record number when the patient is a newborn. |
| 69 | `PAYTO_ADDR_TYP_QUAL` | VARCHAR |  | The indicator that the pay-to address entity on the claim is a person or a non-person. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

