# DOCS_RCVD_SURG_HX

> This table contains surgical history information.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SURG_HX_REF_ID` | VARCHAR |  | This item stores the unique reference identifier associated with the surgical history. |
| 6 | `SURG_HX_NAME` | VARCHAR |  | This item stores the free text name for the surgical history procedure. |
| 7 | `SURG_HX_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 8 | `SURG_HX_START_DATE` | DATETIME |  | This item stores the start date of the surgical history. |
| 9 | `SURG_HX_END_DATE` | DATETIME |  | This item stores the end date of the surgical history. |
| 10 | `SURG_HX_FREE_TXT_DT` | VARCHAR |  | This item stores the free text date of the surgical history. |
| 11 | `SRG_HX_LATERALITY_C_NAME` | VARCHAR | org | This item stores the laterality of the surgical history. |
| 12 | `SURG_HX_COMMENT` | VARCHAR |  | This item stores the comments of the surgical history. |
| 13 | `SURG_HX_SRC_DXR_CSN` | NUMERIC |  | This item stores the contact serial number (CSN) of the Document Received record that owns the instance of this surgical history. |
| 14 | `SURGHX_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the surgical history in UTC. |
| 15 | `SURG_HX_PAT_HX_RESP_C_NAME` | VARCHAR |  | The patient response for the surgical history question. |
| 16 | `SURG_HX_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 17 | `SURG_HX_TEMPLATE_ID` | VARCHAR |  | The unique ID of the history template associated with the surgical history. |
| 18 | `SURG_HX_TEMPLATE_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

