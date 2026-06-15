# OB_UTZ_EFW

> This table contains the estimated fetal weight (EFW) calculations. These measurements are derived from fetal measurements.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OB_UTZ_EFW_SRC_C_NAME` | VARCHAR | org | This item stores the calculation method for the estimated fetal weight (EFW) value. |
| 4 | `OB_UTZ_EFW_VAL` | NUMERIC |  | This item stores the results, in grams, of estimated fetal weight calculations. The weight selected by the resulting clinician as definitive for the study can be found by joining on RES_FETALWEIGHT.FINDING_ID=OB_UTZ_EFW.FINDING_ID AND RES_FETALWEIGHT.OB_UTZ_EFW_SEL_C = OB_UTZ_EFW.OB_UTZ_EFW_SRC_C |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

