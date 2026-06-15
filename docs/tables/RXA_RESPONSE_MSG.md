# RXA_RESPONSE_MSG

> The response message received from the payor.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `I_ADDL_MSG_INFO_ID` | NUMERIC |  | NCPDP format qualifier of the Additional Message Information (526-FQ) that follows. Each value may occur only once per transaction and values must be ordered sequentially (numeric characters precede alpha characters, i.e., 0-9, A-Z). |
| 6 | `I_ADDL_MSG_INFO_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 7 | `I_ADDL_MSG_INFO` | VARCHAR |  | Free text message from the Additional Message Information field of the adjudication response. |
| 8 | `I_ADDL_MSG_INF_1_ID` | NUMERIC |  | Indicates continuity of the text found in the current repetition of Additional Message Information (526-FQ) with the text found in the next repetition that follows. |
| 9 | `I_ADDL_MSG_INF_1_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 10 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

