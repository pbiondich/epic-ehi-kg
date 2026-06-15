# CAP_PAY_EL_REF_LKUP_TABLE

> This table will be deprecated. To continue accessing this data, use the REFINEMENT_LOOKUP_TABLE_ID column from the CAP_PAY_EL_DETAILS table. The refinement tables used to compute the rate.

**Primary key:** `TX_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `REFINEMENT_LOOKUP_TABLE_ID` | VARCHAR |  | This column will be deprecated. To continue accessing this data, use the REFINEMENT_LOOKUP_TABLE_ID column from the CAP_PAY_EL_DETAILS table. The additional refinement tables used to look up a member's rate. |
| 5 | `REFINEMENT_LOOKUP_TABLE_ID_RATE_TABLE_NAME` | VARCHAR |  | Name of the capitation rate table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

