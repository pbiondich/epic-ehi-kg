# RXA_BEN_STAGE_AMT

> This table extracts the related multiple-response Benefit Stage Amount (I RXA 3635) item.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of the associated 'Benefit Stage Amount' in the adjudication's record. Together with adjudication RECORD_ID, this forms the foreign key to the RXA_BEN_STAGE_AMT table. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple 'Benefit Stage Amount' associated with the adjudication from the RXA_BEN_STAGE_AMT table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `O_BEN_STAGE_AMT` | NUMERIC |  | The amount of claim allocated to the Medicare stage identified by the 'Benefit Stage Qualifier' (393-MV). |
| 7 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

