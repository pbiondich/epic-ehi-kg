# HSP_ACCT_EBC_VG_CNGAN

> Congenital anomalies of the newborn for electronic birth certificate extract. This table is a new version of HSP_ACCT_EBC_CNGAN, geared toward the 2003 standard for reporting birth information. This item is based on options allowed in birth information form version G from the state of Hawaii.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONGENITAL_ANOM_C_NAME` | VARCHAR | org | The congenital anomalies of the newborn category ID for Electronic Birth Certificate information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

