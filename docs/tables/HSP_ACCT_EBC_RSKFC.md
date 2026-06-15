# HSP_ACCT_EBC_RSKFC

> This table contains multiple-response medical risk factors for pregnancy electronic birth certificate information in the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated medical risk factors for the pregnancy electronic birth certificate information. |
| 2 | `LINE` | INTEGER | PK | The line number associated with medical risk factors for the pregnancy on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_MED_RSK_FAC_C_NAME` | VARCHAR | org | Indicates the medical risk factors of the pregnancy on the electronic birth certificate associated with the hospital account. 0-None, 1-Anemia, 2-Cardiac Disease, 3-Acute or Chronic Lung Disease, 4-Diabetes, 5-Genital Herpes, 6-Hydramnios/Oligohydramnios, 7-Hemoglobinopathy, 8-Hypertension, Chronic, 9-Hypertension, Pregnancy-associated, 10-Eclampsia, 11-Incompetent Cervix, 12-Previous Infant 4000+ grams, 13-Previous Preterm or Small for Gestational Age Infant, 14-Renal Disease, 15-RH Sensitization, 16-Uterine Bleeding, 17-Infectious Disease, 18-Low MSAFP, 19-High MSAFP, 20-Other |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

