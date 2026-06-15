# HSP_ACCT_EBC_OB_PX

> This table contains multiple-response obstetric procedures electronic birth certificate information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated obstetric procedures electronic birth certificate information. |
| 2 | `LINE` | INTEGER | PK | The line number associated with obstetric procedures on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_OBST_PX_C_NAME` | VARCHAR | org | Indicates the obstetric procedures on the electronic birth certificate associated with the hospital account. 0-None, 1-Amniocentesis, 2-Electronic Fetal Monitoring, 3-Induction of Labor, 4-Simulation of Labor, 5-Tocolysis, 6-Ultrasound, 7-Other |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

