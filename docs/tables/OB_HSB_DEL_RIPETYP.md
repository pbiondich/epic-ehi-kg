# OB_HSB_DEL_RIPETYP

> This table contains information about the cervical ripening methods used during labor for this pregnancy.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID assigned to the episode record (HSB .1). |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `OBD_CERV_RIPE_TP_C_NAME` | VARCHAR | org | This column stores cervical ripening methods employed during the labor for this pregnancy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

