# HSC_MICRO_SPEC_INSTR

> The HSC_MICRO_SPEC_INSTR table contains special instruction information for microbiology specimens.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MICROBIOLOGY_SPEC_INSTR_C_NAME` | VARCHAR | org | The category values for the microbiology special instructions for a specimen record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

