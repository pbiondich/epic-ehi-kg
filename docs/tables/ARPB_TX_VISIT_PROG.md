# ARPB_TX_VISIT_PROG

> This table contains information about the patient visit programs that were entered in charge entry for these transactions. This information is typically used in sliding scale calculations and as a grouper for transactions.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_VISIT_PROGRAM_C_NAME` | VARCHAR | org | This item stores the patient visit program that was entered during charge entry. This field is commonly used as grouper and for sliding scale. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

