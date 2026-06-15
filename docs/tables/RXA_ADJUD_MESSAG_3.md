# RXA_ADJUD_MESSAG_3

> Adjudication fields for D.0.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 115

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `O_BIN_NUMBER` | VARCHAR |  | Card Issuer ID or Bank ID Number used for network routing. |
| 5 | `O_VERSION_NUMBER` | VARCHAR |  | Code uniquely identifying the transmission syntax and corresponding Data Dictionary. |
| 6 | `O_TRANS_CODE_ID` | NUMERIC |  | NCPDP code identifying the type of transaction. |
| 7 | `O_TRANS_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 8 | `O_PRCSR_CTRL_NUM` | VARCHAR |  | Processor control number assigned by the processor. |
| 9 | `O_SERV_PROV_QUAL_ID` | NUMERIC |  | NCPDP code qualifying the 'Service Provider ID' (201-B1). |
| 10 | `O_SERV_PROV_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 11 | `O_SERV_PROV_ID` | VARCHAR |  | The unique identifier for the pharmacy or provider |
| 12 | `O_DATE_OF_SERV_DT` | DATETIME |  | Identifies date the prescription was filled or professional service rendered or subsequent payer began coverage following Part A expiration in a long-term care setting only. |
| 13 | `O_SOFTWARE_VENDOR` | VARCHAR |  | Code indicating the type of dispensing dose. |
| 14 | `O_CARDHOLDER_ID` | VARCHAR |  | Insurance ID assigned to the cardholder or identification number used by the plan. |
| 15 | `O_CARDHOLDER_FIRST` | VARCHAR |  | The insurance cardholder's first name used by the plan (312-CC) |
| 16 | `O_CARDHOLDER_LAST` | VARCHAR |  | The insurance cardholder's last name used by the plan (313-CD) |
| 17 | `O_HOME_PLAN` | VARCHAR |  | The code identifying the Blue Cross or Blue Shield plan ID which shows where the member's coverage has been designated. Usually where the member lives or purchased their coverage. |
| 18 | `O_PLAN_ID` | VARCHAR |  | Plan ID assigned by the processor to identify a set of parameters, benefit, or coverage criteria used to adjudicate a claim. |
| 19 | `O_ELIG_CLAR_CODE_ID` | NUMERIC |  | NCPDP code indicating that the pharmacy is clarifying eligibility for a patient. |
| 20 | `O_ELIG_CLAR_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 21 | `O_GROUP_ID` | VARCHAR |  | Unique ID assigned to cardholder group or employer group. |
| 22 | `O_PERSON_CODE` | VARCHAR |  | NCPDP code assigned to a specific person within a family. |
| 23 | `O_PAT_RELAT_CODE_ID` | NUMERIC |  | NCPDP code indicating the gender of the individual. |
| 24 | `O_PAT_RELAT_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 25 | `O_OTH_PAY_BIN_NUM` | VARCHAR |  | The secondary, tertiary, etc. card issuer or bank ID number used for network routing. |
| 26 | `O_OTH_PAY_PRCSR_NUM` | VARCHAR |  | The unique identifier of the secondary, tertiary, etc. payer to the processor. |
| 27 | `O_OTH_PAY_CARD_ID` | VARCHAR |  | Unique cardholder ID for the member associated with the designated Payor |
| 28 | `O_OTH_PAY_GROUP_ID` | VARCHAR |  | ID assigned to the cardholder group or employer group by the secondary, tertiary, etc. payer. |
| 29 | `O_MEDIGAP_ID` | VARCHAR |  | Patient's ID assigned by the Medigap insurer. |
| 30 | `O_MEDICAID_IND_ID` | NUMERIC |  | Two character State abbreviation indicating the state where Medicaid coverage exists |
| 31 | `O_MEDICAID_IND_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 32 | `O_PROV_ASGN_IND_ID` | NUMERIC |  | NCPDP code indicating whether the provider accepts assignment. |
| 33 | `O_PROV_ASGN_IND_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 34 | `O_PARTD_QUAL_FAC_ID` | NUMERIC |  | ID that indicates the patient resides in a facility that qualifies for the CMS Part D benefit. |
| 35 | `O_PARTD_QUAL_FAC_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 36 | `O_MEDICAID_ID_NUM` | VARCHAR |  | A unique member identification number assigned by the Medicaid Agency. |
| 37 | `O_MEDICAID_ASGN_NUM` | VARCHAR |  | Number assigned by processor to identify the individual Medicaid Agency or representative. |
| 38 | `O_PAT_ID_QUAL_ID` | NUMERIC |  | NCPDP code qualifying the 'Patient ID' (332-CY). |
| 39 | `O_PAT_ID_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 40 | `O_PAT_ID` | VARCHAR | FK→ | The unique identifier assigned to the patient |
| 41 | `O_PAT_DOB_DT` | DATETIME |  | The birth date of the patient. |
| 42 | `O_PAT_SEX_CODE_ID` | NUMERIC |  | NCPDP code indicating the gender of the individual. |
| 43 | `O_PAT_SEX_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 44 | `O_PAT_FIRST_NAME` | VARCHAR |  | Patient's first name sent to the payer (310-CA) |
| 45 | `O_PAT_LAST_NAME` | VARCHAR |  | Patient's last name sent to the payer (311-CB) |
| 46 | `O_PAT_STREET` | VARCHAR |  | Patient free text street address (322-CM) |
| 47 | `O_PAT_CITY` | VARCHAR |  | Free-form text for city name. |
| 48 | `O_PAT_STATE_ID` | NUMERIC |  | Standard State/Province Code as defined by appropriate government agency. |
| 49 | `O_PAT_STATE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 50 | `O_PAT_ZIP` | VARCHAR |  | Patient postal code zone excluding punctuation and blanks (zip code for US) (325-CF) |
| 51 | `O_PAT_PHONE_NUM` | VARCHAR |  | Ten-digit phone number of patient. |
| 52 | `O_PLACE_OF_SERV_ID` | NUMERIC |  | NCPDP code identifying the place where a drug or service is dispensed or administered. |
| 53 | `O_PLACE_OF_SERV_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 54 | `O_EMPLOYER_ID` | VARCHAR |  | Unique ID assigned to employer. |
| 55 | `O_SMOKER_CODE_ID` | NUMERIC |  | NCPDP code indicating the patient as a smoker or non-smoker. |
| 56 | `O_SMOKER_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 57 | `O_PREG_INDICATOR_ID` | NUMERIC |  | NCPDP code indicating the patient as pregnant or non-pregnant. |
| 58 | `O_PREG_INDICATOR_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 59 | `O_PAT_EMAIL_ADDRESS` | VARCHAR |  | The E-Mail address of the patient (member). |
| 60 | `O_PAT_RESIDENCE_ID` | NUMERIC |  | NCPDP code identifying the patient's place of residence. |
| 61 | `O_PAT_RESIDENCE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 62 | `O_RX_REF_NUM_QL_ID` | NUMERIC |  | This ID indicates the type of bill submitted. |
| 63 | `O_RX_REF_NUM_QL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 64 | `O_RX_REF_NUM` | VARCHAR |  | Reference number assigned by the provider for the dispensed product or service provided. |
| 65 | `O_PROD_ID_QUAL_ID` | NUMERIC |  | NCPDP code qualifying the value in 'Product/Service ID' (407-D7). |
| 66 | `O_PROD_ID_QUAL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 67 | `O_PROD_ID` | VARCHAR |  | Code indicating whether the provider accepts assignment. |
| 68 | `O_ASC_RX_REF_NUM` | VARCHAR |  | Associated 'Prescription/Service Reference Number' (402-D2) for particular service. |
| 69 | `O_ASC_RX_SERV_DT` | DATETIME |  | Date of the 'Associated Prescription/Service Reference Number' (456-EN). |
| 70 | `O_QUANTITY_DISP` | NUMERIC |  | Quantity dispensed in metric decimal units. |
| 71 | `O_FILL_NUM` | INTEGER |  | The code indicating whether the prescription is an original or a refill. |
| 72 | `O_DAYS_SUPPLY` | NUMERIC |  | Estimated number of days the prescription will last. |
| 73 | `O_COMPOUND_CODE_ID` | NUMERIC |  | NCPDP code indicating whether or not the prescription is a compound. |
| 74 | `O_COMPOUND_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 75 | `O_DAW_ID` | NUMERIC |  | Code indicating whether or not the prescriber's instructions regarding generic substitution were followed. |
| 76 | `O_DAW_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 77 | `O_DATE_WRITTEN_DT` | DATETIME |  | Date prescription was written. |
| 78 | `O_NUM_REFILLS_AUTH` | INTEGER |  | Number of refills authorized by the prescriber. |
| 79 | `O_RX_ORIGIN_CODE_ID` | NUMERIC |  | NCPDP code indicating the origin of the prescription. |
| 80 | `O_RX_ORIGIN_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 81 | `O_QTY_PRESCRIBED` | NUMERIC |  | Amount prescribed in metric decimal units. |
| 82 | `O_OTH_CVG_CODE_ID` | NUMERIC |  | Code indicating whether or not the patient has other insurance coverage. |
| 83 | `O_OTH_CVG_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 84 | `O_SPEC_PACK_IND_ID` | NUMERIC |  | NCPDP code identifying the type of transaction. |
| 85 | `O_SPEC_PACK_IND_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 86 | `O_ORIG_PRD_ID_QL_ID` | NUMERIC |  | NCPDP code qualifying the value in 'Originally Prescribed Product/Service Code' (Field 445-EA). |
| 87 | `O_ORIG_PRD_ID_QL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 88 | `O_ORIG_RX_PROD` | VARCHAR |  | NCPDP code of the initially prescribed product or service. |
| 89 | `O_ORIG_RX_QUANTITY` | NUMERIC |  | Initial prescribed amount in metric decimal units |
| 90 | `O_ALT_ID` | VARCHAR |  | Unique personal ID used for controlled product reporting. ID can be that of the patient or the person picking up the prescription as required by the state. |
| 91 | `O_SCHED_RX_ID_NUM` | VARCHAR |  | The serial number of the prescription form. |
| 92 | `O_UNIT_OF_MEAS_ID` | NUMERIC |  | NCPDP standard product billing codes. |
| 93 | `O_UNIT_OF_MEAS_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 94 | `O_LEVEL_OF_SERV_ID` | NUMERIC |  | Code indicating the type of service the provider supplied |
| 95 | `O_LEVEL_OF_SERV_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 96 | `O_PRIOR_AUTH_TYP_ID` | NUMERIC |  | NCPDP code qualifying the value in 'Product/Service ID' (407-D7). |
| 97 | `O_PRIOR_AUTH_TYP_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 98 | `O_PRIOR_AUTH_NUM` | VARCHAR |  | Code clarifying the 'Prior Authorization Number Submitted' (462-EV) or benefit/plan exemption. |
| 99 | `O_INT_AUTH_TYP_ID` | NUMERIC |  | ID indicating that authorization occurred for intermediary processing. |
| 100 | `O_INT_AUTH_TYP_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 101 | `O_INT_AUTH_ID` | VARCHAR |  | ID indicating intermediary authorization occurred. |
| 102 | `O_DISP_STATUS_ID` | NUMERIC |  | Code indicating the quantity dispensed is a partial fill or the completion of a partial fill. Used only in situations where inventory shortages do not allow the full quantity to be dispensed. |
| 103 | `O_DISP_STATUS_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 104 | `O_QTY_INT_TO_DISP` | NUMERIC |  | Metric decimal quantity of medication that would be dispensed on original filling if inventory were available. Used in association with a 'P' or 'C' in 'Dispensing Status' (343-HD). |
| 105 | `O_DAYS_INT_TO_DISP` | NUMERIC |  | Days supply for metric decimal quantity of medication that would be dispensed on original dispensing if inventory were available. Used in association with a 'P' or 'C' in 'Dispensing Status' (343-HD). |
| 106 | `O_DELAY_RSN_CODE_ID` | NUMERIC |  | NCPDP code to specify the reason that submission of the transactions has been delayed. |
| 107 | `O_DELAY_RSN_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 108 | `O_TX_REF_NUMBER` | VARCHAR |  | A reference number assigned by the provider to each of the data records in the batch or real-time transactions. The purpose of this number is to facilitate the process of matching the transaction response to the transaction. The transaction reference number assigned should be returned in the response. |
| 109 | `O_PAT_ASGN_IND_ID` | NUMERIC |  | Code which indicates a patient's choice on assignment of benefits. |
| 110 | `O_PAT_ASGN_IND_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 111 | `O_ROUTE_ADMIN_ID` | NUMERIC |  | This is an override to the "default" route referenced for the product. For a multi-ingredient compound, it is the route of the complete compound mixture. |
| 112 | `O_ROUTE_ADMIN_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 113 | `O_COMPOUND_TYPE_ID` | NUMERIC |  | Unique ID used to clarify the type of compound. |
| 114 | `O_COMPOUND_TYPE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 115 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `O_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

