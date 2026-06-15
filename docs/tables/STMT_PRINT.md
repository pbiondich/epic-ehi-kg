# STMT_PRINT

> The STMT_PRINT table contains information about your statement print and detail bill records.

**Primary key:** `PRINT_ID`  
**Columns:** 35  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `GUAR_ACCT_ID` | NUMERIC |  | This column stores the unique identifier for the guarantor account that received this statement print or detail bill. |
| 3 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `INVOICE_NUMBER` | VARCHAR |  | The master invoice number for a statement print or detail bill. |
| 5 | `INV_NUM_ASGN_DT` | DATETIME |  | The date on which the invoice number was generated. |
| 6 | `IS_DEMAND_STMT_YN` | VARCHAR |  | Whether this is a demand statement. |
| 7 | `STMT_END_BATCH_DATE` | DATETIME |  | End system batch date for the statement. Only transactions posted on or before this date can be included on the statement. |
| 8 | `STMT_PROC_DATE` | DATETIME |  | The date statement data was populated into this print record. |
| 9 | `BILL_HOME_PHONE` | VARCHAR |  | Home phone of the guarantor. |
| 10 | `BILL_WORK_PHONE` | VARCHAR |  | Work phone of the guarantor. |
| 11 | `RESPONSIBLE_PARTY_NAME` | VARCHAR |  | Addressee of the statement. This is usually guarantor's name. |
| 12 | `BILL_HOUSE_NUM` | VARCHAR |  | House number of the guarantor. |
| 13 | `BILL_DISTRICT_C_NAME` | VARCHAR | org | District of the guarantor. |
| 14 | `BILL_CITY` | VARCHAR |  | The city of the guarantor. |
| 15 | `BILL_COUNTY_C_NAME` | VARCHAR | org | County of the guarantor. |
| 16 | `BILL_STATE` | VARCHAR |  | The state of the guarantor. |
| 17 | `BILL_COUNTRY_C_NAME` | VARCHAR | org | Country of the guarantor. |
| 18 | `BILL_ZIP` | VARCHAR |  | The zip code of the guarantor. |
| 19 | `BILL_DELIV_POINT` | VARCHAR |  | The billing delivery point is a two digit extension to the nine digit US zipcode, with values from 00 to 99. This is typically not seen in human readable format. This can be used when printed as a bar code on a letter to obtain a bulk mail discount. |
| 20 | `START_SERVICE_DATE` | DATETIME |  | If specified, professional transactions with service date before this date and hospital accounts with discharge date before this date will be excluded from statement. |
| 21 | `END_SERVICE_DATE` | DATETIME |  | If specified, professional transactions with service date after this date and hospital accounts with discharge date after this date will be excluded from statement. |
| 22 | `BILL_RUN_TYPE_C_NAME` | VARCHAR |  | The type of this enterprise bill print. |
| 23 | `PAT_ENC_CSN_ID` | INTEGER | FK→ | Stores the linked patient serial number of the patient on the statement. If the guarantor is a patient in the system, this will be the patient for the guarantor. Otherwise if there is only one patient on the statement, it will be that patient. If there are multiple patients on the statement, this item will be blank. |
| 24 | `IS_MYCHART_NOTIF_YN` | VARCHAR |  | Stores if the statement/detail bill notification was sent via MyChart. |
| 25 | `HSP_BUCKET_ID` | NUMERIC |  | The liability bucket record ID that requested this bill print record. |
| 26 | `CLAIM_PRINT_ID` | NUMERIC | shared | The claim print record ID that requested this bill print record. |
| 27 | `ROI_ID` | VARCHAR |  | The release of information record ID that requested this bill print record. |
| 28 | `ROI_DATE` | DATETIME |  | The contact date of the release of information record that requested this bill print record. |
| 29 | `ROI_DOC_KEY` | VARCHAR |  | The document reference key for the release of information record that requested this bill print record. |
| 30 | `COMMUNICATION_TOPIC_SETTING_ID` | NUMERIC |  | Stores the topic that will be used for sending the relevant communication. |
| 31 | `COMMUNICATION_TOPIC_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 32 | `STMT_SCENARIO_C_NAME` | VARCHAR |  | Stores the scenario the statement falls under. It can be used by PDF statements to build content to match what the guarantor would eventually receive in the notification. |
| 33 | `AUTH_BILL_USER_MYPT_ID` | VARCHAR |  | Stores the authorized billing user if the statement is a copy generated for that for that user upon request. |
| 34 | `ORIGINAL_STMT_PRINT_ID` | NUMERIC |  | If the current statement is a copy generated for the authorized user, this item will point to the original statement sent to the guarantor. |
| 35 | `RECIPIENT_NAME` | VARCHAR |  | Name of the person receiving the statement. If it is an authorized user copy, then this would be the name of that user. Otherwise, this will usually be the guarantor's name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

