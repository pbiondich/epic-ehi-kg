# HSP_ACCT_EBC_DLVMD

> This table contains multiple-response method of delivery electronic birth certificate information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated method of delivery electronic birth certificate information. |
| 2 | `LINE` | INTEGER | PK | The line number associated with method of delivery on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_DLVRY_MTHD_C_NAME` | VARCHAR | org | Indicates the method of delivery on the electronic birth certificate associated with the hospital account. 1-Vaginal, 2-Vaginal Birth After Previous C-Section, 3-Primary C-Section, 4-Repeat C-Section, 5-Forceps, 6-Vacuum |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

