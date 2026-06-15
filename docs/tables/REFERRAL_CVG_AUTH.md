# REFERRAL_CVG_AUTH

> The REFERRAL_CVG_AUTH contains coverage auth/cert information for referrals.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 78  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_CERT_CVG_ID` | NUMERIC |  | Coverage ID for Auth/Cert information |
| 4 | `PRE_CERT_REQ_YN` | VARCHAR |  | Indicates whether pre-cert is required for this coverage |
| 5 | `PRE_CERT_STATUS_C_NAME` | VARCHAR | org | Pre-certification status for this coverage |
| 6 | `PRE_CERT_AGENCY_ID` | VARCHAR |  | ID of the agency used for precertification |
| 7 | `PRE_CERT_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 8 | `PRE_CERT_AGENCY_PH` | VARCHAR |  | Phone number of the agency used for precertification |
| 9 | `PRE_CERT_CONTACT` | VARCHAR |  | Contact individual for the pre-certification agency |
| 10 | `PRE_CERT_CALLED_DT` | DATETIME |  | Date on which the payor was called for pre-certification information |
| 11 | `PRE_CERT_RECV_DT` | DATETIME |  | Date on which pre-certification information was received |
| 12 | `PRE_CERT_RCV_ID` | VARCHAR |  | User who received pre-certification information |
| 13 | `PRE_CERT_RCV_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `PRE_CERT_FAX` | VARCHAR |  | Fax number for pre-certification information |
| 15 | `PRE_CERT_BN_REQ_YN` | VARCHAR |  | Indicates whether a pre-certification benefits check is required |
| 16 | `PRE_CERT_BEN_STS_C_NAME` | VARCHAR | org | Status of the pre-certification benefits |
| 17 | `PRE_CERT_BEN_CHECK` | VARCHAR |  | Individual from whom pre-cert benefits information was received |
| 18 | `PRE_CERT_BEN_PHONE` | VARCHAR |  | Phone number to use for pre-cert benefits checking |
| 19 | `PRE_CERT_BEN_CNCT` | VARCHAR |  | Contact person for pre-cert benefits checking |
| 20 | `PRE_CERT_BEN_FAX` | VARCHAR |  | Fax number for pre-cert benefits checking |
| 21 | `PRE_CERT_BEN_CK_DT` | DATETIME |  | Date on which pre-cert benefits were checked |
| 22 | `PRE_CERT_BN_USR_ID` | VARCHAR |  | ID of user who checked pre-cert benefits information |
| 23 | `PRE_CERT_BN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `PRE_CERT_CLIN_CNCT` | VARCHAR |  | Contact individual for pre-cert clinical information |
| 25 | `PRE_CERT_CLIN_PHON` | VARCHAR |  | Phone number for pre-cert clinical information |
| 26 | `AUTH_FROM_DT` | DATETIME |  | The beginning date of the period authorized by the payor |
| 27 | `AUTH_TO_DT` | DATETIME |  | The end date of the period authorized by the payor. |
| 28 | `MAX_OUT_POCKET` | NUMERIC |  | Contains Maximum Out of Pocket Amount: The most you pay in coinsurance during a benefit plan year. After you reach your out-of-pocket maximum, your medical plan option pays 100% (unless balance billing applies) of eligible expenses for the remainder of the benefit plan year |
| 29 | `LIFETIME_MAX` | NUMERIC |  | Contains Lifetime Maximum Amount: The maximum amount that the insurance company will cover for this patient over the course of their lifetime. |
| 30 | `TOT_PT_AMOUNT` | NUMERIC |  | Contains Total Patient Amount: The total amount the patient owes for this visit |
| 31 | `ADM_NOTIF_STAT_C_NAME` | VARCHAR | org | Contains admission notification status: A field that can be used to track the status of the admission notification that needs to be faxed or sent electronically to the payor. This is a customer-owned category list. |
| 32 | `CONC_REV_REQD_YN` | VARCHAR |  | Contains Information on whether a concurrent review (clinical review) is required or not. |
| 33 | `IN_NETWORK_YN` | VARCHAR |  | This field is used to track whether or not the patient’s insurance is in Network. |
| 34 | `DEDUCTIBLE_MET_YN` | VARCHAR |  | A deductible is the amount you must pay before the Plan begins to pay benefits. This field tracks whether or not the patient has paid that amount. |
| 35 | `DEDUCTIBLE_MET_AMT` | NUMERIC |  | Contains Deductible Met Amount. A deductible is the amount you must pay before the Plan begins to pay benefits. This field tracks how much the patient has paid. |
| 36 | `COINSUR_MET_YN` | VARCHAR |  | Coinsurance is a percentage of an eligible expense that you are required to pay for a covered service. This field tracks whether or not the patient has paid that amount. |
| 37 | `COINSURANCE_MET_AMT` | NUMERIC |  | Contains coinsurance met amount. Coinsurance is a percentage of an eligible expense that you are required to pay for a covered service. This field tracks how much the patient has paid. |
| 38 | `OUT_POCKET_MET_YN` | VARCHAR |  | This fields tracks whether or not the patient has paid their out of pocket expenses. |
| 39 | `OUT_POCKET_MET_AMT` | NUMERIC |  | Contains Out of Pocket Met Amount. This fields tracks how much the patient has paid towards their out of pocket expenses. |
| 40 | `PREEXIST_COND_YN` | VARCHAR |  | Contains whether or not pre-existing conditions are present. It is used to track whether or not the patient has pre-existing conditions that may impact their benefits. |
| 41 | `PREEXIST_COND_VAL` | VARCHAR |  | Contains Pre-existing conditions value. If the patient has pre-existing conditions that may impact their benefits, this field is used to document the pre-existing conditions. |
| 42 | `PRECERT_CMT_NOTE_ID` | VARCHAR |  | The unique ID of the note containing pre-certification comments entered on the referral. |
| 43 | `PRECERT_BEN_NOTE_ID` | VARCHAR |  | The unique ID of the note containing benefits information entered on the referral. |
| 44 | `GENERIC_CATEG_1_C_NAME` | VARCHAR | org | Generic category for general use |
| 45 | `GENERIC_CATEG_2_C_NAME` | VARCHAR | org | Generic category for general use |
| 46 | `GENERIC_CATEG_3_C_NAME` | VARCHAR | org | Generic category for general use |
| 47 | `GENERIC_CATEG_4_C_NAME` | VARCHAR | org | Generic category for general use |
| 48 | `GENERIC_CATEG_5_C_NAME` | VARCHAR | org | Generic category for general use |
| 49 | `GENERIC_CATEG_6_C_NAME` | VARCHAR | org | Generic category for general use |
| 50 | `GENERIC_CATEG_7_C_NAME` | VARCHAR | org | Generic category for general use |
| 51 | `GENERIC_CATEG_8_C_NAME` | VARCHAR | org | Generic category for general use |
| 52 | `GENERIC_CATEG_9_C_NAME` | VARCHAR | org | Generic category for general use |
| 53 | `GENERIC_CATG_10_C_NAME` | VARCHAR | org | Generic category for general use |
| 54 | `GENERIC_STR_1` | VARCHAR |  | Generic string item for general use |
| 55 | `GENERIC_STR_2` | VARCHAR |  | Generic string item for general use |
| 56 | `GENERIC_STR_3` | VARCHAR |  | Generic string item for general use |
| 57 | `GENERIC_STR_4` | VARCHAR |  | Generic string item for general use |
| 58 | `GENERIC_STR_5` | VARCHAR |  | Generic string item for general use |
| 59 | `GENERIC_NUM_IT_1` | NUMERIC |  | Generic numeric item for general use |
| 60 | `GENERIC_NUM_IT_2` | NUMERIC |  | Generic numeric item for general use |
| 61 | `GENERIC_NUM_IT_3` | NUMERIC |  | Generic numeric item for general use |
| 62 | `GENERIC_NUM_IT_4` | NUMERIC |  | Generic numeric item for general use |
| 63 | `GENERIC_NUM_IT_5` | NUMERIC |  | Generic numeric item for general use |
| 64 | `GENERIC_NUM_IT_6` | NUMERIC |  | Generic numeric item for general use |
| 65 | `GENERIC_NUM_IT_7` | NUMERIC |  | Generic numeric item for general use |
| 66 | `GENERIC_NUM_IT_8` | NUMERIC |  | Generic numeric item for general use |
| 67 | `GENERIC_NUM_IT_9` | NUMERIC |  | Generic numeric item for general use |
| 68 | `GENERIC_NUM_IT_10` | NUMERIC |  | Generic numeric item for general use |
| 69 | `GENERIC_DATE_1_DATE` | DATETIME |  | Generic date item for general use |
| 70 | `GENERIC_DATE_2_DATE` | DATETIME |  | Generic date item for general use |
| 71 | `GENERIC_DATE_3_DATE` | DATETIME |  | Generic date item for general use |
| 72 | `GENERIC_DATE_4_DATE` | DATETIME |  | Generic date item for general use |
| 73 | `GENERIC_DATE_5_DATE` | DATETIME |  | Generic date item for general use |
| 74 | `GENERIC_SEC_SINCE_MIDNIGHT_1` | NUMERIC |  | Generic time item for general use |
| 75 | `GENERIC_SEC_SINCE_MIDNIGHT_2` | NUMERIC |  | Generic time item for general use |
| 76 | `GENERIC_SEC_SINCE_MIDNIGHT_3` | NUMERIC |  | Generic time item for general use |
| 77 | `GENERIC_SEC_SINCE_MIDNIGHT_4` | NUMERIC |  | Generic time item for general use |
| 78 | `GENERIC_SEC_SINCE_MIDNIGHT_5` | NUMERIC |  | Generic time item for general use |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

