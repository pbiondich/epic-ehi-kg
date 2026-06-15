# ORDER_REVIEW

> This table contains a list of all the users that have reviewed the order and whether that review was accepted or not.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table is determined by the number of users who reviewed this order. |
| 3 | `REVIEW_USER_ID` | VARCHAR |  | The user that reviewed the order. |
| 4 | `REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REVIEWED_TIME` | DATETIME (UTC) |  | The date and time when the order was reviewed. |
| 6 | `REVIEW_ACCEPTED_YN` | VARCHAR |  | This column contains Y/N to determine if the reviewer accepted the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

