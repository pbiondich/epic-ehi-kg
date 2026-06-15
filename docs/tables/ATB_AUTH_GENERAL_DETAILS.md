# ATB_AUTH_GENERAL_DETAILS

> This table contains information pertaining to the auth request details.

**Primary key:** `AUTH_BUNDLE_ID`  
**Columns:** 27  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `AUTH_PAYER_DCSN_C_NAME` | VARCHAR |  | The Payer Decision category ID for the Auth Bundle's payer decision information. |
| 3 | `AUTH_PA_REQ_TYPE_C_NAME` | VARCHAR |  | The Request Type category ID for the Auth Bundle's authorization request information. |
| 4 | `AUTH_SVC_TYPE_CODE_C_NAME` | VARCHAR |  | The Service Type category ID for the Auth Bundle's authorization request information. |
| 5 | `AUTH_PA_PRIORITY_C_NAME` | VARCHAR |  | The Auth Priority category ID for the Auth Bundle's authorization request information. |
| 6 | `AUTH_START_DATE` | DATETIME |  | The date when the Auth Bundle's authorization starts. |
| 7 | `AUTH_END_DATE` | DATETIME |  | The date when the Auth Bundle's authorization ends. |
| 8 | `AUTH_ADMISSION_TYPE_C_NAME` | VARCHAR | org | The Admission Type category ID for the Auth Bundle's authorization request information. |
| 9 | `AUTH_ADMISSION_SOURCE_C_NAME` | VARCHAR | org | The Admission Source category ID for the Auth Bundle's authorization request information. |
| 10 | `AUTH_PAT_STATUS_C_NAME` | VARCHAR | org | The Patient Status category ID for the Auth Bundle's authorization request information. |
| 11 | `AUTH_POS_TYPE_C_NAME` | VARCHAR | org | The POS Type category ID for the Auth Bundle's authorization request information. |
| 12 | `AUTH_PA_UB_TYPE_OF_FAC_C_NAME` | VARCHAR |  | The UB Type of Facility category ID for the Auth Bundle's authorization request information. |
| 13 | `AUTH_UB_BILL_CLASS_C_NAME` | VARCHAR |  | The UB Type of Bill category ID for the Auth Bundle's authorization request information. |
| 14 | `AUTH_CONTACT_NAME` | VARCHAR |  | The name of the contact person to ask for information about this authorization request. |
| 15 | `AUTH_CONTACT_PHONE` | VARCHAR |  | The phone number of the contact person to ask for information about this authorization request. |
| 16 | `AUTH_CONTACT_FAX` | VARCHAR |  | The fax number of the contact person to ask for information about this authorization request. |
| 17 | `AUTH_CONTACT_EMAIL` | VARCHAR |  | The email of the contact person to ask for information about this authorization request. |
| 18 | `AUTH_REQUESTER_PNTR` | VARCHAR |  | A pointer to the reference ID number used in the entities table to specify which entity is considered the requester. |
| 19 | `AUTH_DISCHARGE_DATE` | DATETIME |  | The date when the auth bundle request information ends as it pertains to a discharge. |
| 20 | `AUTH_REFERENCE_NUM` | VARCHAR |  | The reference number for the authorization as provided by the payer. |
| 21 | `AUTH_NUM` | VARCHAR |  | The authorization number that the payer provided about this particular authorization. |
| 22 | `AUTH_UMO_NAME` | VARCHAR |  | This item contains the contact name for this authorization's relevant UMO. |
| 23 | `AUTH_UMO_PHONE` | VARCHAR |  | Contains the phone number that should be used to contact this authorization's relevant UMO. |
| 24 | `AUTH_UMO_FAX` | VARCHAR |  | Contains the fax number for the authorization's relevant UMO. |
| 25 | `AUTH_UMO_EMAIL` | VARCHAR |  | Contains the email that should be used to contact the authorization's relevant UMO. |
| 26 | `AUTH_UM_DECISION_REASON` | VARCHAR |  | This string represents the reason for the utilization management decision that was made about this authorization. Corresponds to I AUT 1312 and I RTX 61212. |
| 27 | `AUTH_PAYER_REQUIREMENT_C_NAME` | NUMERIC |  | Indicates the payer has determined that authorization is required. Category values provide more detail. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

