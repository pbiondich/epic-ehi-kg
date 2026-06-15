# SPOC_PARTICIPANTS

> List of participants on the plan of care tracked over versions as the plan is updated.

**Primary key:** `POC_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 29  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier for the plan of care record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PART_TYPE_C_NAME` | VARCHAR |  | The type category ID for a plan of care participant. |
| 6 | `PART_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `PART_COMM_MEM` | VARCHAR |  | This item contains the free text name of a community member participating in the creation of the plan of care. |
| 8 | `PART_COMM_MEM_CNCT` | VARCHAR |  | This item contains user entered contact information about a community member participant. |
| 9 | `PART_COMM_MEM_REL` | VARCHAR |  | This item contains the relationship to the patient of a free text community member added to the plan of care. |
| 10 | `PART_DISCIPLINE_ID` | VARCHAR |  | The unique ID of the discipline for the plan of care participant. |
| 11 | `PART_DISCIPLINE_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |
| 12 | `PART_ROLE_C_NAME` | VARCHAR |  | The role category ID for a plan of care participant. |
| 13 | `PART_CMT` | VARCHAR |  | This item contains comments about the participants. Comments up to 100 characters are allowed. |
| 14 | `PART_SIGNER_YN` | VARCHAR |  | Indicates whether the participant in required to sign the plan of care. |
| 15 | `PART_SIGNED_YN` | VARCHAR |  | Indicates whether the participant has signed the plan of care. |
| 16 | `PART_SIG_DATE` | DATETIME |  | The date when the participant signed the plan of care. |
| 17 | `PART_SIG_MTHD_C_NAME` | VARCHAR |  | The signing method category ID for a plan of care participant. |
| 18 | `PART_MK_SIG_RSN_C_NAME` | VARCHAR | org | The mark as signed reason category ID for the plan of care participant. |
| 19 | `PART_MK_SIG_CMT` | VARCHAR |  | This item contains a comment for the reason a participant was marked as signed. |
| 20 | `PART_CONTACT_RLA_ID` | NUMERIC |  | The unique ID of the patient contact added as a participant for a plan of care. |
| 21 | `PART_DECLN_RSN_C_NAME` | VARCHAR | org | The decline reason category ID for a plan of care participant. |
| 22 | `PART_DECLN_RSN_CMT` | VARCHAR |  | This item contains the comment for the reason a participant declined to sign the plan. |
| 23 | `PART_EXTEND_ROLE_C_NAME` | VARCHAR | org | The extended role category ID for the plan of care participant. |
| 24 | `PART_AGRMNT_TYP_C_NAME` | VARCHAR |  | The agreement participant type category ID for participants on an agreement. |
| 25 | `PART_CONT_STATUS_C_NAME` | VARCHAR |  | This item stores the contribution status for the corresponding participant on a plan of care. |
| 26 | `PART_CONTRIBN_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant the contribution for the corresponding participant was recorded on the plan of care. |
| 27 | `PART_COMM_MEM_PAT_FACING_NAME` | VARCHAR |  | This item contains the free text patient-facing name of a community member participating in the creation of the plan of care. |
| 28 | `PART_SIG_DOCUMENT_ID` | VARCHAR |  | The linked E-Signature document for a given participant. |
| 29 | `PART_PROXY_MYPT_ID` | VARCHAR |  | This item contains a WPR ID which is a record that holds the details of a proxy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

