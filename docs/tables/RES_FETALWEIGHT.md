# RES_FETALWEIGHT

> OB Ultrasound Fetal Weight.

**Primary key:** `FINDING_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OB_UTZ_FETAL_WT_ROW` | INTEGER |  | The active fetal weight row in the baby's RES record. |
| 2 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 3 | `OB_UTZ_EFW_SEL_C_NAME` | VARCHAR | org | This item stores which estimation of fetal weight was selected as best indicative of a fetus' true weight. The selected EFW is stored as the corresponding category value from column OB_UTZ_EFW_SRC_C in table OB_UTZ_EFW. The weight selected by the resulting clinician as definitive for the study can be found by joining on RES_FETALWEIGHT.FINDING_ID = OB_UTZ_EFW.FINDING_ID AND RES_FETALWEIGHT.OB_UTZ_EFW_SEL_C = OB_UTZ_EFW.OB_UTZ_EFW_SRC_C |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

