# HH_EPSD_AUTH_INFO

> This table contains Home Health episode-level information entered in the Authorization Information table in the Financial and Authorization Information form in Intake.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTHORIZATION_NUM` | VARCHAR |  | Authorization number. |
| 4 | `AUTHORIZATION_CMT` | VARCHAR |  | Authorization comment text entered by a user. |
| 5 | `AUTH_BY_ID` | VARCHAR |  | This column stores the identifier for the user who entered the authorization information. The column links to the table CLARITY_EMP. |
| 6 | `AUTH_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `AUTHORIZATION_DATE` | DATETIME |  | Authorization date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

