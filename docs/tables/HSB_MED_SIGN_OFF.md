# HSB_MED_SIGN_OFF

> Contains information about the users involved in medication sign off workflows, the actions they took, and when it occurred.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the Episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AN_MED_REVIEWER_ID` | VARCHAR |  | Contains the ID of the user who was involved in the medication review process. |
| 4 | `AN_MED_REVIEWER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `MED_REVIEW_STATUS_C_NAME` | VARCHAR |  | Stores the current status of the medication review. |
| 6 | `STATUS_UPDATED_DTTM` | DATETIME (UTC) |  | Stores the instant that the status was last updated. |
| 7 | `MED_RVW_MSG_ID` | VARCHAR |  | This column contains the message ID for the message that was sent for medication sign off. |
| 8 | `MED_RVW_DEV_C_NAME` | VARCHAR | org | Stores the device used when the user signed off on the medications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

