# SVC_LN_INFO_3

> All values associated with a claim are stored in the Claim External Value record. The SVC_LN_INFO_3 table holds information about the service lines on the claim.

**Overflow of:** [SVC_LN_INFO](SVC_LN_INFO.md)  
**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 75

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LN_INGRED_COST_PAID` | NUMERIC |  | Drug ingredient cost paid. |
| 4 | `LN_DISP_FEE_PAID` | NUMERIC |  | Dispensing fee paid. |
| 5 | `LN_PAT_PAY_AMT` | NUMERIC |  | Patient pay amount. |
| 6 | `LN_COPAY_AMT` | NUMERIC |  | Amount of patient copay. |
| 7 | `LN_COINS_AMT` | NUMERIC |  | Amount of patient coinsurance. |
| 8 | `LN_DEDUCT_AMT` | NUMERIC |  | Amount of patient deductible. |
| 9 | `LN_REGLTRY_FEE_AMT` | NUMERIC |  | Flat sales tax amount paid. |
| 10 | `LN_PCT_TAX_AMT` | NUMERIC |  | Percentage tax amount paid. |
| 11 | `LN_INCENTIVE_AMT` | NUMERIC |  | Incentive amount paid. |
| 12 | `LN_OTHR_AMT_RECOGZ` | NUMERIC |  | Total amount recognized by the processor of any payment from another source. |
| 13 | `LN_NET_AMT_DUE` | NUMERIC |  | Net amount paid to provider by the payer. |
| 14 | `LN_DENT_PROS_QUAL` | VARCHAR |  | This item holds a code indicating if the date for a prior crown/prosthesis is estimated or exact. |
| 15 | `LN_DENT_PROS_DATE` | DATETIME |  | The date a prior crown/prosthesis was previously placed. |
| 16 | `SVC_DENIED_STATUS_IDENT` | VARCHAR |  | This stores the external identifier for the denial status of this line. |
| 17 | `PRCS_IND_CD` | VARCHAR |  | Claim line level processing indicator code. |
| 18 | `PRCS_IND_CD_DESC` | VARCHAR |  | Claim line level processing indicator code description. |
| 19 | `LN_OPR_TAXONOMY` | VARCHAR |  | Stores the Line Operating Provider Taxonomy Code. |
| 20 | `LN_APPLIANCE_REPLACEMENT_DATE` | DATETIME |  | The date when an orthodontic appliance was replaced. |
| 21 | `LN_TREATMENT_START_DATE` | DATETIME |  | The date of the initial treatment for a dental service. |
| 22 | `LN_TREATMENT_COMPLETION_DATE` | DATETIME |  | The date of the completed treatment for a dental service. |
| 23 | `LN_FILL_STATUS` | VARCHAR |  | Stores information on whether the prescription was completely or partially filled. |
| 24 | `LN_ORD_TAXONOMY` | VARCHAR |  | Stores the National Uniform Claim Committee (NUCC) taxonomy code associated with the line-level operating provider |
| 25 | `LN_APPLIANCE_PLACEMENT_DATE` | DATETIME |  | The date when the orthodontic appliance was placed. |
| 26 | `LN_LIN_QUALIFIER` | VARCHAR |  | Qualifier code to identify drug code set or the type/source of the descriptive number used in Product/Service ID. |
| 27 | `LN_PRESC_PROV_NPI` | VARCHAR |  | This column holds the National Provider Identifier (NPI) of the provider that prescribed the medication on this service. |
| 28 | `LN_PRESC_PROV_TAXONOMY` | VARCHAR |  | This column holds the NUCC Taxonomy Code of the provider that prescribed the medication on this service. |
| 29 | `LN_SERV_PROV_NPI` | VARCHAR |  | This item holds the National Provider Identifier (NPI) of the pharmacy that filled the prescription. |
| 30 | `LN_SERV_PROV_TAXONOMY` | VARCHAR |  | This column holds the NUCC Taxonomy Code of the pharmacy that filled the prescription. |
| 31 | `LN_DX_PTR_RANK` | VARCHAR |  | The comma-delimited list of diagnoses ranks for each diagnosis on a service. Each position here corresponds to the same comma-delimited position of the column LN_DX_PTR from the SVC_LN_INFO table. The rank here specifies the ranking of diagnoses for the specific service. This can be different than the rank of the same diagnoses at the header-level or even the same diagnoses for a different service. |
| 32 | `LN_PCP_REF_LAST_NM` | VARCHAR |  | This item stores the line's PCP referring provider's last name. |
| 33 | `LN_PCP_REF_FIRST_NM` | VARCHAR |  | This item stores the line's PCP referring provider's first name. |
| 34 | `LN_PCP_REF_MID_NM` | VARCHAR |  | This item stores the line's PCP referring provider's middle name. |
| 35 | `LN_PCP_REF_SUFFIX_NM` | VARCHAR |  | This item stores the line's PCP referring provider's suffix. |
| 36 | `LN_PCP_REF_NPI` | VARCHAR |  | This item stores the line's PCP referring provider's NPI. |
| 37 | `RX_DATE` | DATETIME |  | The date when the prescription was written. |
| 38 | `SUB_CLAR_CODE` | VARCHAR |  | The code indicating that the pharmacist is clarifying the submission. |
| 39 | `RX_ORIGIN_CODE` | VARCHAR |  | The code indicating the origin of the prescription. |
| 40 | `RX_PHARM_SRV_TYPE` | VARCHAR |  | The type of service being performed by a pharmacy when different contractual terms exist between a payer and the pharmacy, or when benefits are based upon the type of service performed. |
| 41 | `RX_PROD_DESC` | VARCHAR |  | The description of the product being submitted on the prescription claim. |
| 42 | `OTHER_CVG_CODE` | VARCHAR |  | The code indicating whether or not the patient has other insurance coverage. |
| 43 | `RX_SERVICE_LEVEL` | VARCHAR |  | The code indicating the type of service the provider rendered. |
| 44 | `QTY_PRESCRIBED` | NUMERIC |  | The quantity of prescription drug expressed in metric decimal units. |
| 45 | `REASON_SVC_CODE` | VARCHAR |  | The code identifying the type of utilization conflict detected or the reason for the pharmacist's professional service. |
| 46 | `PROF_SRVC_CODE` | VARCHAR |  | The code identifying pharmacist intervention when a conflict code has been identified or service has been rendered. |
| 47 | `RES_SVC_CODE` | VARCHAR |  | The code describing a pharmacist's action in response to a professional conflict. |
| 48 | `LEVEL_OF_EFFORT` | VARCHAR |  | The code indicating the level of effort as determined by the complexity of decision-making or resources utilized by a pharmacist to perform a professional service. |
| 49 | `DOSAGE_FORM_DESC_CD` | VARCHAR |  | The dosage form of the complete compound mixture. |
| 50 | `DISP_UNIT_FORM_INDICATOR` | VARCHAR |  | The NCPDP standard product billing codes. |
| 51 | `ADMIN_ROUTE` | VARCHAR |  | An override to the "default" route referenced for the product. For a multi-ingredient compound, it is the route of the complete compound mixture. |
| 52 | `INGREDIENT_COMPOUND_CNT` | INTEGER |  | The count of compound product IDs (both active and inactive) in the compound mixture submitted. |
| 53 | `USUAL_CUSTOMARY_CHG` | INTEGER |  | The amount charged to cash customers for the prescription exclusive of sales tax or other amounts claimed. |
| 54 | `COST_BASIS` | VARCHAR |  | The code indicating the method used to calculate the ingredient cost. |
| 55 | `INGREDIENT_COST_SUBMITTED` | NUMERIC |  | The product component cost of the dispensed prescription. |
| 56 | `DISP_FEE_SUBMITTED` | NUMERIC |  | The dispensing fee submitted by the pharmacy. |
| 57 | `PROF_FEE_SUBMITTED` | NUMERIC |  | The amount submitted by the provider for professional services rendered. |
| 58 | `INGREDIENT_AMT_SUBMITTED` | NUMERIC |  | The amount representing the fee that is submitted by the pharmacy for contractually agreed upon services. |
| 59 | `OTHER_AMT_SUBMITTED` | NUMERIC |  | The amount representing the additional incurred costs for a dispensed prescription or service. |
| 60 | `GROSS_AMOUNT_DUE` | NUMERIC |  | The total gross amount submitted on the claim. |
| 61 | `LN_PICK_UP_CNTY` | VARCHAR |  | County in which the ambulance pick-up occured. |
| 62 | `LN_DROP_OFF_CNTY` | VARCHAR |  | Stores the Line Ambulance Drop-Off Location County |
| 63 | `LN_START_LOCAL_DTTM` | DATETIME (Local) |  | Stores the line service start time. |
| 64 | `LN_END_LOCAL_DTTM` | DATETIME (Local) |  | Stores the end time for the service. |
| 65 | `LN_ELAPSED_TIME` | VARCHAR |  | Stores the time between the start and end time for the service. |
| 66 | `SECTION_340B` | VARCHAR |  | Section 340B Program Participant - if drug was dispensed under 340B program (yes/no) |
| 67 | `ACTIVITY_TCN` | VARCHAR |  | This item stores the Activity ID of a single activity line on the claim. |
| 68 | `ACTIVITY_VAT_PERCENT` | NUMERIC |  | This item stores the VAT percent for a single activity line on the claim. |
| 69 | `ACTIVITY_CODE` | VARCHAR |  | This item stores the Activity code of a single activity line on the claim. |
| 70 | `ACTIVITY_START_DATE` | DATETIME |  | This item stores the activity start date of a single activity line on the claim. |
| 71 | `LN_SERV_PROV_NAME` | VARCHAR |  | The freetext name of the service provider. |
| 72 | `REVENUE_APC_CODE` | VARCHAR |  | The provider-assigned revenue code for each cost center for which a separate charge is billed. |
| 73 | `LINE_PRIMARY_PAYER_CODE` | VARCHAR |  | The code specifying a federal non-Medicare program or other source that has primary responsibility for the payment of the Medicare beneficiary's medical bills relating to the service line on the claim. The presence of this code indicates that some other payer besides Medicare covered at least some portion of the charges. |
| 74 | `LINE_HCPCS_BETOS_CODE` | VARCHAR |  | The Berenson-Eggers Type of Service (BETOS) classification assigned to the Healthcare Common Procedure Coding System (HCPCS) code for the service line. |
| 75 | `LINE_FEDERAL_SERVICE_CODE` | VARCHAR |  | Code indicating the type of service, as defined in the CMS Medicare Carrier Manual, for this line item on the non-institutional claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

