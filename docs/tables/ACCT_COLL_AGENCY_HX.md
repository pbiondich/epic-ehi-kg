# ACCT_COLL_AGENCY_HX

> This table contains historical collection agency information associated with the guarantor account.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AGENCY_ID` | NUMERIC | FK→ | The collection agency that this account was assigned to. |
| 4 | `AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 5 | `SUBMIT_DATE` | DATETIME |  | The date the account was assigned to the collection agency. |
| 6 | `RESOLVED_DATE` | DATETIME |  | The date the account was resolved by the collection agency. |
| 7 | `RESOLUTION_TYPE_C_NAME` | VARCHAR |  | The type of resolution that occurred for this history line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `AGENCY_ID` | [CLARITY_AGENCY](CLARITY_AGENCY.md) | sole_pk | high |

