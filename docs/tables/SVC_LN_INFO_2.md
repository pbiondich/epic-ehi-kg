# SVC_LN_INFO_2

> All values associated with a claim are stored in the Claim External Value record. The SVC_LN_INFO_2 table holds information about the service lines on the claim.

**Overflow of:** [SVC_LN_INFO](SVC_LN_INFO.md)  
**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 92

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `LN_TOS` | VARCHAR |  | This item holds the type of service for the procedure on the service line. |
| 4 | `LN_DATE_QUAL` | VARCHAR |  | This item holds a qualifier to distinguish between a single date (when the from and to dates are the same) and a date range (when the from and to dates are different). |
| 5 | `LN_PURCH_SERV_AMT` | NUMERIC |  | This item holds the purchased service charge amount for the line. |
| 6 | `LN_REFERRING_CLIA` | VARCHAR |  | This item holds the Clinical Laboratory Improvement Amendment (CLIA) number of the referring lab for the line. |
| 7 | `LN_HOSPICE_EMP_IND` | VARCHAR |  | This item holds the Hospice Employee Indicator. |
| 8 | `LN_HOSPICE_COND_IND` | VARCHAR |  | This item holds the Hospice Condition Indicator. |
| 9 | `LN_TTL_AMT_PAID` | NUMERIC |  | This item holds the total amount paid for the line by all payers. This item is populated for both paper and electronic Professional Billing Centers for Medicare and Medicaid Services (CMS) claims but is only used when printing paper claims. |
| 10 | `LN_ADJR_ITM_REF_NUM` | VARCHAR |  | This item stores the Adjusted Repriced Line Item Reference Number. |
| 11 | `LN_SERV_TAX_AMT` | NUMERIC |  | This item stores the line's Service Tax Amount. |
| 12 | `LN_FAC_TAX_AMT` | NUMERIC |  | This item stores the line's Facility Tax Amount. |
| 13 | `LN_REP_ITM_REF_NUM` | VARCHAR |  | This item stores the Repriced Line Item Reference Number. |
| 14 | `LN_PRC_METHOD` | VARCHAR |  | This item stores the Line Pricing Methodology. |
| 15 | `LN_ALLOWED_AMT` | NUMERIC |  | This item stores the Line Allowed Amount. |
| 16 | `LN_SAVINGS_AMT` | NUMERIC |  | This item stores the Line Savings Amount. |
| 17 | `LN_REP_ORG_ID` | VARCHAR |  | This item stores the Line Repricing Organization Identification Number. |
| 18 | `LN_PRICING_RATE` | NUMERIC |  | This item stores the Line Pricing Rate. |
| 19 | `LN_APPRVED_DRG_CODE` | VARCHAR |  | This item stores the Line's Approved diagnosis related group (DRG) Code. |
| 20 | `LN_APP_DRG_AMT` | NUMERIC |  | This item stores the Line Approved diagnosis related group (DRG) Code. |
| 21 | `LN_APP_REV_CODE` | VARCHAR |  | This item stores the Line Approved Revenue Code. |
| 22 | `LN_REPAPR_HCPCS_QL` | VARCHAR |  | This item stores the Line Repriced Approved Healthcare common Procedure Coding System (HCPS). |
| 23 | `LN_REPAPP_HCPCS` | VARCHAR |  | This item stores the Line Repriced Approved (Healthcare Common Procedure Coding System (HCPCS) Code. |
| 24 | `LN_UNIT_MSRMNT_CODE` | VARCHAR |  | This item stores the Line Unit or Basis for Measurement Code. |
| 25 | `LN_APR_SVC_UNT` | NUMERIC |  | This item stores the Line Approved Service Units or Inpatient Days. |
| 26 | `LN_OPR_SER_ETQ` | VARCHAR |  | This item stores the Entity Type Qualifier for line's Operating Physician ID. |
| 27 | `LN_OPR_LAST_NAME` | VARCHAR |  | This item stores the line's Operating Physician's Last Name. |
| 28 | `LN_OPR_FIRST_NAME` | VARCHAR |  | This item stores the line's Operating Physician's First Name. |
| 29 | `LN_OPR_MID_NAME` | VARCHAR |  | This item stores the line's Operating Physician's Middle Name. |
| 30 | `LN_OPR_NAME_SUFFIX` | VARCHAR |  | This item stores the line's Operating Physician's Name Suffix. |
| 31 | `LN_OPR_NPI` | VARCHAR |  | This item stores the line's Operating Physician's ID. |
| 32 | `LN_OTH_OPR_ETQ` | VARCHAR |  | This item stores the qualifier for line's Other Operating Physician. |
| 33 | `LN_OTH_OPR_LAST_NM` | VARCHAR |  | This item stores the line's Other Operating Physician's Last Name. |
| 34 | `LN_OTH_OPR_FIRST_NM` | VARCHAR |  | This items stores the line's Other Operating Physician's First Name. |
| 35 | `LN_OTH_OPR_MID_NM` | VARCHAR |  | This item stores the line's Other Operating Physician's Middle Name. |
| 36 | `LN_OTH_OPR_SUF_NM` | VARCHAR |  | This item stores the line's Other Operating Physician's Name Suffix. |
| 37 | `LN_OTH_OPR_NPI` | VARCHAR |  | This item stores the line's Other Operating Physician ID. |
| 38 | `LN_REF_ETQ` | VARCHAR |  | This item stores the line's Referring Provider's Entity Type Qualifier. |
| 39 | `LN_REF_LAST_NM` | VARCHAR |  | This item stores the line's Referring Provider's Last Name. |
| 40 | `LN_REF_FIRST_NM` | VARCHAR |  | This item stores line's Referring Provider's First Name. |
| 41 | `LN_REF_MID_NM` | VARCHAR |  | This item stores the line's Referring Provider's Middle Name. |
| 42 | `LN_REF_SUFFIX_NM` | VARCHAR |  | This item stores the line's Referring Provider's Name Suffix. |
| 43 | `LN_REF_NPI` | VARCHAR |  | This item stores the line's Referring Provider's National Provider Identifier (NPI). |
| 44 | `LN_DME_PROC_CD` | VARCHAR |  | Stores Line durable medical equipment (DME) Procedure Code |
| 45 | `LN_DME_QTY` | NUMERIC |  | Stores Line durable medical equipment (DME) Length of Medical Necessity |
| 46 | `LN_DME_RENTAL_PRICE` | NUMERIC |  | Stores Line durable medical equipment (DME) Rental Unit Price Indicator |
| 47 | `LN_DME_PUR_PRICE` | NUMERIC |  | Stores Line durable medical equipment (DME) Purchase Price |
| 48 | `LN_DME_RUP_IND` | VARCHAR |  | Stores Line DME Rental Unit Price Indicator |
| 49 | `LN_AMB_PAT_WT` | NUMERIC |  | Stores Line Ambulance Patient Weight |
| 50 | `LN_AMB_TRANS_RSN_CD` | VARCHAR |  | Stores Line Ambulance Transport Reason Code |
| 51 | `LN_AMB_TRANS_DIST` | NUMERIC |  | Stores Line Ambulance Transport Distance |
| 52 | `LN_AMB_RND_TRIP_DES` | VARCHAR |  | Stores Line Ambulance Round Trip Purpose Description |
| 53 | `LN_AMB_STRETCH_DESC` | VARCHAR |  | Stores Line Ambulance Stretcher Purpose Description |
| 54 | `LN_RX_DT` | DATETIME |  | Stores Line Prescription Date |
| 55 | `LN_LST_CERT_DT` | DATETIME |  | Stores Line Last Certification Date |
| 56 | `LN_LST_SEEN_DT` | DATETIME |  | Stores Line Last Seen Date |
| 57 | `LN_SHIPPED_DT` | DATETIME |  | Stores Line Shipped Date |
| 58 | `LN_LST_XRAY_DT` | DATETIME |  | Stores Line Last X-Ray Date |
| 59 | `LN_INIT_TREAT_DT` | DATETIME |  | Stores Line Initial Treatment Date |
| 60 | `LN_OBS_ADDL_UNTS` | NUMERIC |  | Stores Line Obstetric Additional Units |
| 61 | `LN_IMMNZTN_BAT_NUM` | VARCHAR |  | Stores Line Immunization Batch Number |
| 62 | `LN_SALES_TAX_AMT` | NUMERIC |  | Stores Line Sales Tax Amount |
| 63 | `LN_POST_CLM_AMT` | NUMERIC |  | Stores Line Postage Claimed Amount |
| 64 | `LN_ORD_CNCT_NAM` | VARCHAR |  | Stores Line Ordering Provider Contact Name |
| 65 | `LN_PICK_UP_ADDR_1` | VARCHAR |  | Stores Line Ambulance Pick-Up Location Street Address Line 1 |
| 66 | `LN_PICK_UP_ADDR_2` | VARCHAR |  | Stores Line Ambulance Pick-Up Location Street Address Line 2 |
| 67 | `LN_PICK_UP_CITY` | VARCHAR |  | Stores Line Ambulance Pick-Up Location City |
| 68 | `LN_PICK_UP_STATE` | VARCHAR |  | Stores Line Ambulance Pick-Up Location State |
| 69 | `LN_PICK_UP_ZIP` | VARCHAR |  | Stores Line Ambulance Pick-Up Location Zip Code |
| 70 | `LN_PICK_UP_CNTRY` | VARCHAR |  | Stores Line Ambulance Pick-Up Location Country Code |
| 71 | `LN_PICK_UP_CNTRY_S` | VARCHAR |  | Stores Line Ambulance Pick-Up Location Country Subdivision Code |
| 72 | `LN_DROP_OFF_NAME` | VARCHAR |  | Stores Line Ambulance Drop-Off Location Name |
| 73 | `LN_DROP_OFF_ADDR_1` | VARCHAR |  | Stores Line Ambulance Drop-Off Location Address Line 1 |
| 74 | `LN_DROP_OFF_ADDR_2` | VARCHAR |  | Stores Line Ambulance Drop-Off Location Street Address Line 2 |
| 75 | `LN_DROP_OFF_CITY` | VARCHAR |  | Stores Line Ambulance Drop-Off Location City |
| 76 | `LN_DROP_OFF_STATE` | VARCHAR |  | Stores Line Ambulance Drop-Off Location State |
| 77 | `LN_DROP_OFF_ZIP` | VARCHAR |  | Stores Line Ambulance Drop-Off Location Zip |
| 78 | `LN_DROP_OFF_CNTRY` | VARCHAR |  | Stores Line Ambulance Drop-Off Location Country Code |
| 79 | `LN_DROP_OFF_CNTRY_S` | VARCHAR |  | Stores Line Ambulance Drop-Off Location Country Subdivision Code |
| 80 | `LN_SVC_FAC_IDEN` | VARCHAR |  | Stores line service facility location's entity identifier |
| 81 | `LN_RECERT_DT` | DATETIME |  | Store line recertification date |
| 82 | `LN_QTY_TXT` | VARCHAR |  | This item holds the units of quantity string for a service line. |
| 83 | `LN_NOTE_TPO` | VARCHAR |  | This item holds a line level third party organization note. |
| 84 | `LN_PURCH_SERV_REF` | VARCHAR |  | This item holds the purchased service reference identifier for the line. |
| 85 | `LN_DME_LAST_CERT_DT` | DATETIME |  | The last certification date for a durable medical equipment (DME) to be printed on the claim. |
| 86 | `LN_REF_ENTITY_IDENTIFIER_CODE` | VARCHAR |  | This item stores the line's referring provider's entity identifier code. |
| 87 | `LN_FILL_NUMBER` | VARCHAR |  | The code indicating whether the prescription is an original or a refill. |
| 88 | `LN_DAYS_SUPPLY` | INTEGER |  | Estimated number if days the prescription will last. |
| 89 | `LN_DAW_CODE` | VARCHAR |  | Code indicating whether or not the prescriber's instructions regarding generic substitution were followed. |
| 90 | `LN_NDC_COST` | NUMERIC |  | This item holds the unit cost associated with the National Drug Code (NDC) for the service line, which is expected to be the charge amount divided by the NDC quantity. |
| 91 | `LN_MCR_PAID_AMT` | NUMERIC |  | This is the amount that Medicare paid for the service line for field. |
| 92 | `LN_OTHR_PAID_AMT` | NUMERIC |  | This is the amount that the commercial coverage, if any, paid for this service line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

