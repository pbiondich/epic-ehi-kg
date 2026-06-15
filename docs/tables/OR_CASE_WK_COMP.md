# OR_CASE_WK_COMP

> This table contains information related to OR Case Worker's Comp claims.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMPANY_NAME` | VARCHAR |  | Company name of worker's comp. |
| 4 | `CLAIM_NUMBER` | VARCHAR |  | Claim number of worker's comp. |
| 5 | `ADJ_NAME` | VARCHAR |  | Adjuster name of worker's comp. |
| 6 | `ADJ_PHONE_NUMBER` | VARCHAR |  | Adjuster's phone number for worker's comp. |
| 7 | `INJURY_DATE` | DATETIME |  | Date of injury for worker's comp. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

