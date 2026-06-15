# OPH_IPROC_INFO

> This table stores results data for the questions (LQL) configured for use with the Imaging and Procedures visit navigator section.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | This column stores the unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IPROC_QUEST_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `IPROC_PROMPT` | VARCHAR |  | Stores the prompt for multiple response imaging or procedure result form questions. |
| 5 | `IPROC_COMMENT` | VARCHAR |  | Stores the comment related to an imaging or procedure result finding. |
| 6 | `IPROC_USER_ID` | VARCHAR |  | Stores the user who entered the most recent imaging or procedure result information. |
| 7 | `IPROC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `IPROC_UPDATED_INST_DTTM` | DATETIME (Local) |  | Stores the instant of entry for the most recent imaging or procedure result information. |
| 9 | `IPROC_LATERALITY_C_NAME` | VARCHAR |  | Stores the laterality for the imaging or procedure result information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

