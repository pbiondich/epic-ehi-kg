# RXA_OTH_PAY_PD

> This table extracts the related multiple-response Other Payer Amount Paid (I RXA 3610) item.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of the associated other payer amount paid in the adjudication's record. Together with adjudication RECORD_ID, this forms the foreign key to the RXA_OTH_PAY_PD table. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple other payer amounts paid associated with the adjudication from the RXA_OTH_PAY_PD table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `O_OTH_PAY_AMT_PAID` | NUMERIC |  | The amount of any payment from other sources that is known by the pharmacy. |
| 7 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

