# DOCS_RCVD_ASMT_QUESTIONS

> Stores data related to discrete external assessment questions.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ASMNT_QUESTION_IDENTIFIER` | VARCHAR |  | This item stores the unique reference ID of a question asked as part of an assessment. |
| 6 | `ASMNT_QUESTION_ASMT_IDENTIFIER` | VARCHAR |  | This item stores the reference ID of the assessment a question is a part of. |
| 7 | `ASMNT_QUESTION_PROMPT` | VARCHAR |  | This item stores the prompt for a question asked as part of an assessment. |
| 8 | `ASMNT_QUESTION_ANSWER` | VARCHAR |  | This item stores the text of the answer to an assessment's question. |
| 9 | `ASMNT_QUESTION_BLKFL_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 10 | `ASMNT_QUESTION_BLKFL_INCL_DATE` | DATETIME |  | The date to compare to the data period window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |
| 11 | `ASMNT_QUESTION_FLO` | VARCHAR |  | This item stores the flowsheet ID for the associated assessment question. |
| 12 | `ASMNT_QUESTION_FLO_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 13 | `ASMNT_QUESTION_ANSWER_VAL` | VARCHAR |  | This item stores the mapped answer value that is associated with the answer to the question. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

