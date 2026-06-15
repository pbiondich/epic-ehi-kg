# WKQUEUE_REVIEW

> This is the clarity table for Infection Control Workqueue functionality. It contains the review information for a result.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WKQUEUE_TYPE_C_NAME` | VARCHAR | org | This stores user group of a workqueue. This is meant to be used in conjunction with the Workqueue Type parameter from Reporting Workbench reports from the Infection Control Find Results template. |
| 4 | `WKQUEUE_REVIEW_TIME_DTTM` | DATETIME (UTC) |  | This stores the review instant for a result. This is the time at which a user clicked the "Reviewed" button from a Reporting Workbench Workqueue. Each instant is specific to the Workqueue Type and User ID. |
| 5 | `WKQUEUE_REV_USER_ID` | VARCHAR |  | The reviewer for a result. This is related to the review instant and the workqueue type. |
| 6 | `WKQUEUE_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `WKQUEUE_REVIEW_C_NAME` | VARCHAR | org | This stores the review action for a result. This is the action a user took from a Reporting Workbench Workqueue. |
| 8 | `WKQUEUE_REASON_C_NAME` | VARCHAR | org | This stores a result review reason. This is the discrete reason a user documented while reviewing the result. Each reason is specific to a workqueue and user ID. |
| 9 | `WKQUEUE_COMMENT` | VARCHAR |  | This column stores the free text result review comment. This is the comment a user documented while reviewing the result. Each comment is specific to a workqueue and user ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

