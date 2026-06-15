# CANCER_PROB_MERGE_HISTORY

> This table stores a list of changes to the problem specified in the PROBLEM_LIST_ID column that happened during a problem merge.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MERGE_INTO_PROBLEM_LIST_ID` | NUMERIC |  | This is the LPL ID of the problem that was merged into. |
| 4 | `MERGE_INTO_HISTORY_LINE` | INTEGER |  | This is the line number of the problem history related group (SI LPL 1100) for the problem that was merged into. |
| 5 | `MERGE_FROM_PROBLEM_LIST_ID` | NUMERIC |  | This is the LPL ID of the problem that this piece of data came from during a merge. |
| 6 | `IS_ADDED_DATA_YN` | VARCHAR |  | This stores whether this related line represents added data. Yes means the data was added, otherwise the data was removed. |
| 7 | `MERGED_LINKED_EPISODE_ID` | NUMERIC |  | This stores a linked episode (HSB) ID that was added or removed during a problem merge. |
| 8 | `MERGED_ONC_HISTORY_EVENT_LINE` | INTEGER |  | This stores an oncology history event line number that was added or removed during a problem merge. |
| 9 | `MERGED_LINKED_STAGE_ID` | NUMERIC |  | This stores an active cancer stage (STG) ID that was added to or removed from a problem during a merge. |
| 10 | `MERGED_DELETED_STAGE_ID` | NUMERIC |  | This stores a deleted cancer stage (STG) ID that was added to or removed from a problem during a merge. |
| 11 | `MERGED_TREAT_SUMMARY_NOTE_ID` | VARCHAR |  | This stores an active treatment summary HNO ID that was added to or removed from a problem during a merge. |
| 12 | `MERGED_DEL_TREAT_SUM_NOTE_ID` | VARCHAR |  | This stores a deleted treatment summary HNO ID that was added to or removed from a problem during a merge. |
| 13 | `LOCAL_RECUR_PROBLEM_LIST_ID` | NUMERIC |  | This stores a local recurrence problem ID that was added to or removed from a cancer problem during a merge. |
| 14 | `DISTANT_METS_PROBLEM_LIST_ID` | NUMERIC |  | This stores a distant metastasis problem ID that was added to or removed from a cancer problem during a merge. |
| 15 | `MERGED_DISEASE_STATUS_LINE` | INTEGER |  | This stores a disease status line number that was added to or removed from a cancer problem during a merge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

