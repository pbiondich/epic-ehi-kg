# INFECTION_COMMENT_HISTORY

> History of the infection comment field.

**Primary key:** `INFECTION_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFECTION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the infection record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMMENT_HISTORY_TEXT` | VARCHAR |  | Previous iterations of the infection comment. |
| 4 | `COMMENT_HISTORY_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time the comment was set to the corresponding text. |
| 5 | `COMMENT_HISTORY_USER_ID` | VARCHAR |  | The unique ID associated with the user who set the comment to the corresponding text. This column is frequently used to link to the CLARITY_EMP table. |
| 6 | `COMMENT_HISTORY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFECTION_ID` | [INFECTIONS](INFECTIONS.md) | sole_pk | high |

