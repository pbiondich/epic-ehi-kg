# PROV_COMM_SENSITIVE

> This table stores information about provider communications. This includes whether the communication is sensitive or not, where the communication originated from, and the communication job ID.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `COMM_INFO_JOB_ID` | VARCHAR |  | This item stores the job ID for the communication info table. Information stored in this table will stay the same for every recipient in one communication. |
| 5 | `COMM_FROM_USER_ID` | VARCHAR |  | This item stores the communication from user's ID. |
| 6 | `COMM_FROM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `COMM_SENSITIVE_C_NAME` | VARCHAR |  | This item stores the sensitive setting of a communication. |
| 8 | `COMM_TYPE_C_NAME` | VARCHAR | org | The type of communication, used to define a specific workflow for the communication. |
| 9 | `COMM_INFO_FROM_DEP_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `COMM_INFO_EXT_USR` | VARCHAR |  | Communication from external user, a free text string. |
| 11 | `COMM_MSG_ID` | VARCHAR |  | Universally unique ID for a communication. |
| 12 | `COMM_PARENT_ID` | VARCHAR |  | Message ID of the parent communication |
| 13 | `COMM_CONV_ID` | VARCHAR |  | The unique ID of the conversation, which is used to group related communications. |
| 14 | `COMM_FROM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

