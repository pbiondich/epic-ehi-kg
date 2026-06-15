# PAT_ENC_MSP_ACCDNT

> This table contains the Accident part of the Medicare Secondary Payor Information from the Patient (EPT) master file.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 38  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `CONTACT_DATE` | DATETIME |  | The date (calendar format) on which the encounter took place. |
| 3 | `NON_WORK_ACC_YN` | VARCHAR |  | Indicates whether the illness or injury is the result of a non-work-related accident. Y indicates that the illness or injury is the result of a non-work-related accident. N indicates that the illness or injury is not the result of a non-work-related accident. A null value indicates this item was not filled out. |
| 4 | `ACCDNT_TYPE_C_NAME` | VARCHAR | org | The accident type category ID for the MSPQ. |
| 5 | `ACCDNT_DATE` | DATETIME |  | The accident date for the MSPQ. |
| 6 | `ACCDNT_LOCATION_C_NAME` | VARCHAR | org | The accident location category ID for the MSPQ. |
| 7 | `ACCDNT_NON_LIAB_YN` | VARCHAR |  | Indicates whether non-liability insurance is available. Y indicates that there is non-liability insurance available. N indicates that there is not non-liability insurance available. A null value indicates this item was not filled out. |
| 8 | `INSURED_NAME` | VARCHAR |  | Name of the non-liability insurance holder. |
| 9 | `INSUR_COMPANY` | VARCHAR |  | Name of the non-liability insurance company. |
| 10 | `NON_LIAB_POLICY` | VARCHAR |  | Non-liability insurance policy number. |
| 11 | `NON_LIAB_CLAIM` | VARCHAR |  | Non-liability insurance claim number. |
| 12 | `NON_LIAB_INS_ADR_1` | VARCHAR |  | Line 1 of the non-liability insurance company's address. |
| 13 | `NON_LIAB_INS_ADR_2` | VARCHAR |  | Line 2 of the non-liability insurance company's address. |
| 14 | `NON_LIAB_INS_CITY` | VARCHAR |  | Non-liability insurance company's city. |
| 15 | `N_LIAB_INS_STATE_C_NAME` | VARCHAR | org | The category ID of the non-liability insurance company's state. |
| 16 | `NON_LIAB_INS_ZIP` | VARCHAR |  | Non-liability insurance company's zip code. |
| 17 | `THRD_PRTY_LIAB_YN` | VARCHAR |  | Indicates whether a third party is liable for this accident. Y indicates that a third party is liable for this accident. N indicates that a third party is not liable for this accident. A null value indicates this item was not filled out. |
| 18 | `ATTRNY_USD_YN` | VARCHAR | org | Indicates whether the patient has an attorney for this injury. Y indicates that the patient has an attorney for this injury. N indicates that the patient does not have an attorney for this injury. A null value indicates this item was not filled out. |
| 19 | `ACCDNT_LIAB_NAME` | VARCHAR |  | Name of the party responsible for the accident. |
| 20 | `ACCDNT_ATTRNY_NAME` | VARCHAR |  | Name of the patient's attorney or the responsible party's attorney. |
| 21 | `LIABILITY_POLICY` | VARCHAR |  | Liability insurance policy number. |
| 22 | `LIABILITY_CLAIM` | VARCHAR |  | Liability claim number. |
| 23 | `LIABILITY_ADR_1` | VARCHAR |  | Line 1 of attorney or insurance company's address. |
| 24 | `LIABILITY_ADR_2` | VARCHAR |  | Line 2 of attorney or insurance company's address. |
| 25 | `LIABILITY_CITY` | VARCHAR |  | Attorney or insurance company's city. |
| 26 | `LIABILITY_STATE_C_NAME` | VARCHAR |  | Attorney or accident liability insurance company's state. |
| 27 | `LIABILITY_ZIP` | VARCHAR |  | Attorney or insurance company's ZIP Code. |
| 28 | `ATTRNY_PHONE` | VARCHAR |  | Attorney or insurance company's telephone number. |
| 29 | `HAS_ADDL_LIAB_YN` | VARCHAR |  | Indicates whether the patient has additional liability insurers. Y indicates that the patient has additional liability insurers. N indicates that the patient does not have additional liability insurers. A null value indicates this item was not filled out. The additional information will be stored in table PAT_ENC_MSP_ADL_LB. |
| 30 | `HAS_ADDL_NLIAB_YN` | VARCHAR |  | Indicates whether the patient has additional non-liability insurers. Y indicates that the patient has additional non-liability insurers. N indicates that the patient does not have additional non-liability insurers. A null value indicates this item was not filled out. The additional information will be stored in table PAT_ENC_MSP_ADL_NL. |
| 31 | `NON_LIAB_SUB_ADR_1` | VARCHAR |  | Line 1 of the non-liability insurance subscriber's address. |
| 32 | `NON_LIAB_SUB_ADR_2` | VARCHAR |  | Line 2 of the non-liability insurance subscriber's address. |
| 33 | `NON_LIAB_SUB_CITY` | VARCHAR |  | Non-liability insurance subscriber's city. |
| 34 | `NON_LIAB_SUB_ZIP` | VARCHAR |  | Non-liability insurance subscriber's zip code. |
| 35 | `RESP_PARTY_ADR_1` | VARCHAR |  | Line 1 of the responsible party's address. |
| 36 | `RESP_PARTY_ADR_2` | VARCHAR |  | Line 2 of the responsible party's address. |
| 37 | `RESP_PARTY_CITY` | VARCHAR |  | Responsible party's city. |
| 38 | `RESP_PARTY_ZIP` | VARCHAR |  | Responsible party's zip code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

