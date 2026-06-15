# RXA_ADJUD_MESSAG_4

> Adjudication fields for D.0.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 93

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `O_MEDICAID_INT_NUM` | VARCHAR |  | Claim number assigned by the Medicaid Agency. |
| 5 | `O_PHR_SERV_TYPE_ID` | NUMERIC |  | The type of service being performed by a pharmacy when different contractual terms exist between a payer and the pharmacy, or when benefits are based upon the type of service performed. |
| 6 | `O_PHR_SERV_TYPE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 7 | `O_INGRD_COST_SUBMIT` | NUMERIC |  | Submitted ingredient cost of the dispensed prescription. This amount is included in the 'Gross Amount Due' (430-DU). |
| 8 | `O_DISP_FEE_SUBMIT` | NUMERIC |  | Dispensing fee submitted by the pharmacy. This amount is included in the 'Gross Amount Due' (430-DU). |
| 9 | `O_PROF_SERV_FEE` | NUMERIC |  | The amount submitted by the provider for professional services rendered. |
| 10 | `O_PAT_PAID_AMT` | NUMERIC |  | Amount the pharmacy received from the patient for the prescription dispensed. |
| 11 | `O_INCENTIVE_AMT` | NUMERIC |  | Amount represents a fee that is submitted by the pharmacy for contractually agreed upon services. This amount is included in the 'Gross Amount Due' (430-DU). |
| 12 | `O_FLAT_TAX` | NUMERIC |  | Flat sales tax submitted for prescription. This amount is included in the 'Gross Amount Due' (430-DU). |
| 13 | `O_PERC_TAX_AMT` | NUMERIC |  | Percentage of sales tax submitted. |
| 14 | `O_PERC_TAX_RTE` | NUMERIC |  | Percentage sales tax rate used to calculate 'Percentage Sales Tax Amount Submitted' (482-GE). |
| 15 | `O_PERC_TAX_BASIS_ID` | NUMERIC |  | Code indicating the basis for percentage sales tax. |
| 16 | `O_PERC_TAX_BASIS_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 17 | `O_USUAL_AND_CUSTOM` | NUMERIC |  | Amount charged to cash customers for the prescription exclusive of sales tax or other amounts claimed. |
| 18 | `O_GROSS_AMT_DUE` | NUMERIC |  | Code qualifying the length of need. |
| 19 | `O_BASIS_COST_DET_ID` | NUMERIC |  | NCPDP code indicating the method by which 'Ingredient Cost Submitted' (Field 409-D9) was calculated. |
| 20 | `O_BASIS_COST_DET_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 21 | `O_MEDICAID_AMT_PD` | NUMERIC |  | Amount paid by the Medicaid Agency. |
| 22 | `O_PROV_ID_QUAL_ID` | NUMERIC |  | Code qualifying the 'Provider ID' (444-E9). |
| 23 | `O_PROV_ID_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 24 | `O_PROV_ID` | VARCHAR |  | Unique ID assigned to the person responsible for the dispensing of the prescription or provision of the service. |
| 25 | `O_PRESC_ID_QUAL_ID` | NUMERIC |  | Code qualifying the 'Prescriber ID' (411-DB). |
| 26 | `O_PRESC_ID_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 27 | `O_PRESC_ID` | VARCHAR |  | ID assigned to the prescriber. |
| 28 | `O_PRESC_LAST_NAME` | VARCHAR |  | Individual's last name. |
| 29 | `O_PCP_QUAL_ID` | NUMERIC |  | Code qualifying the 'Primary Care Provider ID' (421-DL). |
| 30 | `O_PCP_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 31 | `O_PCP_ID` | VARCHAR |  | ID assigned to the primary care provider. Used when the patient is referred to a secondary care provider. |
| 32 | `O_PCP_LAST_NAME` | VARCHAR |  | Individual's last name. |
| 33 | `O_PRESC_STREET` | VARCHAR |  | Free-form text for prescriber address information. |
| 34 | `O_PRESC_CITY` | VARCHAR |  | Free-form text for the prescriber city name. |
| 35 | `O_PRESC_STATE_ID` | NUMERIC |  | Standard State/Province code as defined by the appropriate government agency. |
| 36 | `O_PRESC_STATE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 37 | `O_PRESC_ZIP` | VARCHAR |  | Code defining international postal zone excluding punctuation and blanks (zip codes in US). |
| 38 | `O_DATE_OF_INJURY_DT` | DATETIME |  | Date on which the injury occurred. |
| 39 | `O_EMPLOYER_NAME` | VARCHAR |  | Employer's full name. |
| 40 | `O_EMPLOYER_STREET` | VARCHAR |  | Free-form text for address information. |
| 41 | `O_EMPLOYER_CITY` | VARCHAR |  | Free-form text for city name. |
| 42 | `O_EMPLOYER_STATE_ID` | NUMERIC |  | Standard State/Province Code as defined by appropriate government agency. |
| 43 | `O_EMPLOYER_STATE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 44 | `O_EMPLOYER_ZIP` | VARCHAR |  | Code defining international postal zone excluding punctuation and blanks (zip code for US). |
| 45 | `O_EMPLOYER_PHONE` | VARCHAR |  | Employer's ten-digit phone number. |
| 46 | `O_EMPLOYER_CONTACT` | VARCHAR |  | Employer primary contact. |
| 47 | `O_CARRIER_ID` | VARCHAR |  | Carrier code assigned in Worker's Compensation Program. |
| 48 | `O_CLAIM_ID` | VARCHAR |  | Identifies the claim number assigned by Worker's Compensation Program. |
| 49 | `O_BILL_TYPE_IND_ID` | NUMERIC |  | NCPDP code that identifies the entity submitting the billing transaction. |
| 50 | `O_BILL_TYPE_IND_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 51 | `O_PAY_TO_QUAL_ID` | NUMERIC |  | The code that qualifies 'Pay to ID' (119-TT). |
| 52 | `O_PAY_TO_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 53 | `O_PAY_TO_ID` | VARCHAR |  | The unique identifier of the entity to receive payment for a claim. |
| 54 | `O_PAY_TO_NAME` | VARCHAR |  | Name of the entity to receive payment for claim. |
| 55 | `O_PAY_TO_STREET` | VARCHAR |  | Street address of the entity to receive payment for claim. |
| 56 | `O_PAY_TO_CITY` | VARCHAR |  | City of the entity to receive payment for claim. |
| 57 | `O_PAY_TO_STATE_ID` | NUMERIC |  | Standard State/Province code as defined by the appropriate government agency. |
| 58 | `O_PAY_TO_STATE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 59 | `O_PAY_TO_ZIP` | VARCHAR |  | Code defining international postal zone excluding punctuation and blanks (zip code for US). |
| 60 | `O_GEN_EQ_PROD_Q_ID` | NUMERIC |  | NCPDP code qualifying the 'Generic Equivalent Product ID' (126-UA). |
| 61 | `O_GEN_EQ_PROD_Q_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 62 | `O_GEN_EQ_PROD_ID` | VARCHAR |  | ID that identifies the generic equivalent of the brand product dispensed. |
| 63 | `O_COUPON_TYPE_ID` | NUMERIC |  | NCPDP code indicating the type of coupon being used. |
| 64 | `O_COUPON_TYPE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 65 | `O_COUPON_NUM` | VARCHAR |  | Unique serial number assigned to the prescription coupons. |
| 66 | `O_COUPON_VALUE` | NUMERIC |  | Value of the coupon. |
| 67 | `O_CMPND_DOSE_FRM_ID` | NUMERIC |  | Dosage form of the complete compound mixture. |
| 68 | `O_CMPND_DOSE_FRM_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 69 | `O_CMPND_DISP_FRM_ID` | NUMERIC |  | NCPDP standard product billing codes. |
| 70 | `O_CMPND_DISP_FRM_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 71 | `O_ADD_DOC_TYPE_ID` | NUMERIC |  | Unique identifier for the additional data being submitted. |
| 72 | `O_ADD_DOC_TYPE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 73 | `O_REQ_BEGIN_DATE` | DATETIME |  | The beginning date of need. |
| 74 | `O_REQ_REVISED_DATE` | DATETIME |  | The effective date of the revision or re-certification provided by the certifying physician. |
| 75 | `O_REQ_STATUS_ID` | NUMERIC |  | A unique code identifying the type of request. |
| 76 | `O_REQ_STATUS_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 77 | `O_LEN_NEED_QUAL_ID` | NUMERIC |  | NCPDP code qualifying the length of need. |
| 78 | `O_LEN_NEED_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 79 | `O_LENGTH_OF_NEED` | INTEGER |  | Duration the physician expects the patient to require use of the ordered item. |
| 80 | `O_PRESC_SIGNED_DATE` | DATETIME |  | The date the form was completed and signed by the ordering physician. |
| 81 | `O_SUPPORT_DOCUMENT` | VARCHAR |  | Free text message for the Supporting Documentation field. |
| 82 | `O_FACILITY_ID` | VARCHAR |  | ID assigned to the patient's clinic/host party. |
| 83 | `O_FACILITY_NAME` | VARCHAR |  | Location of service's provided. |
| 84 | `O_FACILITY_STREET` | VARCHAR |  | Free-form text for facility address information. |
| 85 | `O_FACILITY_CITY` | VARCHAR |  | Free-form text for facility city name. |
| 86 | `O_FACILITY_STATE_ID` | NUMERIC |  | Standard State/Province code as defined by the appropriate government agency. |
| 87 | `O_FACILITY_STATE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 88 | `O_FACILITY_ZIP` | VARCHAR |  | Code defining international postal zone excluding punctuation and blanks (zip code for US). |
| 89 | `O_NARRATIVE_MSG` | VARCHAR |  | Free-form text for the Narrative Message field. |
| 90 | `O_PRESC_FIRST_NAME` | VARCHAR |  | Individual's first name. |
| 91 | `O_PRESC_PHONE_NO` | VARCHAR |  | Ten-digit phone number of the prescriber. |
| 92 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 93 | `SINGL_COMPON_CLM_YN` | VARCHAR |  | Indicates if the adjudication attempt was adjudicating a single component for compound. 'N' or NULL indicate that the attempt was not adjudicating a single component of a compound. 'Y' indicates that the attempt was adjudicating a single component of a compound.. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

