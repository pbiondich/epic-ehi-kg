# OR_CASE_MATERIALS_SPEC_ND

> Case materials special needs table.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CASE_MATERIALS_SPEC_NDS_C_NAME` | VARCHAR | org | This item stores the case materials special needs. |
| 4 | `CASE_MATERIALS_SPEC_NDS_QTY` | INTEGER |  | This item stores the materials special needs quantity. |
| 5 | `CASE_MATERIALS_SPEC_NDS_SIZE` | INTEGER |  | This item stores the materials special needs size. |
| 6 | `CASE_MATERIALS_SPEC_NDS_FT` | VARCHAR |  | This item stores the free text for case materials special needs. |
| 7 | `CASE_MATERIALS_SPEC_NDS_SZ_FT` | VARCHAR |  | This item stores the free text information for the case materials size special needs. |
| 8 | `MATERIALS_SITE_MOD_C_NAME` | VARCHAR | org | This item stores the materials special needs site modifier |
| 9 | `MATERIALS_POWER_C_NAME` | VARCHAR | org | This item stores the materials special needs power |
| 10 | `MATERIALS_SIZE_C_NAME` | VARCHAR | org | This item stores the materials special needs size category |
| 11 | `MATERIALS_MODEL_C_NAME` | VARCHAR | org | This item stores the materials special needs model |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

