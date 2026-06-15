# OR_CASE_LAST_MINUTE_CANC

> Table enables you to report on the last minute case cancellations data.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CANCEL_DT` | DATETIME |  | Stores the cancellation date when the case is canceled at the last minute (i.e., on the day of surgery or on the day of admission). |
| 4 | `CANCEL_TM` | DATETIME (Local) |  | Stores the cancellation time when the case is canceled at the last minute (i.e., on the day of surgery or on the day of admission). |
| 5 | `CANCEL_REASON_C_NAME` | VARCHAR | org | Stores the reason for canceling the case at the last minute (i.e., on the day of surgery or on the day of admission). |
| 6 | `SCHEDULED_SURGERY_DT` | DATETIME |  | Stores the scheduled surgery date when the case is canceled at the last minute (i.e., on the day of surgery or on the day of admission). |
| 7 | `SCHEDULED_SURGERY_TM` | DATETIME (Local) |  | Stores the scheduled surgery time when the case is canceled at the last minute (i.e., on the day of surgery or on the day of admission). |
| 8 | `CANCEL_LOG_ID` | VARCHAR |  | This item stores the log associated with the last minute cancellation entry. The presence of this item indicates that the procedure was canceled after the log was created but the case was not moved to a status of canceled. The cancel reason used to determine if the cancellation is non-clinical will be determined by the mapping of Procedure Not Performed reason (ORL 7802) to Case Cancel reasons. |
| 9 | `IS_REASON_EDITED_YN` | VARCHAR |  | This item stores if the cancel reason was edited via the Edit Last Minute Cancellations activity. For cancellations originating from logs that are marked Procedure Not Performed without canceling the case, once this is set, updates to the Procedure Not Performed Reason in I ORL 7802 will no longer update the reason here. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

