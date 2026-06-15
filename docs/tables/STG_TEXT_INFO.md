# STG_TEXT_INFO

> This table contains textual information about a cancer stage (STG) record, such as the staging comments, prognostic indicators, and free text stage.

**Primary key:** `STAGE_ID`, `CONTACT_DATE_REAL`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STAGE_ID` | NUMERIC | PK shared | The cancer stage (STG) row ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `LB_FREE_TEXT_STAGE` | VARCHAR |  | Stores general free text staging information. |
| 6 | `CLIN_FREE_TEXT_STG` | VARCHAR |  | Stores the clinical free text stage for a cancer diagnosis. |
| 7 | `PATH_FREE_TEXT_STG` | VARCHAR |  | Stores the pathologic free text stage for a cancer diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

