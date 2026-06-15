# PATHWAY_REVIEWED

> Each row in this table contains information related to a user marking a pathway as reviewed in the pathway review activity.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the pathway record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVIEWED_BY_USER_ID` | VARCHAR |  | The unique ID associated with the user who marked the pathway as reviewed. This column is frequently used to link to the CLARITY_EMP table. |
| 4 | `REVIEWED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REVIEWED_AT_DTTM` | DATETIME (UTC) |  | The instant when the pathway was marked as reviewed. |
| 6 | `REVIEWED_COMMENT` | VARCHAR |  | An optional comment that can be entered when marking a pathway as reviewed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

