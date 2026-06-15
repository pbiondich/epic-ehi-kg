# RXA_ADD_DOC_QU_OUT

> Stores information about questions that pertain to prescriptions billed on the National Council for Prescription Drug Programs (NCPDP) interface.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `O_QUESN_NUM` | VARCHAR |  | Identifies the question number/letter that the question response applies to (part of the question information). |
| 6 | `O_QUESN_PERC_RESP` | NUMERIC |  | Percent response to a question (part of the question information). |
| 7 | `O_QUESN_RESP_DATE` | DATETIME |  | Date response to a question (part of the question information). |
| 8 | `O_QUESN_AMT_RESP` | NUMERIC |  | Dollar Amount response to a question (part of the question information). |
| 9 | `O_QUESN_NUM_RESP` | INTEGER |  | Numeric response to a question (part of the question information). |
| 10 | `O_QUESN_ALPHA_RESP` | VARCHAR |  | Alphanumeric response to a question (part of the question information). |
| 11 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

