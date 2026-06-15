# TXP_A_UNACCEPT_AG

> Table of all of a transplant patient's A unacceptable antigens.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The transplant episode record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `A_UNACCEPTABLE_AG_C_NAME` | VARCHAR | org | List of the patient's unacceptable A antigens |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

