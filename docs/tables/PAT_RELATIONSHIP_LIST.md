# PAT_RELATIONSHIP_LIST

> This table includes the majority of patient contact demographic info, general relationship info, and patient-level relationship info. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `PAT_RELATIONSHIP_ID`  
**Columns:** 69  
**Org-specific columns:** 20  
**Joined by:** 18 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK | The unique identifier for the patient contact record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category ID for the patient contact |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient this patient contact is added to. |
| 4 | `PAT_LEVEL_RELATIONSHIP_YN` | VARCHAR |  | Indicates whether the patient contact should be displayed at the patient level. |
| 5 | `NAME` | VARCHAR |  | Patient contact's name. This column only displays names that are stored directly on patient contact records and will be blank for patient contact records that are linked to different patient records. Use the PAT_RELATIONSHIP_RECORD_NAME column instead if you want a single column that will display the names of both linked and unlinked patient contact records. |
| 6 | `GENDER_C_NAME` | VARCHAR | org | The gender category ID for the patient contact. |
| 7 | `BIRTH_DATE` | DATETIME |  | Patient contact's date of birth. |
| 8 | `HOUSE_NUM` | VARCHAR |  | Patient contact's house number. |
| 9 | `CITY` | VARCHAR |  | Patient contact's city of residence. |
| 10 | `STATE_C_NAME` | VARCHAR | org | The state category ID for the patient contact's residence. |
| 11 | `ZIP_CODE` | VARCHAR |  | Patient contact's postal code. |
| 12 | `DISTRICT_C_NAME` | VARCHAR | org | The district category ID for the patient contact's residence. |
| 13 | `COUNTY_C_NAME` | VARCHAR | org | The county category ID for the patient contact. |
| 14 | `COUNTRY_C_NAME` | VARCHAR | org | The country category ID for the patient contact. |
| 15 | `OCCUPATION` | VARCHAR |  | Patient contact's occupation. |
| 16 | `INTERP_NEEDED_YN` | VARCHAR |  | Indicates whether the patient contact requires a language interpreter. |
| 17 | `HEARING_IMPAIRED_YN` | VARCHAR |  | Indicates whether the patient contact is hard of hearing. |
| 18 | `VISUALLY_IMPAIRED_YN` | VARCHAR |  | Indicates whether the patient contact has low vision. |
| 19 | `SPEC_NEED_IMPAIR_C_NAME` | VARCHAR | org | The hearing and vision special needs category ID for the patient contact. |
| 20 | `RECORD_CREATION_DATE` | DATETIME |  | The date when the patient contact was created. |
| 21 | `PREFERRED_LANGUAGE_C_NAME` | VARCHAR | org | The preferred language category ID for the patient contact. |
| 22 | `DISPLAY_SEQUENCE` | INTEGER |  | Stores the order in which patient-level contacts display. |
| 23 | `SOCIAL_CLOSENESS_C_NAME` | VARCHAR | org | The social closeness category ID for the patient contact. |
| 24 | `SAME_HOUSEHOLD_YN` | VARCHAR |  | Indicates whether the patient contact lives in the same household as the patient. |
| 25 | `SUPPORT_NETWORK_YN` | VARCHAR |  | Indicates whether the patient contact is part of the patient's support network. |
| 26 | `CUSTODY_C_NAME` | VARCHAR | org | The custody category ID for the patient contact |
| 27 | `GUARDIAN_YN` | VARCHAR |  | Indicates whether the patient contact is the patient's legal guardian. |
| 28 | `PROTECTION_ORDER_YN` | VARCHAR |  | Indicates whether a protection order has been filed against the patient contact. |
| 29 | `LAST_REV_DTTM` | DATETIME (Attached) |  | Indicates the last instant that this record's relationship information was reviewed or updated from a patient-level encounter. |
| 30 | `LAST_REV_USER_ID` | VARCHAR |  | The unique ID of the user who most recently reviewed or updated this patient contact's information from a patient-level encounter. |
| 31 | `LAST_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `NOTIFY_ON_ADMSN_YN` | VARCHAR |  | Indicates whether the patient contact should be notified when the patient is admitted. |
| 33 | `LEGAL_RELATION_C_NAME` | VARCHAR | org | The legal relationship category ID for the patient contact. |
| 34 | `ACTV_HLTHCR_AGENT_YN` | VARCHAR |  | Indicates whether the patient contact is an active health care agent for the patient. |
| 35 | `GENERIC_CAT_1_C_NAME` | VARCHAR | org | Customer-labeled category item. |
| 36 | `GENERIC_CAT_2_C_NAME` | VARCHAR | org | Customer-labeled category item. |
| 37 | `GENERIC_CAT_3_C_NAME` | VARCHAR | org | Customer-labeled category item. |
| 38 | `GENERIC_CAT_4_C_NAME` | VARCHAR | org | Customer-labeled category item. |
| 39 | `GENERIC_STRING_1` | VARCHAR |  | Customer-labeled string item. |
| 40 | `GENERIC_STRING_2` | VARCHAR |  | Customer-labeled string item. |
| 41 | `GENERIC_STRING_3` | VARCHAR |  | Customer-labeled string item. |
| 42 | `GENERIC_STRING_4` | VARCHAR |  | Customer-labeled string item. |
| 43 | `AUTH_LETTER_RECIPIENT_YN` | VARCHAR |  | Indicates whether the patient contact is authorized to receive appointment letters. |
| 44 | `SEND_LETTERS_BY_DEFAULT_YN` | VARCHAR |  | Indicate whether the patient contact should receive appointment letters about the patient by default. |
| 45 | `LIMITATION_CODE_C_NAME` | VARCHAR | org | The limitation code category ID for a supervisory patient contact. |
| 46 | `RESPONSIBILITY_CODE_C_NAME` | VARCHAR | org | The responsibility code category ID for a supervisory patient contact. |
| 47 | `AUTHORITY_CODE_C_NAME` | VARCHAR | org | The authority code category ID for a supervisory patient contact. |
| 48 | `BUSINESS_IDENT` | VARCHAR |  | The unique ID of the business for a supervisory patient contact. |
| 49 | `PENDING_PAT_LEGAL_RELATION_C_NAME` | VARCHAR |  | The pending Healthcare Agent (HCA) relationship category ID for the patient contact. |
| 50 | `ACP_UPD_REJECTION_REASON_C_NAME` | VARCHAR | org | The rejection reason category ID for the advance care plan (ACP). |
| 51 | `ACP_UPD_REJECTION_REASON_TEXT` | VARCHAR |  | The patient-facing rejection reason for an update to the advance care plan (ACP). |
| 52 | `ACP_UPD_MYCHART_USER_ID` | VARCHAR |  | The unique ID of the MyChart user who updated the advance care plan (ACP). |
| 53 | `PAT_RELATIONSHIP_RECORD_NAME` | VARCHAR |  | The name of the patient contact record. If the patient contact record is linked to a different patient's record, the name will come from the patient record. Otherwise, it will come from the name stored directly on the patient contact record. If your organization does not allow users to link patient contacts to other patient records, this column will act the same as the NAME column in this table. |
| 54 | `ORDER_ISSUED_TASK_C_NAME` | VARCHAR | org | The issued order category ID for the patient contact with regard to the division of tasks amongst patient guardians. |
| 55 | `LIVING_STATUS_C_NAME` | VARCHAR | org | The living status category ID for the patient contact. Epic releases statuses of Alive and Deceased. Missing statuses are treated as Alive. |
| 56 | `PAT_CONTACT_ROW_TYPE_C_NAME` | VARCHAR |  | The patient contact type category ID for a patient contact. This column uses 0 for Person and 1 for Organization. |
| 57 | `ORG_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 58 | `ORG_RELIG_AFFL_ID` | VARCHAR |  | The unique ID of the religious affiliation linked to an organization patient contact. |
| 59 | `ORG_RELIG_AFFL_ID_RELIG_AFFIL_NAME` | VARCHAR |  | The name of the religious affiliation organization. |
| 60 | `ORG_WEBSITE` | VARCHAR |  | A website URL for the organization patient contact. |
| 61 | `ORG_FAX_NUMBER` | VARCHAR |  | The fax number for an organization patient contact. |
| 62 | `ORG_PRIMARY_CONTACT` | VARCHAR |  | The representative or point person for an organization contact. |
| 63 | `ORG_PRIMARY_CONTACT_PHONE` | VARCHAR |  | The phone number for the organization primary contact. |
| 64 | `ORG_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 65 | `MYPT_ID` | VARCHAR | shared | The unique id of the MyChart account associated with the patient contact, primarily for the purpose of granting the contact proxy access to the patient. |
| 66 | `FREETEXT_COMMENT` | VARCHAR |  | A free text comment on the contact |
| 67 | `PRIMARY_OR_FIRST_PHONE` | VARCHAR |  | The phone number of a patient contact. This is the primary phone number if one is marked primary, otherwise this is the first phone number listed for the patient contact. If the patient contact is linked to another record, this phone number is from the linked record, otherwise this phone number is from the patient contact record. |
| 68 | `EMERG_CONTACT_YN` | VARCHAR |  | Indicates whether a patient contact is an emergency contact. |
| 69 | `COMM_ACSS_C_NAME` | VARCHAR |  | Indicates whether the patient contact can receive notifications related to the patient. This can be set to Proxy Access, Basic Notifications, or No Notifications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (18)

| From | Column | Confidence |
|------|--------|------------|
| [APPT_LETTER_RECIPIENTS](APPT_LETTER_RECIPIENTS.md) | `PAT_RELATIONSHIP_ID` | high |
| [COMM_TRACE_EMAIL_RECPNTS](COMM_TRACE_EMAIL_RECPNTS.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_CONTACT_LIST](PAT_CONTACT_LIST.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_RELATIONSHIP_ADDR](PAT_RELATIONSHIP_ADDR.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_CONTEXT](PAT_REL_CONTEXT.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_EMAIL_ADDR](PAT_REL_EMAIL_ADDR.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_INFO_EPSD](PAT_REL_INFO_EPSD.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_INFO_FAM](PAT_REL_INFO_FAM.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_LANGUAGES](PAT_REL_LANGUAGES.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_NOTES](PAT_REL_NOTES.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_NOTES_EPSD](PAT_REL_NOTES_EPSD.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_PHONE_NUM](PAT_REL_PHONE_NUM.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_ROLES](PAT_REL_ROLES.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_ROLES_EPSD](PAT_REL_ROLES_EPSD.md) | `PAT_RELATIONSHIP_ID` | high |
| [PAT_REL_SPEC_NEEDS](PAT_REL_SPEC_NEEDS.md) | `PAT_RELATIONSHIP_ID` | high |
| [REL_CITIZENSHIP](REL_CITIZENSHIP.md) | `PAT_RELATIONSHIP_ID` | high |
| [V_EHI_AUDIT_RLA](V_EHI_AUDIT_RLA.md) | `PAT_RELATIONSHIP_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_RLA](V_EHI_REG_ITEM_AUDIT_RLA.md) | `PAT_RELATIONSHIP_ID` | high |

