# RXA_OTR_AMT_CL_OUT

> Provides more information about prescription fill costs claimed in Other Amount Claimed Submitted in prescription claims adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `O_OTH_AMT_CLM_QL_ID` | NUMERIC |  | NCPDP code identifying the additional incurred cost claimed in 'Other Amount Claimed Submitted' (480-H9). |
| 6 | `O_OTH_AMT_CLM_QL_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 7 | `O_OTH_AMT_CLAIMED` | NUMERIC |  | Amount representing the additional incurred costs for a dispensed prescription or service. |
| 8 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

