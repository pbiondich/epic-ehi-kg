# STG_PED_INFO

> This table stores pediatric cancer staging information. Note that the only records extracted into this table are those with non-null data in the Pediatric Stage (I STG 300) item (Clarity column PEDIATRIC_STAGE_C).

**Primary key:** `STAGE_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STAGE_ID` | NUMERIC | PK shared | The cancer stage ID. |
| 2 | `PEDIATRIC_STAGE_C_NAME` | VARCHAR | org | The pediatric stage. |
| 3 | `STAGE_TITLE_NM` | VARCHAR |  | The title of this cancer stage row, usually indicative of the body site or cancer type being staged. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

