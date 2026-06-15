# PREGNANCY_BABY_SEXES

> This table contains information about the sex of fetuses (I HSB 35575) during a pregnancy episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREG_SEX_C_NAME` | VARCHAR |  | Indicates the suspected sex of the fetus during pregnancy, including multiple gestations, or whether the parents want it to be a surprise. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

