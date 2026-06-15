# HSP_ACCT_BLD_REV

> This table contains blood review information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated blood review information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each blood review will have its own line number. |
| 3 | `BLD_RVW_UNITS` | INTEGER |  | Number of blood units used for the blood review associated with the hospital account. |
| 4 | `BLD_RVW_DT` | DATETIME |  | Date of blood review associated with hospital account. |
| 5 | `BLD_RVW_PHYS_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `BLD_RVW_COMP_C_NAME` | VARCHAR | org | This column stores the blood component of the blood review associated with the hospital account. e.g., Cryoprecipitate, Fresh frozen plasma, Platelets, Packed red blood cells, etc. |
| 7 | `BR_CRIT_MET_C_NAME` | VARCHAR |  | Were the criteria of the blood review associated with the hospital account met? 1-yes 2-no 3-N/A |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

