# ENROLL_INFO

> The ENROLL_INFO table contains information about patient enrollments in research studies, including status, alias, start and end dates, and last modified user and instant.

**Primary key:** `ENROLL_ID`  
**Columns:** 28  
**Org-specific columns:** 1  
**Joined by:** 35 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK | The unique ID of the patient-study association record for this row. This column is frequently used to link to the ENROLL_INFO table. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status, such as hidden or soft-deleted. |
| 3 | `RESEARCH_STUDY_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 4 | `PAT_ID` | VARCHAR | FK→ | Unique ID of the associated Patient record. |
| 5 | `ENROLL_STATUS_C_NAME` | VARCHAR | org | Status category number of the patient's enrollment in the study. |
| 6 | `STUDY_ALIAS` | VARCHAR |  | Patient's alias for the study enrollment. |
| 7 | `ENROLL_START_DT` | DATETIME |  | Start date of the patient's enrollment in the study. |
| 8 | `ENROLL_END_DT` | DATETIME |  | End date of the patient's enrollment in the study. |
| 9 | `ENROLL_CMT_NOTE_ID` | VARCHAR |  | The ID number for comments/notes associated with the enrollment. |
| 10 | `LAST_MOD_DTTM` | DATETIME (Attached) |  | Instant the enrollment information was last modified. |
| 11 | `LAST_MOD_USER_ID` | VARCHAR |  | User who modified the enrollment information last. |
| 12 | `LAST_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `STUDY_BRANCH_ID` | VARCHAR |  | For a patient enrolled in a research study that has multiple branches (or arms), this item stores the ID of the specific branch of that study to which the patient is assigned. |
| 14 | `MYC_APPROVING_EMP_ID` | VARCHAR |  | Either the user who was asked to approve this MyChart recruitment request if it is still awaiting approval, or the one who did approve or decline the request. |
| 15 | `MYC_APPROVING_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `ADVERSE_EVENT_REVIEW_UTC_DTTM` | DATETIME (UTC) |  | The date and time of last review for the adverse events for this study association. |
| 17 | `ADVERSE_EVENT_REVIEW_USER_ID` | VARCHAR |  | The unique ID of the last reviewing user for the adverse events for this study association. |
| 18 | `ADVERSE_EVENT_REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `RECRUITMENT_QUESR_ANSWER_ID` | VARCHAR |  | The unique identifier of the recruitment questionnaire answers for this study association. |
| 20 | `MYC_RESPONSE_TYPE_C_NAME` | VARCHAR |  | The MyChart response type category ID for the enrollment. |
| 21 | `FIRST_INVITATION_SENT_YN` | VARCHAR |  | Indicates whether the patient has ever received a research study invitation for this patient-study association. 'Y' indicates that the patient has received a research study invitation for this patient-study association. 'N' or NULL indicate that the patient has not received a research study invitation for this patient-study association. |
| 22 | `FIRST_INVITE_LAST_MOD_SOURCE_C_NAME` | VARCHAR |  | The modification source category ID of the source from which the first research study invitation was sent for this patient-study association. |
| 23 | `FIRST_INVITATION_SENT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant at which the first research study invitation was sent for this patient-study invitation. |
| 24 | `LAST_DEMO_AUTH_TOKEN` | VARCHAR |  | The last demographic authentication token that was generated for this patient-study association. |
| 25 | `OPA_MANUAL_OUTREACH_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant at which the first manual OPA outreach was performed for this patient-study association. |
| 26 | `OPA_AUTO_OUTREACH_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant at which the first automatic OPA outreach was performed for this patient-study association. |
| 27 | `PAT_INITIATED_INTEREST_C_NAME` | VARCHAR |  | The patient-initiated interest category ID for the enrollment. |
| 28 | `CREATION_COMM_ID` | NUMERIC |  | The unique ID of the CRM case that resulted in the creation of the study association record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (35)

| From | Column | Confidence |
|------|--------|------------|
| [ADVERSE_EVENT_INFO](ADVERSE_EVENT_INFO.md) | `ENROLL_ID` | high |
| [ADVERSE_EVENT_REVIEW_INFO](ADVERSE_EVENT_REVIEW_INFO.md) | `ENROLL_ID` | high |
| [CL_LAR_ID](CL_LAR_ID.md) | `ENROLL_ID` | high |
| [CL_LAR_ID_HX](CL_LAR_ID_HX.md) | `ENROLL_ID` | high |
| [CL_QANSWER](CL_QANSWER.md) | `ENROLL_ID` | high |
| [DATA_CAPTURE_FORMS](DATA_CAPTURE_FORMS.md) | `ENROLL_ID` | high |
| [DOCS_NEEDING_RECONSENT](DOCS_NEEDING_RECONSENT.md) | `ENROLL_ID` | high |
| [DOC_INFORMATION_2](DOC_INFORMATION_2.md) | `ENROLL_ID` | high |
| [ELIGIBILITY_ANALYSIS](ELIGIBILITY_ANALYSIS.md) | `ENROLL_ID` | high |
| [ENROLL_INFO_HX](ENROLL_INFO_HX.md) | `ENROLL_ID` | high |
| [ENROLL_INFO_HX_1](ENROLL_INFO_HX_1.md) | `ENROLL_ID` | high |
| [ENROLL_LINKED_CSN2](ENROLL_LINKED_CSN2.md) | `ENROLL_ID` | high |
| [ENROLL_LINKED_CSN_HX](ENROLL_LINKED_CSN_HX.md) | `ENROLL_ID` | high |
| [ENROLL_QUESR](ENROLL_QUESR.md) | `ENROLL_ID` | high |
| [ENROLL_QUESR_SERIES](ENROLL_QUESR_SERIES.md) | `ENROLL_ID` | high |
| [ENROLL_REC_HX](ENROLL_REC_HX.md) | `ENROLL_ID` | high |
| [ENROLL_STAT_CHNG](ENROLL_STAT_CHNG.md) | `ENROLL_ID` | high |
| [ENROLL_STAT_CHNG_DT_HX](ENROLL_STAT_CHNG_DT_HX.md) | `ENROLL_ID` | high |
| [ENROLL_STAT_CHNG_HX](ENROLL_STAT_CHNG_HX.md) | `ENROLL_ID` | high |
| [ENROLL_STUDY_COORD](ENROLL_STUDY_COORD.md) | `ENROLL_ID` | high |
| [ENROLL_TIMELINE](ENROLL_TIMELINE.md) | `ENROLL_ID` | high |
| [EPISODE_2](EPISODE_2.md) | `ENROLL_ID` | high |
| [IB_RSH_ASSOC_MSG](IB_RSH_ASSOC_MSG.md) | `ENROLL_ID` | high |
| [IP_WORKLIST](IP_WORKLIST.md) | `ENROLL_ID` | high |
| [MYC_CONVO](MYC_CONVO.md) | `ENROLL_ID` | high |
| [NOTE_RESEARCH_LINK](NOTE_RESEARCH_LINK.md) | `ENROLL_ID` | high |
| [ORD_RESEARCH_CODE](ORD_RESEARCH_CODE.md) | `ENROLL_ID` | high |
| [PAT_ENC_RSH](PAT_ENC_RSH.md) | `ENROLL_ID` | high |
| [RSH_INVITATIONS](RSH_INVITATIONS.md) | `ENROLL_ID` | high |
| [RSH_INVITE_AUTH_TOKENS](RSH_INVITE_AUTH_TOKENS.md) | `ENROLL_ID` | high |
| [RSH_INVITE_INV_VIEW_INST](RSH_INVITE_INV_VIEW_INST.md) | `ENROLL_ID` | high |
| [RSH_INVITE_RECPNTS](RSH_INVITE_RECPNTS.md) | `ENROLL_ID` | high |
| [RSH_INVITE_RECPNT_ACTV](RSH_INVITE_RECPNT_ACTV.md) | `ENROLL_ID` | high |
| [RSH_PAT_INIT_INTEREST_HX](RSH_PAT_INIT_INTEREST_HX.md) | `ENROLL_ID` | high |
| [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | `ENROLL_ID` | high |

