# CL_QANSWER

> This table contains general information about questionnaire answer records. For example, the questionnaire the answer record is for, the date it was answered, and whether the answer record is closed.

**Primary key:** `ANSWER_ID`  
**Columns:** 11  
**Joined by:** 34 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK | The unique ID of the questionnaire answer record. |
| 2 | `REC_CREATE_USER_ID` | VARCHAR |  | The unique ID of the user who created this record. |
| 3 | `REC_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `PE_HX_REVIEWED_YN` | VARCHAR |  | This records whether a provider has viewed the history data in this record in the MyChart\Welcome patient history visit navigator section. It is assumed that if the provider has had a chance to look at the submitted history data, they have filed or reviewed the data. After the provider review, MyChart and Welcome will start pre-loading answers from the history section rather than the patient's previous responses. |
| 5 | `PE_HX_DONE_YN` | VARCHAR |  | This records whether a provider has completed review of the history data in this record in the MyChart\Welcome patient history visit navigator section. After the provider review, MyChart and Welcome will start pre-loading answers from the history section rather than the patient's previous responses. |
| 6 | `ENROLL_ID` | NUMERIC | FK→ | The unique identifier of the research study-patient association for the questionnaire. |
| 7 | `IMG_PROC_ORDER_ID` | NUMERIC |  | Virtual item that returns the record ID for the ORD that points to the given Questionnaire Answer |
| 8 | `WORKFLOW_DURATION` | INTEGER |  | The amount of time (in seconds) that was spent answering the patient-entered questionnaire. |
| 9 | `FURTHEST_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 10 | `PARENT_ANSWER_ID` | VARCHAR |  | The parent questionnaire response that was branched from to get to this questionnaire. |
| 11 | `CONFIDENTIAL_YN` | VARCHAR |  | The confidential status for the questionnaire answers. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

## Joined in — referenced by (34)

| From | Column | Confidence |
|------|--------|------------|
| [CL_QANSWER_ATTEMPT](CL_QANSWER_ATTEMPT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_AUDIT](CL_QANSWER_AUDIT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_DOCS](CL_QANSWER_EVID_DOCS.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_DXS_TXT](CL_QANSWER_EVID_DXS_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_EDOCS](CL_QANSWER_EVID_EDOCS.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_EDOCS_TXT](CL_QANSWER_EVID_EDOCS_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_MEDS_TXT](CL_QANSWER_EVID_MEDS_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_NOTES_TXT](CL_QANSWER_EVID_NOTES_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_PAT_TXT](CL_QANSWER_EVID_PAT_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_PRBLT_TXT](CL_QANSWER_EVID_PRBLT_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_PROCS_TXT](CL_QANSWER_EVID_PROCS_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_REVC_TXT](CL_QANSWER_EVID_REVC_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_EVID_SURG_TXT](CL_QANSWER_EVID_SURG_TXT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_FAMILY_MEMBERS](CL_QANSWER_FAMILY_MEMBERS.md) | `ANSWER_ID` | high |
| [CL_QANSWER_FAMILY_PROBS](CL_QANSWER_FAMILY_PROBS.md) | `ANSWER_ID` | high |
| [CL_QANSWER_GEN_CMT](CL_QANSWER_GEN_CMT.md) | `ANSWER_ID` | high |
| [CL_QANSWER_OVTM](CL_QANSWER_OVTM.md) | `ANSWER_ID` | high |
| [CL_QANSWER_QA](CL_QANSWER_QA.md) | `ANSWER_ID` | high |
| [CL_QANSWER_QNR_PROGRESS](CL_QANSWER_QNR_PROGRESS.md) | `ANSWER_ID` | high |
| [CL_QANSWER_VERIFY](CL_QANSWER_VERIFY.md) | `ANSWER_ID` | high |
| [DTREE_CVG_CREATION_INFO](DTREE_CVG_CREATION_INFO.md) | `ANSWER_ID` | high |
| [DTREE_NODE_ORDERS](DTREE_NODE_ORDERS.md) | `ANSWER_ID` | high |
| [ENROLL_QUESR](ENROLL_QUESR.md) | `ANSWER_ID` | high |
| [FLAGGED_QUESTIONS](FLAGGED_QUESTIONS.md) | `ANSWER_ID` | high |
| [HIST_Q_AND_A](HIST_Q_AND_A.md) | `ANSWER_ID` | high |
| [IDENTITY_HQA_ID](IDENTITY_HQA_ID.md) | `ANSWER_ID` | high |
| [IDENTITY_HQA_ID_HX](IDENTITY_HQA_ID_HX.md) | `ANSWER_ID` | high |
| [OR_LOG_QUEST_ANS](OR_LOG_QUEST_ANS.md) | `ANSWER_ID` | high |
| [OR_LOG_QUEST_AN_P](OR_LOG_QUEST_AN_P.md) | `ANSWER_ID` | high |
| [QUESR_PREV_RESP_INFO](QUESR_PREV_RESP_INFO.md) | `ANSWER_ID` | high |
| [RECENT_PAT_COMP_DTREES](RECENT_PAT_COMP_DTREES.md) | `ANSWER_ID` | high |
| [SERIES_ANSWER_ID](SERIES_ANSWER_ID.md) | `ANSWER_ID` | high |
| [ST_QUES_VERIFICATION_INFO](ST_QUES_VERIFICATION_INFO.md) | `ANSWER_ID` | high |
| [V_EHI_HQA_QUEST_ANSWER](V_EHI_HQA_QUEST_ANSWER.md) | `ANSWER_ID` | high |

