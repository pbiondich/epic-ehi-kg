# CV_COMPLICATION_TRACKING

> This table contains rows for tracking surgical log complication elements.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ELEMENT_C_NAME` | VARCHAR | org | To keep track of procedure complication outcome. |
| 4 | `ELEMENT_TIME_C_NAME` | VARCHAR | org | Represents the phase of the procedure when the complication element occurred, such as intraproc or postop. |
| 5 | `ELEMENT_PRIORITY_C_NAME` | VARCHAR | org | To record the outcome of a complication element. |
| 6 | `ELEMENT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `ELEMENT_COMMENT` | VARCHAR |  | Stores the comment for the complication element. |
| 8 | `ELEMENT_STATUS_C_NAME` | VARCHAR |  | Indicates whether the complication element is active or inactive. |
| 9 | `ELEMENT_FOUND_DATE` | DATETIME |  | This item is used to define the date when a complication was first encountered. This is not the same as when it was first documented. |
| 10 | `ELEMENT_FOUND_TM` | DATETIME (Local) |  | This item is used to define the time when a complication was first encountered. This is not the same as when it was first documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

