# CAP_PAY_EL_MATCH_CVG_ATTR

> This table will be deprecated. To continue accessing this data, use the MATCHED_CVG_ATTR_C column from the CAP_PAY_EL_DETAILS table. The coverage attributes matched to when returning the rate.

**Primary key:** `TX_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `MATCHED_CVG_ATTR_C_NAME` | VARCHAR | org | This column will be deprecated. To continue accessing this data, use the MATCHED_CVG_ATTR_C column from the CAP_PAY_EL_DETAILS table. The coverage attributes used to select the rate groups from the lookup table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

