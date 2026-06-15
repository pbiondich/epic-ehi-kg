# HSP_BFH_ACT_DATA_BDC

> This table stores billing activity history action-specific data. Every time a billing activity (ATM) is performed on a record or group of records, an activity history record (BFH) is logged. These activity history records store specific data related to each action that was performed on the activity. Each action (and its related data) is logged as a line in related group BFH 300. This table is specifically for actions performed on insurance follow-up (BDC) records.

**Primary key:** `BFH_ID`, `LINE`  
**Columns:** 44  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the billing activity history record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | The action category ID for this row in the billing activity history. The other data in this row represent specific values associated with this action performed. |
| 4 | `ACT_BDC_STATUS_C_NAME` | VARCHAR | org | This column stores the denial/correspondence record status category ID that is set as a result of this action. |
| 5 | `ACT_BDC_RESOLVE_REASON_C_NAME` | VARCHAR | org | This column stores the denial/correspondence record resolution reason category ID that is set as a result of this action. |
| 6 | `ACT_BDC_OWNING_AREA_C_NAME` | VARCHAR | org | This column stores the denial/correspondence record owning area category ID that is set as a result of this action. |
| 7 | `ACT_BDC_DENIAL_CATEGORY_C_NAME` | VARCHAR | org | This column stores the category ID of the denial record denial category that is set as a result of this action. |
| 8 | `ACT_BDC_ROOT_CAUSE_C_NAME` | VARCHAR | org | This column stores the denial/correspondence record root cause category ID that is set as a result of this action. |
| 9 | `ACT_BDC_RPT_REMIT_CODE_ID` | VARCHAR |  | This column stores the denial/correspondence record reporting remittance code ID that is set as a result of this action. |
| 10 | `ACT_BDC_RPT_REMIT_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 11 | `ACT_BDC_SOURCE_AREA_C_NAME` | VARCHAR |  | This column stores the denial/correspondence source area category ID that is set as a result of this action. |
| 12 | `ACT_BDC_PREVENTABLE_YN` | VARCHAR |  | This column stores the denial record preventable status that is set as a result of this action. 'Y' indicates that the denial was preventable. 'N' or NULL indicate that it was not preventable. |
| 13 | `ACT_BDC_APPEAL_STAGE_C_NAME` | VARCHAR | org | This column stores the denial appeal stage (I BDC 10130). |
| 14 | `ACT_BDC_APPEAL_DUE_DATE` | DATETIME |  | This column stores the denial appeal due date (I BDC 10022). |
| 15 | `ACT_BDC_APPEAL_USER_ID` | VARCHAR |  | This column stores the denial appealing user (I BDC 10027). |
| 16 | `ACT_BDC_APPEAL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `ACT_BDC_APPEAL_SUBMIT_DATE` | DATETIME |  | This column stores the denial appeal submission date (I BDC 10023). |
| 18 | `ACT_BDC_APPEAL_SUBMIT_MTHD_C_NAME` | VARCHAR | org | This column stores the denial appeal submission method (I BDC 10028). |
| 19 | `ACT_BDC_RES_OWNER_USER_ID` | VARCHAR |  | The column represents the resolution owner for the follow-up records. |
| 20 | `ACT_BDC_RES_OWNER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `ACT_BDC_SOURCE_USER_ID` | VARCHAR |  | The column represents the caused by user for the follow-up records. |
| 22 | `ACT_BDC_SOURCE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 23 | `ACT_BDC_SOURCE_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 24 | `ACT_BDC_APPEAL_SELECT_LN_YN` | VARCHAR |  | The column indicates whether denial resubmission had a manually-selected line. |
| 25 | `ACT_BDC_APPEAL_OVRIDE_DATA_YN` | VARCHAR |  | The column indicates whether resubmitted lines had override data. |
| 26 | `ACT_BDC_NEXT_FOLLOWUP_DATE` | DATETIME |  | The Next Follow-up Date that was changed as a result of this action. |
| 27 | `ACT_BDC_APPEAL_LEVEL_C_NAME` | VARCHAR |  | The appeal level set as a result of this action. |
| 28 | `ACT_BDC_ROI_RECIPIENT_ID` | VARCHAR |  | This column stores the recipient or organization (AGY record) specified when generating the Release of Information (ROI) documentation created from this action. |
| 29 | `ACT_BDC_ROI_RECIPIENT_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 30 | `ACT_BDC_ROI_SUB_MTHD_C_NAME` | VARCHAR | org | This column stores the submission method specified when generating the Release of Information (ROI) documentation created from this action. |
| 31 | `ACT_BDC_ROI_RELEASE_TMPLT_ID` | NUMERIC |  | This column stores the release template (RTM record) specified when generating the Release of Information (ROI) documentation created from this action. |
| 32 | `ACT_BDC_ROI_RELEASE_TMPLT_ID_ROI_TEMPLT_NAME` | VARCHAR |  | The name of the release template. |
| 33 | `ACT_BDC_PAYER_DOWNGRADE_TYPE_C_NAME` | VARCHAR |  | The BDC Payer Downgrade Type that is set as a result of this action. |
| 34 | `ACT_PAYER_DOWNGRADE_OUTCOME_C_NAME` | VARCHAR |  | The BDC Payer Downgrade Outcome that is set as a result of this action. |
| 35 | `ACT_BDC_RULE_ID` | VARCHAR |  | The BDC rule used for billing activities. |
| 36 | `ACT_BDC_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 37 | `ACT_BDC_FOLLOW_UP_CONTEXT_C_NAME` | VARCHAR |  | The follow-up context (I BDC 32) set on a follow-up BDC. |
| 38 | `ACT_BDC_ICN` | VARCHAR |  | Internal Control Number (ICN) to provide a payer in relation to a follow-up. |
| 39 | `ACT_BDC_FOL_UP_RESP_TYPE_C_NAME` | VARCHAR |  | The response type (I BDC 10507) set on a follow-up record. |
| 40 | `ACT_BDC_TRACKING_IDENT` | VARCHAR |  | The submission tracking ID (BDC-10502) set on a follow-up record. |
| 41 | `ACT_BDC_INCLUDE_AI_REFS_YN` | VARCHAR |  | Whether or not the user chose to include the automatically AI generated references in the release of information when starting a new appeal. |
| 42 | `ACT_BDC_INCL_FAX_CVR_SHEET_YN` | VARCHAR |  | Whether to include the fax cover sheet in the output. |
| 43 | `ACT_BDC_ADDL_SMARTTEXT_ID` | VARCHAR |  | The ID of the addtional SmartText that was used in the BDC level action. |
| 44 | `ACT_BDC_ADDL_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

