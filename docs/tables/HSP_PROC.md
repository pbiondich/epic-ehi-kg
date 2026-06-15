# HSP_PROC

> This table contains the surgical procedures for UB claims.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique ID of the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UB_PROC_ID` | NUMERIC |  | The unique ID of the procedure that is associated with this uniform billing claim record. For Professional Billing, this is a record in the procedure master file. For Hospital Billing, this is a record in the International Classification of Diseases procedures master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

