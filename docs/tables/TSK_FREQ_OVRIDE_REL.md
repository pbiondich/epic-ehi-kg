# TSK_FREQ_OVRIDE_REL

> Frequency override related days and times.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EFQ_OVRIDE_REL_DAYS` | INTEGER |  | Contains a list of days that are used to override the frequency specified for the order along with the times in LTK-34656. |
| 4 | `EFQ_OVRIDE_REL_TM` | DATETIME (Local) |  | Contains a set of times related to the days in LTK-34655 used to override the frequency the order was placed with. |
| 5 | `EFQ_OVRIDE_REL_ZC_TM_OF_DAY_C_NAME` | NUMERIC | org | Contains a list of reminder time buckets related to the days in LTK-34655 used to override and/or specify the frequency associated with the task. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

