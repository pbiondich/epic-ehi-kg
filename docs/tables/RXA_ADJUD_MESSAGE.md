# RXA_ADJUD_MESSAGE

> Contains various information relating to a single contact of an adjudication record. Adjudication records are used by Ambulatory Pharmacy during prescription copay adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 100  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact number for this adjudication |
| 6 | `CONTACT_NUM` | NUMERIC |  | The unique contact number for this adjudication |
| 7 | `NAME_HX` | VARCHAR |  | Stores the history of the record name |
| 8 | `CONTACT_TYPE_C_NAME` | VARCHAR |  | The contact type category ID for the adjudication record. |
| 9 | `STATUS_C_NAME` | VARCHAR |  | The status category ID of the adjudication message. |
| 10 | `VERSION_NUM_C_NAME` | VARCHAR |  | Version number category ID of the NCPDP message |
| 11 | `TX_CODE_C_NAME` | VARCHAR |  | The transaction code category ID of the adjudication message (Billing, Rebill, Reversal...) |
| 12 | `RESPONSE_STATUS_C_NAME` | VARCHAR |  | The response status category ID if the message was accepted or rejected. |
| 13 | `SERVICE_PROV_QUAL_C_NAME` | VARCHAR |  | The provider ID type category ID (NPI, DEA, State License...) that was sent over RX adjudication |
| 14 | `SERVICE_PROV` | VARCHAR |  | The unique ID of the pharmacy (service provider). |
| 15 | `SERVICE_DATE` | DATETIME |  | The service date of the order. This is typically the date the pharmacy starts processing the order. |
| 16 | `MESSAGE` | VARCHAR |  | Free text message sent back from the payor. |
| 17 | `GROUP_ID` | VARCHAR | shared | The Group ID number submitted in the adjudication attempt |
| 18 | `PLAN_ID` | VARCHAR |  | Assigned by the Pharmacy Benefits Manager to identify a set of parameters, benefits, or coverage criteria used to adjudicate a claim. |
| 19 | `NETWORK_REIMBURSE` | VARCHAR |  | As defined by the Pharmacy Benefits Bander, this field identifies the network, for the covered member, used to calculate the reimbursement to the pharmacy. |
| 20 | `PAYOR_QUALIFIER_C_NAME` | VARCHAR |  | NCPDP code indicating the type of payor ID. |
| 21 | `PAYOR_ID` | VARCHAR | FK→ | The ID of the payer from the Payer ID field of the adjudication response. |
| 22 | `TX_RESP_C_NAME` | VARCHAR |  | The status category ID of the adjudication transaction. |
| 23 | `AUTH_NUM` | VARCHAR |  | Number assigned by the PBM to identify an authorized transaction. |
| 24 | `ADDL_MESSAGE` | VARCHAR |  | This is a free text message sent from the PBM. |
| 25 | `HELPDESK_PH_QUAL_C_NAME` | VARCHAR |  | NCPDP code qualifying the phone number in the 'Help Desk Phone Number' (550-8F) Field 550-8F) |
| 26 | `HELP_DESK_PHONE_NUM` | VARCHAR |  | Ten-digit phone number of the help desk. |
| 27 | `PRESC_REF_NUM_C_NAME` | VARCHAR |  | Reference number (prescription or service) category ID assigned by the provider for the order. |
| 28 | `PRESC_REFRENCE_NUM` | VARCHAR |  | Reference number assigned by the provider for the dispensed drug/product and/or service provided. |
| 29 | `PAT_PAY_AMOUNT` | NUMERIC |  | Amount that is calculated by the PBM and returned to the pharmacy as the TOTAL amount to be paid by the patient to the pharmacy: The patient's total cost share, including copayments, amounts applied to deductible, over maximum amounts, penalties, etc. |
| 30 | `INGREDIENT_COSTPAID` | NUMERIC |  | The amount paid for the drug ingredient. Amount included in 'Total Amount Paid' |
| 31 | `DISPENSE_FEE_PAID` | NUMERIC |  | Dispensing fee paid included in the "Total Amount Paid" sent out in adjudication (NCPDP Field 509-F9) |
| 32 | `TAX_EXEMPT_IND_C_NAME` | VARCHAR |  | NCPDP code indicating the payor as exempt from taxes. |
| 33 | `FLAT_SALES_TAX_PAID` | NUMERIC |  | Amount of flat sales tax paid. Included in the "Total Amount Paid". |
| 34 | `PERC_SALES_TAX_PAID` | NUMERIC |  | Amount of percentage sales tax paid which is included in the Total Amount Paid |
| 35 | `PERC_SALES_TAX_RATE` | NUMERIC |  | Percentage sales tax rate used to calculate Percentage Sales Tax Amount Paid |
| 36 | `PERC_SALES_TX_BAS_C_NAME` | VARCHAR |  | NCPDP code indicating the percentage sales tax paid basis. |
| 37 | `INCENTIVE_AMT_PAID` | NUMERIC |  | Amount represents the contractually agreed upon incentive fee paid for specific services rendered. Amount is included in the 'Total Amount Paid' |
| 38 | `PROF_SERVICE_FEE` | NUMERIC |  | Amount representing the contractually agreed upon fee for professional services rendered. This amount is included in the Total Amount Paid |
| 39 | `OTHER_PAYOR_AMT_REC` | NUMERIC |  | Total dollar amount of any payment from another source including coupons. |
| 40 | `TOTAL_AMOUNT_PAID` | NUMERIC |  | Total amount to be paid by the claim's pharmacy benefit manager (PBM). |
| 41 | `BASIS_ING_REIMB_C_NAME` | VARCHAR |  | NCPDP code identifying how the reimbursement amount was calculated for Ingredient Cost Paid |
| 42 | `AMT_ATTRB_SALES_TAX` | NUMERIC |  | Amount to be collected from the patient that is included in Patient Pay Amount that is due to sales tax paid. |
| 43 | `ACCUMULATED_DED_AMT` | NUMERIC |  | Amount in dollars met by the patient/family in a deductible plan. |
| 44 | `REMAINING_DED_AMT` | NUMERIC |  | Amount not met by the patient/family in the deductible plan. |
| 45 | `REMAINING_BEN_AMT` | NUMERIC |  | Amount remaining in a patient/family plan with a periodic maximum benefit. |
| 46 | `AMT_APPLIED_DEDUCT` | NUMERIC |  | Amount to be collected from a patient that is included in Patient Pay Amount that is applied to a periodic deductible. |
| 47 | `AMT_COPAY` | NUMERIC |  | Amount to be collected from the patient that is included in Patient Pay Amount that is due to a per prescription copay/coinsurance. |
| 48 | `AMT_ATTRIB_PROD_SEL` | NUMERIC |  | Amount to be collected from the patient that is included in the Patient Pay Amount that is due to the patient's selection of drug product. |
| 49 | `AMT_EXCEED_BEN_MAX` | NUMERIC |  | Amount to be collected from the patient that is included in Patient Pay Amount that is due to the patient exceeding a periodic benefit maximum |
| 50 | `BASIS_CALC_DISP_C_NAME` | VARCHAR |  | NCPDP code indicating how the reimbursement amount was calculated for Dispensing Fee Paid |
| 51 | `BASIS_CALC_COPAY_C_NAME` | VARCHAR |  | NCPDP code indicating how the reimbursement amount was calculated for Patient Pay Amount |
| 52 | `BASIS_CALC_FLATTX_C_NAME` | VARCHAR |  | NCPDP code indicating how the reimbursement amount was calculated for Flat Sales Tax Amount Paid |
| 53 | `BASIS_PCT_SLS_TAX_C_NAME` | VARCHAR |  | NCPDP code indicating how the reimbursement amount was calculated for Percentage Sales Tax Amount Paid |
| 54 | `PRIOR_AUTH_PROC_DT` | DATETIME |  | Date the prior authorization request was processed. |
| 55 | `PRIOR_AUTH_EFF_DT` | DATETIME |  | Date the prior authorization became effective. |
| 56 | `PRIOR_AUTH_EXP_DT` | DATETIME |  | Date the prior authorization expires. |
| 57 | `PRIOR_AUTH_QUANTITY` | NUMERIC |  | Amount authorized by the prior authorization expressed in metric decimal units. |
| 58 | `PRIOR_AUTH_DOL_AUTH` | NUMERIC |  | Amount authorized in the prior authorization. |
| 59 | `PRIOR_AUTH_NM_REFIL` | NUMERIC |  | Number of refills authorized by the prior authorization. |
| 60 | `PRIOR_AUTH_ACCUM` | NUMERIC |  | Accumulated authorized amount expressed in metric decimal units. |
| 61 | `PRIOR_AUTH_NUM` | VARCHAR |  | Unique number identifying the prior authorization assigned by the PBM. |
| 62 | `INSTANT_OF_ENTRY_TM` | DATETIME (Attached) |  | Stores the date and time of entry when a record is edited |
| 63 | `CONTINUE_ON_FAIL_YN` | VARCHAR |  | Indicates if the adjudication attempt will continue to the next coverage if this fails. 'N' or NULL indicate that the attempt will not continue on failure. 'Y' indicates that the attempt will continue on failure. |
| 64 | `PRIOR_AUTH_NUM_SENT` | VARCHAR |  | The number being sent in for prior authorization for prescription adjudication. |
| 65 | `PRIOR_AUTH_TYPE_C_NAME` | VARCHAR |  | The prior authorization category ID being sent during prescription adjudication. |
| 66 | `SUBMISSION_CLR_C_NAME` | VARCHAR |  | Additional information category ID of an adjudication message to tell the payor more information about the order for adjudication. Like the patient is a student or is going on vacation. |
| 67 | `DISPENSE_FEE_SUBMTD` | NUMERIC |  | Dispensing fee submitted by the pharmacy to the payer. (412-DC) |
| 68 | `PROF_SVC_FEE_SUBMTD` | NUMERIC |  | Amount submitted by the provider for professional services rendered. (440-E5) |
| 69 | `INCENTIV_AMT_SUBMTD` | NUMERIC |  | Amount represents a fee that is submitted by the pharmacy for contractually agreed upon services. (439-E3) |
| 70 | `QTY_PRESCRIBED` | NUMERIC |  | Prescribed amount expressed in metric decimal units. (460-ET) |
| 71 | `UNIT_DOSE_IND_C_NAME` | VARCHAR |  | NCPDP code indicating the type of unit dose dispensing. (429-DT) |
| 72 | `ORG_PRES_PROD_QF_C_NAME` | VARCHAR |  | NCPDP code qualifying the value in 'Originally Prescribed Product/Service' Code. (453-EJ) |
| 73 | `LEVEL_OF_SERVICE_C_NAME` | VARCHAR |  | NCPDP code indicating the type of service the provider rendered. (418-DI) |
| 74 | `INTRMED_AUTH_TYP_C_NAME` | VARCHAR |  | NCPDP code indicating that authorization occurred for intermediary processing. (463-EW) |
| 75 | `INTRAUTH_IDENTIFIER` | VARCHAR |  | Value indicating intermediary authorization occurred. (464-EX) |
| 76 | `COUPON_TYPE_C_NAME` | VARCHAR |  | NCPDP code indicating the type of coupon being used. (485-KE) |
| 77 | `COUPON_VALUE_AMT` | NUMERIC |  | Value of the coupon. (487-NE) |
| 78 | `PRIOR_AUTH_REQTYP_C_NAME` | VARCHAR |  | NCPDP code identifying type of prior authorization request. (498-PA) |
| 79 | `PRIORAUTH_RQBEG_DT` | DATETIME |  | Beginning date for a prior authorization request. (498-PB) |
| 80 | `PRIORAUTH_RQEND_DT` | DATETIME |  | Ending date for a prior authorization request. (498-PC) |
| 81 | `PRIORAUTH_BAS_RQ_C_NAME` | VARCHAR |  | NCPDP code describing the reason for prior authorization request. (498-PD) |
| 82 | `PRIOR_AUTH_REP_FNAM` | VARCHAR |  | First name of the patient's authorized representative (498-PE) |
| 83 | `PRIOR_AUTH_REP_LNAM` | VARCHAR |  | Last name of the patient's authorized representative. (498-PF) |
| 84 | `PRIOR_ATH_REP_STADD` | VARCHAR |  | Street address of the patient's representative. (498-PG) |
| 85 | `PRI_ATH_REP_CITYADD` | VARCHAR |  | City of the patient's representative. (498-PH) |
| 86 | `PRI_ATH_REP_STATE_C_NAME` | VARCHAR | org | State or province category ID of the patient's representative. (498-PJ) |
| 87 | `PRI_ATH_REP_ZIP` | VARCHAR |  | ZIP code or other postal zone code of the patient's representative. (498-PK) |
| 88 | `PRI_ATH_NUM_ASSGN` | VARCHAR |  | Unique number identifying the prior authorization assigned by the processor. (498-PY) |
| 89 | `PRI_ATH_AUTH_NUM` | VARCHAR |  | Number assigned by the processor to identify an authorized transaction. (503-F3) |
| 90 | `PRI_ATH_SUPP_DOC` | VARCHAR |  | Free-text comments supplied by the pharmacy that may be used to process a prior authorization transaction. (498-PP) |
| 91 | `SMOKER_CODE_C_NAME` | VARCHAR |  | NCPDP code indicating the patient as a smoker or non-smoker. (334-1C) |
| 92 | `PREGNANCY_IND_C_NAME` | VARCHAR |  | NCPDP code indicating the patient as pregnant or not pregnant. (335-2C) |
| 93 | `PRESCRIBER_LOC_CODE` | VARCHAR |  | Location address code assigned to the prescriber as identified in the National Provider System (NPS). (467-1E) |
| 94 | `ALT_IDENTIFIER` | VARCHAR |  | Person identifier to be used for controlled product reporting. Identifier may be that of the patient or the person picking up the prescription as required by the governing body. (330-CW) |
| 95 | `COUPON_NUM` | VARCHAR |  | Unique serial number assigned to the prescription coupons. (486-ME) |
| 96 | `PAT_ID_QF_C_NAME` | VARCHAR |  | NCPDP code qualifying the Patient ID sent in 332-CY. (331-CX) |
| 97 | `PAT_IDENTIFIER` | VARCHAR |  | ID assigned to the patient. (332-CY) |
| 98 | `EMPLOYER` | VARCHAR |  | A unique ID assigned to the employer. (333-CZ) |
| 99 | `PAT_PAID_AMT_SUBMTD` | NUMERIC |  | Amount the pharmacy received from the patient for the prescription dispensed. |
| 100 | `PAT_DOB_DT` | DATETIME |  | Date of birth of patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAYOR_ID` | [CLARITY_EPM](CLARITY_EPM.md) | sole_pk | high |

