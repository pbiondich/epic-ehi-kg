# LAB_CASE_QA

> This table contains the selected case's quality assurance information.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAB_CASE_QA_EVENT_C_NAME` | VARCHAR | org | This will store the QA (Quality Assurance) event type for the case. |
| 4 | `LAB_CASE_QA_CASE_ID` | NUMERIC |  | The unique identifier of the correlated case record. |
| 5 | `LAB_CASE_QA_SPEC_ID` | VARCHAR |  | The unique identifier of the correlated specimen record. |
| 6 | `LAB_AP_REVIEWER_ID` | VARCHAR |  | The unique identifier of the user who is the reviewer of a related QA (Quality Assurance) event. |
| 7 | `LAB_AP_REVIEWER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `LAB_AP_REVIEW_DATE` | DATETIME |  | Stores the review date of a related QA (Quality Assurance) event. |
| 9 | `LAB_AP_QA_STATUS_C_NAME` | VARCHAR |  | The status category number for the related QA (Quality Assurance) event. |
| 10 | `LAB_CASE_QA_ORD_ID` | NUMERIC |  | The unique identifier of the correlated order record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

