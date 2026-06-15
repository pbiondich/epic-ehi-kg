# HSP_ACCT_EBC_ACTPR

> This table contains multiple-response acute problems of the newborn electronic birth certificate information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated acute problems of the newborn electronic birth certificate information. |
| 2 | `LINE` | INTEGER | PK | The line number associated with acute problems of the newborn on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_NBRN_AC_PRB_C_NAME` | VARCHAR | org | This item indicates the acute problems of the newborn on the electronic birth certificate associated with the hospital account: 0-None, 1-Anemia, 2-Birth Injury, 3-Fetal Alcohol Syndrome, 4-Hyaline Membrane Disease/RDS, 5-Meconium Aspiration Syndrome, 6-Assisted Ventilation < 30min, 7-Assisted Ventilation >= 30min, 8-Seizures, 9-ABO Incompatibility, or 10-Other. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

