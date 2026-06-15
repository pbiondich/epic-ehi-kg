# CDI_STAT_HX

> This table contains information about the status and assigned user change history for the Clinical Documentation Improvement (CDI) reviews in a hospital account.

**Primary key:** `CODING_RECORD_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier of the coding record associated with the hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this account. Each line represents a change in clinical documentation improvement (CDI) status or assigned user. |
| 3 | `CDI_HX_ASGN_USER_ID` | VARCHAR |  | This item stores what the clinical documentation improvement (CDI) assigned user is changed to for this account. |
| 4 | `CDI_HX_ASGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CDI_HX_STAT_C_NAME` | VARCHAR | org | This item stores the clinical documentation improvement (CDI) status changes for this account. |
| 6 | `CDI_HX_CHNG_USER_ID` | VARCHAR |  | This item stores the user who makes the change of clinical documentation improvement (CDI) assigned user or status for this account. |
| 7 | `CDI_HX_CHNG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CDI_HX_CHNG_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant when the clinical documentation improvement (CDI) status or assigned user was changed based on the UTC timezone. Data retrieval should generally occur by using the column CDI_HX_CHG_DTTM, which will return the change instant in local time. |
| 9 | `CDI_HX_CHNG_DTTM` | DATETIME (Local) |  | This item shows the instant when the clinical documentation improvement (CDI) status or assigned user was changed based on the system local timezone. |
| 10 | `CDI_HX_CHNG_CMT` | VARCHAR |  | The comment associated with the status change in the clinical documentation improvement (CDI) status history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

