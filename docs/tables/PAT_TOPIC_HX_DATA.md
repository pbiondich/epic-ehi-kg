# PAT_TOPIC_HX_DATA

> History of edits to patient topic data.

**Primary key:** `AGENDA_TOPIC_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AGENDA_TOPIC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit agenda topic record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WPR_IDENT` | INTEGER |  | Indicates the user involved with the given edit to patient topic data. |
| 4 | `AGENDA_CODEASSIST_C_NAME` | NUMERIC |  | Indicates the code/workflow involved with the given edit to patient topic data. |
| 5 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | Time as a UTC instant for the given edit to patient topic data. |
| 6 | `TITLE_CHANGED_YN` | VARCHAR |  | Indicates whether a missing PREVIOUS_TITLE value means "no change" or that it was previously null |
| 7 | `PREVIOUS_TITLE` | VARCHAR |  | State of the patient title of the topic before the given edit. |
| 8 | `DESCRIPTION_CHANGED_YN` | VARCHAR |  | Indicates whether a missing PREVIOUS_DESCRIPTION value means "no change" or that it was previously null. |
| 9 | `PREVIOUS_DESCRIPTION` | VARCHAR |  | State of the patient description of the topic before the given edit. |
| 10 | `PRIMARY_PAT_TOPIC_CHANGED_YN` | VARCHAR |  | Indicates whether a missing PREVIOUS_PRIMARY_PAT_TOPIC_YN value means "no change" or that it was previously null. |
| 11 | `PREVIOUS_PRIMARY_PAT_TOPIC_YN` | VARCHAR |  | Was this topic the primary patient topic before the given edit? |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AGENDA_TOPIC_ID` | [AGENDA_TOPIC_INFO](AGENDA_TOPIC_INFO.md) | sole_pk | high |

