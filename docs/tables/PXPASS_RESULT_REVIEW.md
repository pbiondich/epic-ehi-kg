# PXPASS_RESULT_REVIEW

> This table contains information about users who reviewed results in the system and indicated that their review was relevant to a particular Procedure Pass.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID of the Procedure Pass record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVIEW_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 4 | `REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REVIEW_ORDER_ID` | NUMERIC |  | The unique ID of the order whose result was reviewed by a user who indicated that their review was specific to this Procedure Pass |
| 6 | `REVIEW_ORD_DAT` | NUMERIC |  | Stores the order contact for a result that was reviewed by a user who indicated that their review was specific to this Procedure Pass |
| 7 | `PXPASS_REVIEW_RSN_C_NAME` | VARCHAR | org | Stores the reason that a result was reviewed. |
| 8 | `REVIEW_COMMENT` | VARCHAR |  | Stores the comment associated with a result review. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

