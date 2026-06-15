# HSPC_HIS_COMP_QUESN_INST

> This table extracts the related multiple response Hospice Item Set - Z0400 Questions Completed Inst (I LHO 912) item, which is the instant that the Hospice Item Set question was completed or updated.

**Primary key:** `DATASET_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DATASET_ID` | NUMERIC | PK shared | The unique identifier for the data set record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `QUESTION_COMP_INST_DTTM` | DATETIME (UTC) |  | This column displays the instant that a Hospice Item Set (HIS) question was completed or updated. This correlates directly to item Z0400 on the HIS. Item Z0400 indicates who actually answered the question. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

