# RYN_WHT_GENO_PHENO_SCREEN

> Stores data for Ryan White CAREWare Geno/Pheno Screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_GENO_PHENO_DATE` | DATETIME |  | The date on which the Geno/Pheno screening took place. |
| 4 | `RW_GENOPHENO_RSLT_C_NAME` | VARCHAR |  | The result of the Geno/Pheno screening. |
| 5 | `RW_GENO_PHENO_SCORE` | NUMERIC |  | The numerical score of the Geno/Pheno screening. |
| 6 | `RW_GENO_PHENO_CMTS` | VARCHAR |  | The comments for the Geno/Pheno screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

