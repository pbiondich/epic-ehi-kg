# HSP_TX_DIAG

> This table contains hospital account transaction diagnoses from the Hospital Permanent Transactions (HTR) master file.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Because multiple diagnosis codes can be associated with one charge, each diagnosis will have a unique line number. |
| 3 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account associated with the hospital billing transaction. |
| 4 | `POST_DATE` | DATETIME |  | The post date of a transaction. |
| 5 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 7 | `DX_QUAL_HA_C_NAME` | VARCHAR | org | A qualifier entered with a diagnosis code in charge entry. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

