# DOCS_RCVD_MEDICAL_HX

> This table contains information about patients' medical history.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MED_HX_REF` | VARCHAR |  | The unique reference identifier associated with the medical history. |
| 6 | `MED_HX_FREE_TXT_DT` | VARCHAR |  | The free text date for this medical history. |
| 7 | `MED_HX_COMMENT` | VARCHAR |  | The comments for the medical history. |
| 8 | `MED_HX_SRC_DXR_DOCUMENT_CSN_ID` | NUMERIC |  | The contact serial number of the received document record that owns the instance of this medical history. |
| 9 | `MED_HX_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | The last update instant of the medical history in UTC. |
| 10 | `MED_HX_PAT_HX_RESP_C_NAME` | VARCHAR |  | The patient's response to the medical history question. |
| 11 | `MED_HX_SRC_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 12 | `MED_HX_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 13 | `MED_HX_TEMPLATE_ID` | VARCHAR |  | Stores the ID of the medical history questionnaire. |
| 14 | `MED_HX_TEMPLATE_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 15 | `MED_HX_NAME` | VARCHAR |  | This item stores the free text name for the medical history diagnosis. |
| 16 | `MED_HX_START_DATE` | DATETIME |  | This item stores the start date of the medical history. |
| 17 | `MED_HX_END_DATE` | DATETIME |  | This item stores the end date of the medical history. |
| 18 | `MED_HX_CREATED_DATE` | DATETIME |  | Date when the medical history diagnosis was added to the patient's chart. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

