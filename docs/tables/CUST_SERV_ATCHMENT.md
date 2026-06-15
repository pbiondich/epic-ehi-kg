# CUST_SERV_ATCHMENT

> Extracts the attachments for this NCS (customer service) record.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 41  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique ID of the customer service communication record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATCHMENT_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 4 | `ATCHMENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ATCHMENT_INSTANT` | DATETIME (UTC) |  | The instant that this attachment line was added to the customer service communication record. |
| 6 | `ATCHMENT_TYPE_C_NAME` | VARCHAR |  | The attachment type category ID for the customer service communication attachment. |
| 7 | `ATCHMENT_PT_CSN_ID` | NUMERIC |  | The unique contact serial number for the patient encounter that is attached to the customer service communication. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 8 | `ATCHMENT_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `ATCHMENT_EMP_GRP_ID` | VARCHAR |  | The unique ID of the employer group record that is attached to the customer service communication. |
| 10 | `ATCHMENT_EMP_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 11 | `ATCHMENT_VEN_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 12 | `ATCHMENT_MCR_ID` | VARCHAR |  | The unique ID of the carrier record that is attached to the customer service communication. |
| 13 | `ATCHMENT_MCR_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 14 | `ATCHMENT_REF_ID` | NUMERIC |  | The unique ID of the referral record that is attached to the customer service communication. |
| 15 | `ATCHMENT_CLM_ID` | NUMERIC |  | The unique ID of the AP Claim record that is attached to the customer service communication. |
| 16 | `ATCHMENT_NET_ID` | VARCHAR |  | The unique ID of the network record that is attached to the customer service communication. |
| 17 | `ATCHMENT_NET_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 18 | `ATCHMENT_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 19 | `ATCHMENT_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 20 | `ATCHMENT_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 21 | `ATCHMENT_PBA_ID` | VARCHAR |  | The unique ID of the premium billing account record that is attached to the customer service communication. |
| 22 | `ATCHMENT_EAR_ID` | NUMERIC |  | The unique ID of the account record that is attached to the customer service communication. |
| 23 | `ATCHMENT_NCS_ID` | NUMERIC |  | The unique ID of the customer service communication record that is attached to the customer service communication. |
| 24 | `ATCHMENT_RSN_C_NAME` | VARCHAR | org | The attachment reason category ID for the customer service communication attachment. |
| 25 | `ATCHMENT_RSN_CMT` | VARCHAR |  | The attachment reason comment for the customer service communication attachment. |
| 26 | `ATCHMENT_HAR_ID` | NUMERIC |  | The unique ID of the hospital account record that is attached to the customer service communication. |
| 27 | `ATCHMENT_CVG_ID` | NUMERIC |  | The unique ID of the coverage record that is attached to the customer service communication. |
| 28 | `ATCHMENT_PROG_ID_MEMBERSHIP_NAME` | VARCHAR |  | The name for membership/benefit record. |
| 29 | `ATCHMENT_ZIP` | VARCHAR |  | The ZIP code that was associated with the attachment when it was added to the customer service communication. |
| 30 | `ATCHMENT_PROSPECT_ID` | NUMERIC |  | The unique ID of the prospective patient record that is attached to the customer service communication. |
| 31 | `ATCHMENT_CAMPAIGN_ID` | NUMERIC |  | The unique ID of the campaign record that is attached to a customer service communication. |
| 32 | `ATCHMENT_CAMPAIGN_ID_CAMPAIGN_NAME` | VARCHAR |  | The name of the campaign record. |
| 33 | `ATCHMENT_ORDER_ID` | NUMERIC |  | Stores relevant order records for this NCS record. |
| 34 | `ATCHMENT_ESTIMATE_ID` | NUMERIC |  | The unique ID of the estimate record that is attached to the customer service communication. |
| 35 | `ATCHMENT_DOCUMENT_ID` | VARCHAR |  | The unique ID of the document record that is attached to this customer service communication line. |
| 36 | `ATCHMENT_CLAIM_RECON_ID` | VARCHAR |  | The unique ID of the rejected claim record that is attached to the customer service communication. |
| 37 | `ATCHMENT_RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 38 | `ATCHMENT_AUTH_REQUEST_ID` | NUMERIC |  | Stores relevant authorization requests for CRM |
| 39 | `ATCHMENT_AGENCY_ID` | VARCHAR |  | Stores the relevant agency (AGY) records for the CRM. |
| 40 | `ATCHMENT_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 41 | `ATCHMENT_AGENT_ID_AGENT_NAME` | VARCHAR |  | The name of the agent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

