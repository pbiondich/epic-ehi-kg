# HSP_PRE_AR_AUTH_ID

> This table contains the auth ID information for hospital billing temporary transactions. This table is limited to charge temporary transactions that have not yet been posted to the account.

**Primary key:** `HTT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HTT_ID` | NUMERIC | PK FK→ | The unique identifier for the transaction record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUTH_ID` | NUMERIC | FK→ | This column contains the list of authorization records linked to a charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |
| `HTT_ID` | [HSP_PRE_AR_SESSION](HSP_PRE_AR_SESSION.md) | sole_pk | high |

