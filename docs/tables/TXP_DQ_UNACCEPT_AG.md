# TXP_DQ_UNACCEPT_AG

> This table lists a patient's unacceptable DQ antigens.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The transplant episode record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DQ_UNACCEPT_AG_C_NAME` | VARCHAR | org | List all of the patient's unacceptable DQ antigens. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

