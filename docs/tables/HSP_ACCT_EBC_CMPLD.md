# HSP_ACCT_EBC_CMPLD

> This table contains multiple-response complications of labor and delivery electronic birth certificate information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated complication of labor and delivery electronic birth certificate information. |
| 2 | `LINE` | INTEGER | PK | The line number associated with complications of labor and delivery on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_COMPL_LANDD_C_NAME` | VARCHAR | org | This column stores the complications of labor and delivery on the electronic birth certificate associated with the hospital account: 0-None, 1-Febrile, 2-Meconium: Moderate/Heavy, 3-Premature Rupture of Membrane, 4-Abruptio Placenta, 5-Placenta Previa, 6-Other Excessive Bleeding, 7-Seizures During Labor, 8-Precipitous Labor, 9-Prolonged Labor, 10-Dysfunctional Labor, 11-Breech/Malpresentation, 12-Cephalopelvic Disproportion, 13-Cord Prolapse, 14-Anesthetic Complications, 15-Fetal Distress, or 16-Other. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

