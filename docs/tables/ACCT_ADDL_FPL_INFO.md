# ACCT_ADDL_FPL_INFO

> Stores additional income types and values that correspond with entries from the ACCOUNT_FPL_INFO table.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. It is used to differentiate records in this table, but is not meaningful. |
| 3 | `ADDL_INCOME_TYPE_C_NAME` | VARCHAR | org | Additional income type for the federal poverty level (FPL) table. This is a translated version of FPL Additional Income Type Combined (I EAR 144) storing the information as a discrete line instead of a delimited string. |
| 4 | `ADDL_INCOME_VALUE` | NUMERIC |  | Additional income amount for the federal poverty level (FPL) table. This is a translated version of FPL Additional Income Value Calculated (I EAR 145) storing the information as a discrete line instead of a delimited string. |
| 5 | `FPL_INFO_LINE` | INTEGER |  | Points to the line number ACCOUNT_FPL_INFO that this line is related to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

