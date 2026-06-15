# PT_TREATMENT_DATE_AUDIT

> This table contains audit trail information for occurrence code 35 - the date physical therapy treatment started.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PT_TREATMENT_HX_DATE` | DATETIME |  | This audit trail item stores past values of the date physical therapy (PT) treatment started. |
| 4 | `PT_TREATMENT_DATE_USER_ID` | VARCHAR |  | This audit trail item stores users who changed the value of the date physical therapy (PT) treatment started. |
| 5 | `PT_TREATMENT_DATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `PT_TREATMENT_DATE_UTC_DTTM` | DATETIME (UTC) |  | This audit trail item stores the instant users changed the value of the date physical therapy (PT) treatment started. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

