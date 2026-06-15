# RA_CDI_REVIEW

> A table to hold the recommendations made from Risk Adjustment CDI Reviews.

**Primary key:** `CODING_RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the coding record record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RA_CDI_TYPE_C_NAME` | VARCHAR |  | The type of recommendation being made - component or diagnosis. |
| 6 | `RA_CDI_COMP_TEMPLATE_VERSION_C_NAME` | VARCHAR | org | The version of the component that a recommendation is being added to. One risk adjustment model may have multiple versions, as the sets of diagnoses related to a component may be changed over time by a payer or organization. |
| 7 | `RA_CDI_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 8 | `RA_CDI_DX_EDG_CODE_SET_C_NAME` | VARCHAR | org | The code set of the diagnosis being recommended in I COD 803. |
| 9 | `RA_CDI_RECOM_ACTION_C_NAME` | VARCHAR |  | The recommendation on the component or diagnosis. |
| 10 | `RA_CDI_REVIEWED_YN` | VARCHAR |  | If this recommendation has been acted on by a provider |
| 11 | `RA_CDI_REC_CMT` | VARCHAR |  | The reviewer's comment associated with their recommendation. |
| 12 | `RA_CDI_REC_ORIGIN_C_NAME` | VARCHAR |  | The source of the recommendation. |
| 13 | `RA_CDI_REC_NEW_YN` | VARCHAR |  | If the diagnosis or component being recommended or commented on is manually added by a user in this review. |
| 14 | `REC_SRC_CODING_RECORD_CSN_ID` | NUMERIC |  | The CSN of the review where this diagnosis or component recommendation was first added. |
| 15 | `RA_REC_EVID_TYPE_C_NAME` | VARCHAR |  | Stores the source of the evidence that was showing to a coder when the recommendation was made. |
| 16 | `RA_CDI_ORIG_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 17 | `RA_CDI_ORIG_DX_EDG_CODE_SET_C_NAME` | VARCHAR |  | The code set of the diagnosis that was recommended in RA_CDI_ORIG_DX_ID. |
| 18 | `RA_CDI_REC_USER_ID` | VARCHAR |  | The CDI user associated with the recommendation. |
| 19 | `RA_CDI_REC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `RA_CDI_RELEVANT_QUERY_CSN_ID` | NUMERIC |  | Stores the query record that was relevant to this CDI user's recommendation. The query information was seen by the user when they were making this recommendation. The query information is shown downstream if the query does not disagree with the user's recommendation. |
| 21 | `RA_CDI_REC_DISCARD_YN` | VARCHAR |  | Item that is used for pended reviews when the condition's attached query has been discarded in a pended review. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

