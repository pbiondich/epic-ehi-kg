# CASE_SAVINGS

> The CASE_SAVINGS table contains information about savings associated with case records, such as the amount, type of savings, and reason for savings.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SAVINGS_AMOUNT` | NUMERIC |  | Specifies the savings amount. |
| 4 | `SAVINGS_TYPE_C_NAME` | VARCHAR | org | Specifies the savings type. |
| 5 | `SAVINGS_REASON` | VARCHAR |  | Specifies the savings reason. |
| 6 | `SAVINGS_USER_ID` | VARCHAR |  | The unique ID of the savings user. |
| 7 | `SAVINGS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `SAVINGS_DATE` | DATETIME |  | Specifies the savings date. |
| 9 | `SAVINGS_REVERSAL_LINE` | INTEGER |  | Holds the line number of the savings-related group that this line is a reversal of. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

