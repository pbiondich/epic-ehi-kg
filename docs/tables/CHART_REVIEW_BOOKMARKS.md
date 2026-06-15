# CHART_REVIEW_BOOKMARKS

> This table contains bookmarked content.

**Primary key:** `BOOKMARK_LIST_ID`, `LINE`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BOOKMARK_LIST_ID` | NUMERIC | PK | The unique identifier for the bookmark list record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CMT` | VARCHAR |  | The user-entered comment for each bookmark. |
| 4 | `ENC_CSN` | NUMERIC |  | The contact serial number (CSN) for each bookmarked encounter. |
| 5 | `LETTER_LN` | INTEGER |  | The line number in the item for letter status for each bookmarked letter record. |
| 6 | `NOTE_ID` | VARCHAR | shared | The note identification number for every bookmarked note. |
| 7 | `ORDER_ID` | NUMERIC | shared | The order identification number for each bookmarked order. |
| 8 | `COMPONENT_IDX` | INTEGER |  | The index of each bookmarked result component. |
| 9 | `DOC_INFO_ID` | VARCHAR | FK→ | The document identification number for every bookmarked piece of media. |
| 10 | `EPISODE_ID` | NUMERIC | FK→ | The episode identification number for every bookmarked episode. |
| 11 | `LDA_ID` | VARCHAR |  | The LDA identification number for each bookmarked LDA (Lines, Drains, and Airways) record. |
| 12 | `REFERRAL_ID` | NUMERIC | FK→ | The referral ID for every bookmarked referral. |
| 13 | `ADDED_UTC_DTTM` | DATETIME (UTC) |  | The instant at which an item was bookmarked. |
| 14 | `OUTSIDE_ENC` | VARCHAR |  | The base Care Everywhere reference ID of each outside encounter that has been bookmarked. |
| 15 | `OUTSIDE_NOTE_LOCAL_IDENT` | VARCHAR |  | The locally-assigned unique identifier of the bookmarked external note. |
| 16 | `OUTSIDE_NOTE_DOCUMENT_CSN_ID` | NUMERIC |  | The ID of the bookmarked note's source DXR contact. |
| 17 | `OUTSIDE_EPISODE_IDENT` | VARCHAR |  | The episode ID of the bookmarked external episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DOC_INFO_ID` | [DOC_INFORMATION](DOC_INFORMATION.md) | sole_pk | high |
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

