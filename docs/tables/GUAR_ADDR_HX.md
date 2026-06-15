# GUAR_ADDR_HX

> This table holds the Accounts Receivable (EAR) related group 5000 pertaining to Guarantor Address Change History.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDR_CHANGE_DATE` | DATETIME |  | This column specifies the date on which the address change described on the rest of the row was performed. |
| 4 | `ADDR_HX_1` | VARCHAR |  | This column contains the first line of a previous guarantor address. |
| 5 | `ADDR_HX_2` | VARCHAR |  | This column contains the second line of a previous guarantor address. |
| 6 | `ADDR_HX_EXTRA` | VARCHAR |  | This contains any additional lines for a previous guarantor address. |
| 7 | `CITY_HX` | VARCHAR |  | This column contains the city for a previous address for this guarantor. |
| 8 | `STATE_HX_C_NAME` | VARCHAR | org | This column contains the state for a previous address for this guarantor. |
| 9 | `ZIP_HX` | VARCHAR |  | This column contains the ZIP code for a previous address for this guarantor. |
| 10 | `ADDR_CHANGE_SRC_C_NAME` | VARCHAR |  | This column contains the context from which the address change was performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

