# SVC_LN_INFO

> All values associated with a claim are stored in the Claim External Value record. The SVC_LN_INFO table holds information about the service lines on the claim.

**Overflow family:** [SVC_LN_INFO_2](SVC_LN_INFO_2.md), [SVC_LN_INFO_3](SVC_LN_INFO_3.md)  
**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 88

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `LN_FROM_DT` | DATETIME |  | This item holds the earliest service date represented on the line. |
| 4 | `LN_TO_DT` | DATETIME |  | This item holds the latest service date represented on the line. It will not be populated if the line only represents a single date. |
| 5 | `LN_PROC_QUAL` | VARCHAR |  | This item holds a code identifying the type of procedure code reported on the line. |
| 6 | `LN_PROC_CD` | VARCHAR |  | This item holds the procedure code for the line. |
| 7 | `LN_PROC_DESC` | VARCHAR |  | This item holds a procedure specific description for the line. |
| 8 | `LN_PROC_MOD` | VARCHAR |  | This item holds a comma delimited list of modifiers for the procedure on the line. |
| 9 | `LN_QTY_QUAL` | VARCHAR |  | This item holds a code identifying the unit in which the quantity is reported. |
| 10 | `LN_QTY` | NUMERIC |  | This item holds the quantity for the service line. |
| 11 | `LN_AMT` | NUMERIC |  | This item holds the billed amount for the line. For Uniform Billing (UB) claims, this amount will include both covered and non-covered amounts. |
| 12 | `LN_REV_CD` | VARCHAR |  | This item holds the revenue code for the service line. |
| 13 | `LN_REV_CD_DESC` | VARCHAR |  | This item holds a revenue code specific description for the line. |
| 14 | `LN_RATE` | NUMERIC |  | This item holds the daily rate for accommodation revenue code lines. |
| 15 | `LN_NON_CVD_AMT` | NUMERIC |  | This item holds the non-covered amount for the line. |
| 16 | `LN_POS_CD` | VARCHAR |  | This item holds the place of service code identifying where the service on the line was performed. |
| 17 | `LN_DX_PTR` | VARCHAR |  | This item holds a comma delimited list of diagnosis pointers. Each piece of the string is a line number from the claim diagnosis table. |
| 18 | `LN_EMERG_IND` | VARCHAR |  | This item identifies the service on the line as an emergency service. |
| 19 | `LN_EPSDT_IND` | VARCHAR |  | This item identifies the service on the line as an Early & Periodic Screening, Diagnosis, and Treatment (EPSDT) service. |
| 20 | `LN_FAM_PLAN_IND` | VARCHAR |  | This item identifies the service on the line as a family planning service. |
| 21 | `LN_COPAY_STAT_CD` | VARCHAR |  | This item identifies when the patient was exempt from a copay for the service on the line. |
| 22 | `LN_AMB_PAT_CNT` | INTEGER |  | This item holds the number of patients transported in the ambulance when the line represents an ambulance service. |
| 23 | `LN_MAMM_CERT_NUM` | VARCHAR |  | This item holds the mammography certification number for the line. |
| 24 | `LN_CLIA_NUM` | VARCHAR |  | This item holds the Clinical Laboratory Improvement Amendment (CLIA) number for the line. |
| 25 | `LN_ORAL_CAV_CD` | VARCHAR |  | This item holds a comma delimited list of oral cavity codes for the line. |
| 26 | `LN_DENT_PROSTHESIS` | VARCHAR |  | This item holds a code to indicate the initial placement or replacement of a dental prosthesis, crown, or inlay. |
| 27 | `LN_DME_CMN_CD` | VARCHAR |  | This item holds a code describing how the certificate of medical necessity (CMN) for the line was transmitted to the DMERC. |
| 28 | `LN_DME_CERT_TYP` | VARCHAR |  | This item identifies the type of certification (initial, renewal, or revised) applies to the line. |
| 29 | `LN_DME_DURATION` | INTEGER |  | This item holds the number of months the durable medical equipment (DME) supplies will be needed. |
| 30 | `LN_DME_RECERT_DT` | DATETIME |  | This item holds the new durable medical equipment (DME) certification date when the certification type is renewed or revised. |
| 31 | `LN_CME_BEG_THRPY_DT` | DATETIME |  | This item holds the date that therapy requiring the durable medical equipment (DME) began. |
| 32 | `LN_DME_COND_IND` | VARCHAR |  | This item holds a comma delimited list of durable medical equipment (DME) condition codes for the service line. |
| 33 | `LN_CNTRCT_TYP` | VARCHAR |  | This item holds a code representing the type of contract between the provider and the payer used for the service line. |
| 34 | `LN_CNTRCT_AMT` | NUMERIC |  | This item holds the contract amount for the line. |
| 35 | `LN_CNTRCT_PCT` | NUMERIC |  | This item holds the contract percentage for the line. |
| 36 | `LN_CNTRCT_CD` | VARCHAR |  | This item holds a code representing the line. |
| 37 | `LN_CNTRCT_DISCNT_P` | NUMERIC |  | This item holds the discount percentage for the line. |
| 38 | `LN_CNTRCT_VERS_ID` | VARCHAR |  | This item identifies the version of the contract used for the line. |
| 39 | `LN_NDC` | VARCHAR |  | This item holds the National Drug Code (NDC) for the service line. |
| 40 | `LN_NDC_UNIT_QTY` | NUMERIC |  | This item holds the quantity associated with the National Drug Code (NDC), in terms of the units reported with the NDC. |
| 41 | `LN_NDC_UNIT` | VARCHAR |  | This item holds the units associated with the National Drug Code (NDC). |
| 42 | `LN_RX_NUM_QUAL` | VARCHAR |  | This item holds a code distinguishing prescription numbers from sequence numbers used to represent compound drugs. |
| 43 | `LN_RX_NUM` | VARCHAR |  | This item holds the prescription number for the line. |
| 44 | `LN_NOTE` | VARCHAR |  | This item holds a line level note. |
| 45 | `LN_REND_PROV_TYP` | VARCHAR |  | This item indicates whether the rendering provider on the line is a person or a non-person. |
| 46 | `LN_REND_NAM_LAST` | VARCHAR |  | This item holds the rendering provider's last name (if a person) or the organization name (if a non-person). |
| 47 | `LN_REND_NAM_FIRST` | VARCHAR |  | This item holds the rendering provider's first name. It is only populated when the provider is a person. |
| 48 | `LN_REND_NAM_MID` | VARCHAR |  | This item holds the rendering provider's middle name. It is only populated when the provider is a person. |
| 49 | `LN_REND_NAM_SUF` | VARCHAR |  | This item holds the suffix to the rendering provider's name (Jr, III, etc). It is only populated when the provider is a person. |
| 50 | `LN_REND_NPI` | VARCHAR |  | This item holds the rendering provider's National Provider Identifier (NPI). |
| 51 | `LN_REND_TAXONOMY` | VARCHAR |  | This item holds the rendering provider's taxonomy code. |
| 52 | `LN_SVC_FAC_NAM` | VARCHAR |  | This item holds the name of the external location where the services were performed. |
| 53 | `LN_SVC_FAC_NPI` | VARCHAR |  | This item holds the National Provider Identifier (NPI) of the external location where the services were performed. |
| 54 | `LN_SVC_FAC_ADDR_1` | VARCHAR |  | This item holds the first line of the external location street address. |
| 55 | `LN_SVC_FAC_ADDR_2` | VARCHAR |  | This item holds the second line of the external location street address. |
| 56 | `LN_SVC_FAC_CITY` | VARCHAR |  | This item holds the external location's city. |
| 57 | `LN_SVC_FAC_STATE` | VARCHAR |  | This item holds the external location's state. |
| 58 | `LN_SVC_FAC_ZIP` | VARCHAR |  | This item holds the external location's ZIP code. |
| 59 | `LN_SVC_FAC_CNTRY` | VARCHAR |  | This item holds the external location's country. It is only populated if the address is outside the United States. |
| 60 | `LN_SVC_FAC_CNTRY_SU` | VARCHAR |  | This item holds the external location's country subdivision (state, province, etc). It is only populated if the address is outside the United States. |
| 61 | `LN_SUP_NAM_LAST` | VARCHAR |  | This item holds the supervising provider's last name. |
| 62 | `LN_SUP_NAM_FIRST` | VARCHAR |  | This item holds the supervising provider's first name. |
| 63 | `LN_SUP_NAM_MID` | VARCHAR |  | This item holds the supervising provider's middle name. |
| 64 | `LN_SUP_NAM_SUF` | VARCHAR |  | This item holds the suffix to the supervising provider's name (Jr, III, etc). |
| 65 | `LN_SUP_NPI` | VARCHAR |  | This item holds the supervising provider's National Provider Identifier (NPI). |
| 66 | `LN_ORD_NAM_LAST` | VARCHAR |  | This item holds the ordering provider's last name. |
| 67 | `LN_ORD_NAM_FIRST` | VARCHAR |  | This item holds the ordering provider's first name. |
| 68 | `LN_ORD_NAM_MID` | VARCHAR |  | This item holds the ordering provider's middle name. |
| 69 | `LN_ORD_NAM_SUF` | VARCHAR |  | This item holds the suffix to the ordering provider's name (Jr, III, etc). |
| 70 | `LN_ORD_NPI` | VARCHAR |  | This item holds the ordering provider's National Provider Identifier (NPI). |
| 71 | `LN_ORD_ADDR_1` | VARCHAR |  | This item holds the first line of the ordering provider's street address. |
| 72 | `LN_ORD_ADDR_2` | VARCHAR |  | This item holds the second line of the ordering provider's street address. |
| 73 | `LN_ORD_CITY` | VARCHAR |  | This item holds the ordering provider's city. |
| 74 | `LN_ORD_STATE` | VARCHAR |  | This item holds the ordering provider's state. |
| 75 | `LN_ORD_ZIP` | VARCHAR |  | This item holds the ordering provider's ZIP code. |
| 76 | `LN_ORD_CNTRY` | VARCHAR |  | This item holds the ordering provider's country. It is only populated if the address is outside the United States. |
| 77 | `LN_ORD_CNTRY_SUB` | VARCHAR |  | This item holds the ordering provider's country subdivision (state, province, etc). It is only populated if the address is outside the United States. |
| 78 | `LN_PURCH_PROV_TYP` | VARCHAR |  | This item indicates whether the purchased service provider on the line is a person or a non-person. |
| 79 | `LN_PURCH_NPI` | VARCHAR |  | This item holds the purchased service provider's National Provider Identifier (NPI). |
| 80 | `LN_ASST_TYP` | VARCHAR |  | This item indicates whether the assistant dental surgeon on the line is a person or a non-person. |
| 81 | `LN_ASST_NAM_LAST` | VARCHAR |  | This item holds the assistant dental surgeon's last name (if a person) or the organization name (if a non-person). |
| 82 | `LN_ASST_NAM_FIRST` | VARCHAR |  | This item holds the assistant dental surgeon's first name. It is only populated when the provider is a person. |
| 83 | `LN_ASST_NAM_MID` | VARCHAR |  | This item holds the assistant dental surgeon's middle name. It is only populated when the provider is a person. |
| 84 | `LN_ASST_NAM_SUF` | VARCHAR |  | This item holds the suffix to the assistant dental surgeon's name (Jr, III, etc). It is only populated when the provider is a person. |
| 85 | `LN_ASST_NPI` | VARCHAR |  | This item holds the assistant dental surgeon's National Provider Identifier (NPI). |
| 86 | `LN_ASST_TAXONOMY` | VARCHAR |  | This item holds the assistant dental surgeon's taxonomy code. |
| 87 | `LN_DOC_TYP` | VARCHAR |  | This item holds a code indicating the type of supporting document included with the service line. |
| 88 | `LN_DOC_FORM_ID` | VARCHAR |  | This item identifies the specific document. For example, this can identify the version number of a questionnaire so that the payer can correctly interpret the responses. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

