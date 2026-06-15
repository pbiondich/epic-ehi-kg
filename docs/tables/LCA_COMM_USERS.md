# LCA_COMM_USERS

> Table contains information regarding the sender of a communication and the recipients of the communication. In a record the 1st entry is assumed to be the sender, subsequent entries are the recipients.

**Primary key:** `COMMUNICATION_ID`, `LINE`  
**Columns:** 29  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | LCA routing record id |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMM_NAME` | VARCHAR |  | Name of the sender/recipient |
| 4 | `COMM_INI` | VARCHAR |  | INI of the sender/recipient |
| 5 | `COMM_ID_USER` | VARCHAR |  | ID the sender/recipient |
| 6 | `FAX_NUM` | VARCHAR |  | fax number of the sender/recipient that communication would be sent to if a fax method was used to send the communication |
| 7 | `PHONE_NUM` | VARCHAR |  | phone number of the sender/recipient |
| 8 | `ADDRESS` | VARCHAR |  | address of the sender/recipient that communication would be sent to if a mailing method was used to send the communication |
| 9 | `CITY` | VARCHAR |  | city of the sender/recipient that communication would be sent to if a mailing method was used to send the communication |
| 10 | `STATE` | VARCHAR |  | state of the sender/recipient that communication would be sent to if a mailing method was used to send the communication |
| 11 | `ZIP_CODE` | VARCHAR |  | zip code of the sender/recipient that communication would be sent to if a mailing method was used to send the communication |
| 12 | `COUNTRY` | VARCHAR |  | country of the sender/recipient that communication would be sent to if a mailing method was used to send the communication |
| 13 | `SENT_METHOD_C_NAME` | VARCHAR | org | The Send Method category number for the communication. |
| 14 | `FILE_CREATED_YN` | VARCHAR |  | Indicates if a file was created for that recipient. If so can look in attachments at blob columns for the file name. |
| 15 | `EMAIL` | VARCHAR |  | email address of the sender/recipient |
| 16 | `HOUSE_NUM` | VARCHAR |  | House number of the sender/recipient that communication would be sent to if mailing method was used to send communication. |
| 17 | `DISTRICT_C_NAME` | VARCHAR | org | District of the sender/recipient that communication would be sent to if mailing method was used to send the communication. |
| 18 | `COUNTY_C_NAME` | VARCHAR | org | County of the sender/recipient that communication would be sent to if mailing method was used to send the communication. |
| 19 | `COMM_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this communication if COMM_INI is EMP. This column is frequently used to link to the CLARITY_EMP table. |
| 20 | `COMM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `COMM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `COMM_PAT_ID` | VARCHAR | FK→ | The unique ID associated with the patient record for this communication if COMM_INI is EPT. This column is frequently used to link to the PATIENT table. |
| 23 | `ORGANIZATION_ID` | NUMERIC | FK→ | The unique ID associated with the organization record for this communication if COMM_INI is DXO. This column is frequently used to link to the ORG_DETAILS table. |
| 24 | `ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 25 | `COMM_REG_ID` | NUMERIC |  | The unique ID associated with the pool record for this communication if COMM_INI is HIP. This column is frequently used to link to the CLARITY_HIP table. |
| 26 | `COMM_REG_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 27 | `CONSENT_DOC_INFO_ID` | VARCHAR |  | DCS record that contains patient consent for sending the communication to this recipient. |
| 28 | `COMM_CE_SUB_MTHD_C_NAME` | VARCHAR |  | The sub-routing method category ID for the communication. |
| 29 | `SENT_DIRECT_ADDRESS` | VARCHAR |  | The address level Direct address of the recipient to whom the communication is routed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COMM_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `ORGANIZATION_ID` | [ORG_DETAILS](ORG_DETAILS.md) | sole_pk | high |

