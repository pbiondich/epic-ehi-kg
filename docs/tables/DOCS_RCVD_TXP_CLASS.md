# DOCS_RCVD_TXP_CLASS

> Cosmos discrete data related to organ class of transplant episodes.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TXP_CLASS_REF_IDENT` | VARCHAR |  | unique id corresponding to a transplant episode in SI DXR 11700 and a specific organ class |
| 2 | `TXP_EPISODE_REF_IDENT` | VARCHAR |  | episode id corresponding to a transplant episode in SI DXR 11700 |
| 3 | `TXP_ORGAN_CLASS_C_NAME` | VARCHAR |  | A type of organ class being transplanted in an episode |
| 4 | `TXP_PRIMARY_FAIL_REASON_C_NAME` | VARCHAR | org | The primary reason a patient's native or retransplant organ failed. |
| 5 | `TXP_OTHER_FAIL_REASON_ONE_C_NAME` | VARCHAR |  | First additional reason for a patient's native or retransplant organ failure. |
| 6 | `TXP_OTHER_FAIL_REASON_TWO_C_NAME` | VARCHAR |  | Second additional reason for a patient's native or retransplant organ failure. |
| 7 | `TXP_OTHER_FAIL_REASON_THREE_C_NAME` | VARCHAR |  | Third additional reason for a patient's native or retransplant organ failure. |
| 8 | `TXP_OTHER_FAIL_REASON_FOUR_C_NAME` | VARCHAR |  | Fourth additional reason for a patient's native or retransplant organ failure. |
| 9 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 10 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 11 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

