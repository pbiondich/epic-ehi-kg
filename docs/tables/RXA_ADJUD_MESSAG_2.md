# RXA_ADJUD_MESSAG_2

> Contains various information relating to a single contact of an adjudication record. Adjudication records are used by Ambulatory Pharmacy during prescription copay adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 77

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `BIN_NUM` | VARCHAR |  | The BIN (Bank Identification Number) used during prescription adjudication. This number can be stored in the plan and payor, and a different number can be returned based on whether the adjudication is primary or not. (101-A1) |
| 5 | `PROCESSOR_CTRL_NUM` | VARCHAR |  | The processor control number used during prescription adjudication. This number can be stored in the plan and payor, and a different number can be returned based on whether the adjudication is primary or not.(104-A4) |
| 6 | `ORG_PRESC_PROD_CODE` | VARCHAR |  | NCPDP code of the initially prescribed product or service.(445-EA) |
| 7 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 8 | `I_TX_CODE_ID` | NUMERIC |  | NCPDP code identifying the type of transaction. |
| 9 | `I_TX_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 10 | `I_HEADER_RESP_ST_ID` | NUMERIC |  | NCPDP code indicating the status of the transmission. |
| 11 | `I_HEADER_RESP_ST_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 12 | `I_SVC_PROV_QUAL_ID` | NUMERIC |  | NCPDP code qualifying the 'Service Provider ID' (201-B1). |
| 13 | `I_SVC_PROV_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 14 | `I_PYR_QUAL_ID` | NUMERIC |  | NCPDP code indicating the type of payer ID. |
| 15 | `I_PYR_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 16 | `I_MCAID_MEM_ID_NUM` | VARCHAR |  | A unique member identification number assigned by the Medicaid Agency. |
| 17 | `I_MEDICAID_AGNC_NUM` | VARCHAR |  | The Medicaid Agency Number sent to the payer (116-N6) |
| 18 | `I_CARDHOLDER_ID` | VARCHAR |  | Insurance ID assigned to the cardholder or identification number used by the plan. |
| 19 | `I_MCARE_D_CVG_ID` | NUMERIC |  | NCPDP code indicating whether a coverage is a Medicare Part D Coverage |
| 20 | `I_MCARE_D_CVG_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 21 | `I_CMS_LICS_LEVEL` | VARCHAR |  | ID for the formulary list |
| 22 | `I_CONTRACT_NUMBER` | VARCHAR |  | Code indicating the status of the transmission. |
| 23 | `I_FORMULARY_ID` | VARCHAR |  | The unique identifier for the formular list. |
| 24 | `I_BENEFIT_ID` | VARCHAR |  | Insurance ID assigned to the cardholder or identification number used by the plan. |
| 25 | `I_NXT_MDCR_D_EFF_DT` | DATETIME |  | A Medicare Part D coverage's effective starting date |
| 26 | `I_NXT_MDCR_D_TR_DT` | DATETIME |  | A Medicare Part D coverage's effective ending date |
| 27 | `I_PATIENT_FIRST_NAM` | VARCHAR |  | Patient's first name sent to the payer (310-CA) |
| 28 | `I_PATIENT_LAST_NAME` | VARCHAR |  | Patient's last name sent to the payer (311-CB) |
| 29 | `I_BIRTH_DATE` | DATETIME |  | ID for the formulary list |
| 30 | `I_TX_RESP_STAT_ID` | NUMERIC |  | NCPDP code indicating the status of the transaction. |
| 31 | `I_TX_RESP_STAT_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 32 | `I_HELP_DESK_QUAL_ID` | NUMERIC |  | NCPDP code qualifying the phone number in the 'Help Desk Phone Number' (550-8F). |
| 33 | `I_HELP_DESK_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 34 | `I_TX_REF_NUM` | VARCHAR |  | Code indicating the status of the transaction. |
| 35 | `I_INT_CTRL_NUM` | VARCHAR |  | Number assigned by the processor to identify an adjudicated claim when supplied in payer-to-payer coordination of benefits only. |
| 36 | `I_URL` | VARCHAR |  | The web page address sent to the payer (987-MA) |
| 37 | `I_RX_RF_NUM_QUAL_ID` | NUMERIC |  | NCPDP code indicating the type of billing submitted. |
| 38 | `I_RX_RF_NUM_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 39 | `I_MCAID_CLAIM_NUM` | VARCHAR |  | Claim number assigned by the Medicaid Agency. |
| 40 | `I_TAX_EXEMPT_IND_ID` | NUMERIC |  | NCPDP code indicating the payer and/or the patient is exempt from taxes. |
| 41 | `I_TAX_EXEMPT_IND_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 42 | `I_BAS_REIM_DET_ID` | NUMERIC |  | NCPDP code identifying how the reimbursement amount was calculated for 'Ingredient Cost Paid' (506-F6). |
| 43 | `I_BAS_REIM_DET_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 44 | `I_BAS_DISP_FEE_ID` | NUMERIC |  | NCPDP code indicating how the reimbursement amount was calculated for 'Dispensing Fee Paid' (507-F7). |
| 45 | `I_BAS_DISP_FEE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 46 | `I_BAS_CALC_COPAY_ID` | NUMERIC |  | NCPDP code indicating how the Copay reimbursement amount was calculated for 'Patient Pay Amount' (505-F5). |
| 47 | `I_BAS_CALC_COPAY_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 48 | `I_BAS_FLAT_TAX_ID` | NUMERIC |  | NCPD code indicating how the reimbursement amount was calculated for 'Flat Sales Tax Amount Paid' (558-AW). |
| 49 | `I_BAS_FLAT_TAX_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 50 | `I_BAS_PCT_TAX_ID` | NUMERIC |  | NCPDP code indicating how the reimbursement amount was calculated for 'Percentage Sales Tax Amount Paid' (559-AX). |
| 51 | `I_BAS_PCT_TAX_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 52 | `I_AMT_ATTR_PROC_FEE` | NUMERIC |  | This specifies the amount that is attributed to the processor fee. |
| 53 | `I_PAT_SAL_TAX_AMT` | NUMERIC |  | The sales tax that has been calculated. |
| 54 | `I_PLAN_SAL_TAX_AMT` | NUMERIC |  | The sales tax amount attributed to the plan. |
| 55 | `I_AMT_COINS` | NUMERIC |  | The amount of coinsurance that was calculated. |
| 56 | `I_BAS_CALC_COINS` | NUMERIC |  | NCPDP code specifying the basis on which the coinsure was calculated. |
| 57 | `I_BAS_CALC_COINS_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 58 | `I_EST_GENERC_SAVING` | NUMERIC |  | The calculated estimated generic savings. |
| 59 | `I_SP_ACC_AMT_REM` | NUMERIC |  | The amount remaining on the spending amount. (128-UC) |
| 60 | `I_HPFA_AMT` | NUMERIC |  | Medicare Part D Coverage Code |
| 61 | `I_AMT_PROV_NET_SEL` | NUMERIC |  | The amount that has been attributed to the provider network selection |
| 62 | `I_AMT_PROD_SEL_BRAN` | NUMERIC |  | The amount that is attributed to product selection for branded drugs. |
| 63 | `I_AMT_NPRF_FRM_SEL` | NUMERIC |  | The amount that is attributed to a product selection for non preferred formulary selections. |
| 64 | `I_AMT_BRND_NPRF_FRM` | NUMERIC |  | The amount that is attributed to product selection for Brand non preferred formulary selections. |
| 65 | `I_AMT_ATTR_CVG_GAP` | NUMERIC |  | The amount that is attributed to the coverage gap. |
| 66 | `I_INGR_COST_CNTRCTD` | NUMERIC |  | The cost of the ingredient contracted/reimbursable amount. |
| 67 | `I_DISP_FEE_CNTRCTD` | NUMERIC |  | The dispensible free that was contracted/reimbursable amount |
| 68 | `I_PCT_TAX_PD_ID` | NUMERIC |  | NCPDP code indicating the percentage sales tax paid basis. |
| 69 | `I_PCT_TAX_PD_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 70 | `I_COPAY_AMT` | NUMERIC |  | The amount to be collected from the patient that is included in 'Patient Pay Amount' (505-F5) that is due to a per prescription copay. |
| 71 | `REVERSE_OF_RXA_ID` | NUMERIC |  | The unique ID of the original adjudication that this reversal or rebill is reversing. |
| 72 | `REVERSE_OF_DATE_REAL` | FLOAT |  | Unique contact date in decimal format of the original adjudication that this reversal or rebill is reversing. |
| 73 | `IS_MANUALLY_APPROVED_YN` | VARCHAR |  | Indicates if the adjudication attempt was manually approved. 'N' or NULL indicate that the attempt was not manually approved. 'Y' indicates that the attempt as manually approved. |
| 74 | `PREVIOUS_ADJ_RXA_ID` | NUMERIC |  | Gets the adjudication attempt ID of the previous coverage in the filing order at the moment of this adjudication attempt. For primary coverage adjudications, this will always be null. For secondary coverages, this will point to the primary coverage. For tertiary coverages, this will point to the secondary coverage. |
| 75 | `PREVIOUS_ADJ_DATE_REAL` | FLOAT |  | Gets the unique adjudication attempt date of the previous coverage in the filing order at the moment of this adjudication attempt. For primary coverage adjudications, this will always be null. For secondary coverages, this will point to the primary coverage. For tertiary coverages, this will point to the secondary coverage. |
| 76 | `M3P_STATUS_C_NAME` | VARCHAR |  | This is the M3P status inferred from the NCPDP vD.0 field Approved Message Codes (548-6F). Blank - No M3P related status 1 - Patient is likely to benefit from M3P (Code 056) 2 - Patient is enrolled in the M3P (Code 057) and the coverage applied correctly 3 - Patient is enrolled in the M3P (Code 057) but the coverage not applied correctly 4 - Patient not longer participating/elected not to participate (Code 058) |
| 77 | `RESUB_DOCUMENT_ID` | VARCHAR |  | The document attached in the Resubmission/Attachment field. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

