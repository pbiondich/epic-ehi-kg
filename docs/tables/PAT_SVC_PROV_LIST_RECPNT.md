# PAT_SVC_PROV_LIST_RECPNT

> This table stores information of service provider list recipients that received the list through a guest link.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `LIST_IDENT` | INTEGER |  | The unique ID in I EPT 97216 for the list that the recipient information is for. |
| 7 | `RECIPIENT_NAME` | VARCHAR |  | The name of the service provider list recipient. |
| 8 | `RECIPIENT_CONTACT_METHOD_C_NAME` | VARCHAR |  | The contact method used to send the service provider list to the recipient. |
| 9 | `RECIPIENT_PHONE` | VARCHAR |  | The phone number that was used to send the service provider list to the recipient. |
| 10 | `RECIPIENT_EMAIL` | VARCHAR |  | The email that was used to send the service provider list to the recipient. |
| 11 | `RECIPIENT_IS_NEW_CONTACT_YN` | VARCHAR |  | Indicates whether the recipient of a Patient Choice list is a new visit contact created when sharing the list. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

