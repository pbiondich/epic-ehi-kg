# HSP_ACCT_EBC_CNGAN

> This table contains multiple-response congenital anomalies of the newborn electronic birth certificate information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated congenital anomalies of the newborn electronic birth certificate information. |
| 2 | `LINE` | INTEGER | PK | The line number associated with congenital anomalies of the newborn on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_CNGNTL_ANOM_C_NAME` | VARCHAR | org | Indicates the congenital anomalies of the newborn on the electronic birth certificate associated with the hospital account. 0-None, 1-Anencephalus, 2-Spinal Bifida/Meningocele,3-Hydrocephalus, 4-Microcephalus, 5-Other Central Nervous System Anomalies, 6-Heart Malformation, 7-Other Circulatory Anomalies, 8-Respiratory Anomalies, 9-Rectal Atresia/Stenosis,10-Tracheo-esophageal Fistula/Esophageal Atresia, 11-Omphalocele/Gastroschisis, 12-Other Gastrointestinal Anomalies, 13-Malformed Genitalia, 14-Renal Agenesis, 15-Hydrocele, 16-Other Urogenital Anomalies, 17-Cleft Lip/Palate, 18-Polydactyly/Syndactyly/Adactyly, 19-Club Foot, 20-Diaphragmalic Hernia, 21-Other Musculoskeletal Anomalies, 22-Downs Syndrome, 23-Other Chromosomal Anomalies, 24-Hemangioma, 25-Nevus, 26-Simian Crease, 27-Skin Tag, 28-Other Skin Anomalies |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

