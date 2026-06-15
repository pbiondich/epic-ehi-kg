# HSP_ACCT_OPERATIVE

> This table contains operative component information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account containing related operative information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each operative information set will have its own line number. |
| 3 | `OPER_COMP_C_NAME` | VARCHAR | org | Operative component note type associated with hospital account. i.e. 1-dictated 2-progress note |
| 4 | `OPER_PHYSICIAN_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `OPER_DT` | DATETIME |  | Date of operation associated with hospital account. |
| 6 | `CRIT_MET_C_NAME` | VARCHAR |  | This column stores whether the criteria of the operation associated with the hospital account were met: 1-yes, 2-no, or 3-N/A. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

