# CAL_COMM_HX

> Stores the history of communications. Each column audits a value in CAL_COMM_TRACKING of the same name, unless otherwise specified in the column description.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 49  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique identifier for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMM_TYPE_C_NAME` | VARCHAR |  | Stores the category identifier of the communication type. |
| 4 | `COMM_PURPOSE_C_NAME` | VARCHAR |  | Stores the category identifier of the communication purpose. |
| 5 | `LOGIN_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 6 | `COMM_INSTANT_LOCAL_DTTM` | DATETIME (Attached) |  | Stores the instant of the communication in local time. |
| 7 | `COMM_END_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant in UTC the communication ended. |
| 8 | `COMM_COMMENT` | VARCHAR |  | Stores the comment on the communication. |
| 9 | `COMM_CMT_NOTE_ID` | VARCHAR |  | Stores the unique identifier of the associated note. |
| 10 | `CALLER_NAME` | VARCHAR |  | Stores the caller's name. |
| 11 | `PHONE_NUMBER` | VARCHAR |  | Stores the phone number used for the communication. |
| 12 | `PHONE_TYPE_C_NAME` | VARCHAR | org | Stores the category identifier of the type of phone communication. |
| 13 | `CALL_TYPE_C_NAME` | VARCHAR | org | Stores the category identifier of the call type. |
| 14 | `CALL_OUTCOME_C_NAME` | VARCHAR | org | Stores the category identifier of the outcome. |
| 15 | `LAB_CALL_TOPIC_C_NAME` | VARCHAR | org | Stores the category identifier of the lab call topic. |
| 16 | `COMM_CONTACT_TYPE_C_NAME` | VARCHAR | org | Stores the category identifier of the type of record being contacted. |
| 17 | `CONTACT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `CONTACT_PLAN_GRP_ID` | VARCHAR |  | Stores the unique identifier of the employer group being contacted. This corresponds to CAL_COMM_TRACKING.CONTACT_EMPGROUP_ID. |
| 19 | `CONTACT_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 20 | `CONTACT_CARRIER_ID` | VARCHAR |  | Stores the unique identifier of the carrier being contacted. |
| 21 | `CONTACT_CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 22 | `CONTACT_ACCT_ID` | NUMERIC |  | Stores the unique identifier of the guarantor being contacted. |
| 23 | `CONTACT_NETWORK_ID` | VARCHAR |  | Stores the unique identifier of the network being contacted. |
| 24 | `CONTACT_NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 25 | `CONTACT_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 26 | `CONTACT_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 27 | `CONTACT_PB_ACCT_ID` | VARCHAR |  | Stores the unique identifier of the premium billing account being contacted. This corresponds to CAL_COMM_TRACKING.CONTACT_PBA_ID. |
| 28 | `CONTACT_REGISTRY_ID` | NUMERIC |  | Stores the unique identifier of the pool being contacted. This corresponds to CAL_COMM_TRACKING.CONTACT_HIP_ID. |
| 29 | `CONTACT_REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 30 | `CONTACT_USER_ID` | VARCHAR |  | Stores the unique identifier of the user being contacted. |
| 31 | `CONTACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `CONTACT_ADHOC_NAME` | VARCHAR |  | Stores the name of an ad hoc contact. |
| 33 | `CONTACT_ADHOC_FAX` | VARCHAR |  | Stores the fax number of an ad hoc contact. |
| 34 | `CONTACT_ADHOC_PHONE` | VARCHAR |  | Stores the phone number of an ad hoc contact. |
| 35 | `CONTACT_ADHOC_ADDR` | VARCHAR |  | Stores the address of an ad hoc contact. |
| 36 | `CONTACT_ADHOC_CITY` | VARCHAR |  | Stores the city of an ad hoc contact. |
| 37 | `CONTACT_ADHOC_STATE_C_NAME` | VARCHAR | org | Stores the category identifier of the state of an ad hoc contact. This corresponds to CAL_COMM_TRACKING.CONTACT_ADHOC_STT_C. |
| 38 | `CONTACT_ADHOC_ZIP` | VARCHAR |  | Stores the zip code of an ad hoc contact. |
| 39 | `CONTACT_ADHOC_COUNTRY_C_NAME` | VARCHAR | org | Stores the category identifier of the country of an ad hoc contact. This corresponds to CAL_COMM_TRACKING.CONTACT_ADHOC_CTR_C and can be translated using ZC_COUNTRY_2. |
| 40 | `CONTACT_PHARMACY_ID` | NUMERIC |  | Stores the unique identifier of the pharmacy being contacted. This corresponds to CAL_COMM_TRACKING.CONTACT_PHR_ID. |
| 41 | `CONTACT_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 42 | `CONTACT_WORKER_ID` | NUMERIC |  | Stores the unique identifier of the worker being contacted. |
| 43 | `CONTACT_WORKER_PAGER_C_NAME` | VARCHAR | org | Stores the category identifier of the worker pager being contacted. This can be translated using ZC_DEFAULT_PAGER. |
| 44 | `CONTACT_PROSPECT_ID` | NUMERIC |  | Stores the unique identifier of the prospective party being contacted. |
| 45 | `CONTACT_SUBMITTER_ID` | NUMERIC |  | Stores the unique identifier of the submitter being contacted. |
| 46 | `CONTACT_SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 47 | `CHANGE_USER_ID` | VARCHAR |  | The history change user is the user who triggered the update to record this history line. This means that the user who recorded this line changed the state of the record from the values on this line and set the values on the following line or the current state of the record if this is the last line in the history. This differs from I CAL 8010 which tracks the entry user who is normally the user who made the actual communication. |
| 48 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 49 | `PAT_LOCATION` | VARCHAR |  | History of the patient location item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

