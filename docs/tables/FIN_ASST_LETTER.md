# FIN_ASST_LETTER

> This table contains information about letters sent as part of financial assistance workflows.

**Primary key:** `NOTE_ID`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LETTER_PRNT_MTHD_C_NAME` | VARCHAR |  | The purpose of this item is to provide additional context for I HNO 39 - Letter Print Instant. This item specifies whether the last print action for this letter was via the server or via the client. |
| 3 | `LETTER_PRNT_INSTANT_DTTM` | DATETIME (Attached) |  | Holds the instant the letter was last printed. |
| 4 | `LETTER_SENT_DT` | DATETIME |  | This item stores the date the letter was sent. |
| 5 | `ENTRY_PERSON_ID` | VARCHAR |  | Letter printing user's ID. |
| 6 | `ENTRY_PERSON_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `HB_LET_TEMPLT_ID` | VARCHAR |  | Stores the internal ID of the letter template used. |
| 8 | `HB_LET_TEMPLT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 9 | `HB_LTR_EXT_IMG_LINK` | VARCHAR |  | Stores the filename on the BLOB server for the image of the letter. |
| 10 | `HB_LTR_DVRY_MTD_C_NAME` | VARCHAR |  | This items stores how the letter was delivered, for example, by paper or electronic notification. |
| 11 | `HB_LTR_PAPER_RSN_C_NAME` | VARCHAR |  | Stores the reason the letter was forced to be sent by paper. |
| 12 | `FIN_ASST_CASE_ID` | NUMERIC | FK→ | This item stores the internal ID of the financial assistance case record this note is linked to. |
| 13 | `FIN_ASST_TRACKER_ID` | NUMERIC | FK→ | Stores the internal ID of the financial assistance program tracker linked to this note. |
| 14 | `REG_FA_LETTER_TYP_C_NAME` | VARCHAR |  | This item stores the type of letter being sent for a financial assistance case record. |
| 15 | `REG_FA_LTR_SRC_C_NAME` | VARCHAR |  | This item stores the source from which a letter has been generated for a financial assistance case record. |
| 16 | `HNO_RECORD_TYPE_C_NAME` | VARCHAR |  | Record type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

