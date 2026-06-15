# CRITERIA_REVIEW

> This table contains information about medical necessity criteria reviews. The records included in this table are Criteria Review Records (CRR) records storing items that a case manager would enter in the Utilization Review activity or during a criteria review completed in Tapestry. For example, this includes the review outcome, guideline days, and the time and date the review was completed.

**Primary key:** `CRITERIA_REVIEW_ID`  
**Columns:** 50  
**Org-specific columns:** 5  
**Joined by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CRITERIA_REVIEW_ID` | NUMERIC | PK | The unique ID of the criteria review record. |
| 2 | `CRITERIA_REV_NAME` | VARCHAR |  | The name of the criteria review record. |
| 3 | `PATIENT_ID` | VARCHAR |  | Stores the patient the criteria review is for. |
| 4 | `OBJECT_TYPE_C_NAME` | VARCHAR |  | The type of record the criteria review is for. |
| 5 | `REFERRAL_ID` | NUMERIC | FK→ | The ID of the referral that is associated with the criteria review. |
| 6 | `REVIEW_ID` | VARCHAR | FK→ | The review ID associated with the criteria review. |
| 7 | `REVIEW_NUMBER` | VARCHAR |  | The review number of the criteria review record. |
| 8 | `CRITERIA_SET_NAME` | VARCHAR |  | The criteria set name for this criteria record. |
| 9 | `CRITERIA_STATUS_C_NAME` | VARCHAR |  | The status of the criteria review. |
| 10 | `SERVICE_DATE` | DATETIME |  | The service date associated with this criteria review record. |
| 11 | `PROVIDER_ID` | VARCHAR |  | The unique ID of the provider associated with the criteria review. |
| 12 | `PROVIDER_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 13 | `NOTE_ID` | VARCHAR | shared | The unique ID of any notes associated with this criteria review. |
| 14 | `REVIEW_STATUS_C_NAME` | VARCHAR |  | Review status for criteria using CERMe (third-party software from McKesson used for utilization review). |
| 15 | `PATIENT_CSN` | NUMERIC |  | Stores the Patient Contact Serial Number for the encounter in which the review was created. |
| 16 | `REV_TYPE_C_NAME` | VARCHAR | org | Stores the type of review that is performed - Admission, Concurrent, Discharge, etc. |
| 17 | `ADDITIONAL_NOTES_ID` | VARCHAR |  | Stores additional comments or notes related to the review. |
| 18 | `REVIEW_INSTANT_DTTM` | DATETIME (UTC) |  | Stores the instant the review was filed. |
| 19 | `CONTENT_SOURCE_C_NAME` | VARCHAR | org | The content provider used for this review. |
| 20 | `REVIEW_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 21 | `REVIEW_PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 22 | `CRITERIA_OUTCOME_C_NAME` | VARCHAR | org | Final determination of the review. |
| 23 | `PARENT_REVIEW_ID` | NUMERIC |  | Points to the parent criteria review that generated this review. |
| 24 | `REV_DAY_TYPE_C_NAME` | VARCHAR | org | Stores the type of day for this review. |
| 25 | `REVIEW_DAY` | INTEGER |  | Stores the numeric day of the review. |
| 26 | `GUIDELINE_DAY` | INTEGER |  | Stores the current Guideline Day for an MCG Optimal Recovery Course. |
| 27 | `COMP_INST_UTC_DTTM` | DATETIME (UTC) |  | The time and date a utilization review was marked complete. |
| 28 | `COMP_USER_ID` | VARCHAR |  | The user who marked a utilization review as complete. |
| 29 | `COMP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `REVIEW_SELECTED_YN` | VARCHAR |  | This row indicates whether a patient status associated with a review is the status selected by the user. Selection is relevant for reviews in which the user can check off criteria for more than one patient status such as observation or inpatient, but for which the user must select one target patient status to file the review. If the patient status associated with the review is the selected status, this item is set to Yes. If the patient status associated with a review is not the status selected by the user, it is set to No. If this item is empty, then the review does not have an associated patient status that is either selected or not selected. |
| 31 | `CREATION_REVIEWER_USER_ID` | VARCHAR |  | The reviewer who first created this review. |
| 32 | `CREATION_REVIEWER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 33 | `CREATION_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant at which this review was created. |
| 34 | `OVERALL_DETERMINATION` | VARCHAR |  | Textual representation of the overall determination of a review. |
| 35 | `REVIEW_VENDOR_C_NAME` | VARCHAR | org | This item stores which criteria review vendor created the review. |
| 36 | `AUTH_REQUEST_STATUS` | VARCHAR |  | Authorization request status from a third party criteria review vendor. |
| 37 | `AUTH_REQUEST_ID` | NUMERIC | FK→ | The authorization request associated with the guideline review. |
| 38 | `CREATION_AUTH_REQUEST_CSN_ID` | NUMERIC |  | The authorization request contact associated with the creation of this criteria review record. |
| 39 | `RECENT_AUTH_REQUEST_CSN_ID` | NUMERIC |  | The authorization request contact associated with the most recent data in this criteria review record. |
| 40 | `GUIDELINE_TYPE_C_NAME` | VARCHAR |  | The type of guideline review. Internal Guideline Review [1] means that the guideline review was created for an internal guideline (GLD). |
| 41 | `AI_ANSWER_ID` | VARCHAR |  | AI-generated questionnaire answers associated with guideline review |
| 42 | `VENDOR_AGENCY_ID` | VARCHAR |  | The guideline review vendor that created the review as a unique record ID instead of a category. |
| 43 | `VENDOR_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 44 | `ASSOCIATED_DATES_FROM_DATE` | DATETIME |  | If the review is associated with dates of a patient's stay, this is the beginning of the date range. |
| 45 | `ASSOCIATED_DATES_TO_DATE` | DATETIME |  | If the review is associated with dates of a patient's stay, this is the end of the date range. |
| 46 | `UPDATE_INST_LOCAL_DTTM` | DATETIME (Attached) |  | Stores the instant the review was last updated in the local (patient encounter) time zone. |
| 47 | `DAYS_OF_CARE_START` | INTEGER |  | For a progression plan review, this item is the numeric representation of the first day this review covers of the patient's stay, with the day the progression plan began considered day 1. |
| 48 | `DAYS_OF_CARE_END` | INTEGER |  | For a progression plan review, this item is the numeric representation of the last day this review covers of the patient's stay, with the day the progression plan began considered day 1. |
| 49 | `DAYS_OF_PROGRESSION_PLAN_START` | INTEGER |  | For a progression plan review, this item is the numeric representation of the first day in the progression plan this review covers. |
| 50 | `DAYS_OF_PROGRESSION_PLAN_END` | INTEGER |  | For a progression plan review, this item is the numeric representation of the last day in the progression plan this review covers. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |
| `REVIEW_ID` | [SECOND_LEVEL_REVIEWS](SECOND_LEVEL_REVIEWS.md) | sole_pk | high |

## Joined in — referenced by (6)

| From | Column | Confidence |
|------|--------|------------|
| [CRITERIA_REVIEW_DTR_REQS](CRITERIA_REVIEW_DTR_REQS.md) | `CRITERIA_REVIEW_ID` | high |
| [CRITERIA_REVIEW_GEN_TRACK](CRITERIA_REVIEW_GEN_TRACK.md) | `CRITERIA_REVIEW_ID` | high |
| [CRITERIA_REVIEW_HX](CRITERIA_REVIEW_HX.md) | `CRITERIA_REVIEW_ID` | high |
| [CRITERIA_REVIEW_SVC_AUTHS](CRITERIA_REVIEW_SVC_AUTHS.md) | `CRITERIA_REVIEW_ID` | high |
| [CRITERIA_REVIEW_TRACK](CRITERIA_REVIEW_TRACK.md) | `CRITERIA_REVIEW_ID` | high |
| [CRITERIA_REV_CNCT](CRITERIA_REV_CNCT.md) | `CRITERIA_REVIEW_ID` | high |

