# PR_EST_CNCT_ADDR

> Address information when a non-patient has requested a price estimate. This table must be used in conjunction with PR_EST_INFO to get the full contact information.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the price estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDRESS` | VARCHAR |  | The street and house number information for the contact person's address. Use the PR_EST_INFO table to retrieve the rest of the contact information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

