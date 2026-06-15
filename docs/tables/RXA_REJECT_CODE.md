# RXA_REJECT_CODE

> Stores reject codes for adjudication records. Reject codes may be used when an adjudication fails, for example, due to missing prior authorization. Adjudication records are used by Ambulatory Pharmacy during prescription copay adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `REJECT_CODE_ID` | NUMERIC |  | NCPDP code indicating the error encountered using a record from the flag master file. |
| 7 | `REJECT_CODE_ID_RECORD_NAME` | VARCHAR |  | The flag name. |
| 8 | `REJECT_FIELD_OCCUR` | INTEGER |  | Code indicating the error encountered. |
| 9 | `RJCT_CODE_FREE_TXT` | VARCHAR |  | A free-text description of the reject code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

