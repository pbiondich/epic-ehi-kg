# CAP_PAY_EL_DETAILS

> This table stores additional details involving the selection of rate elements used in a capitation or commission transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DETAIL_KEY_GROUP_LINE` | VARCHAR |  | This key corresponds with the rate element's group line in related-multi item DTX 3515 (column GROUP_LINE from table CAP_PAY_EL_IDENT). |
| 4 | `DETAIL_KEY_VALUE_LINE` | VARCHAR |  | This key corresponds with the rate element's value line in related-multi item DTX 3515 (column VALUE_LINE from table CAP_PAY_EL_IDENT). |
| 5 | `REFINEMENT_LOOKUP_TABLE_ID` | VARCHAR |  | Stores the refinement table used to compute the rate element. |
| 6 | `REFINEMENT_LOOKUP_TABLE_ID_RATE_TABLE_NAME` | VARCHAR |  | Name of the capitation rate table. |
| 7 | `MATCHED_CVG_ATTR_C_NAME` | VARCHAR | org | Stores the matched coverage attribute used to select the value for the rate element. |
| 8 | `MATCHED_RIDER_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 9 | `MATCHED_RULE_ID` | VARCHAR |  | Stores the matched rule used to select the value for the rate element. |
| 10 | `MATCHED_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 11 | `SELECTED_VALUE` | NUMERIC |  | Stores the value selected for the rate element from a matched rate group in the lookup table. |
| 12 | `RATE_EL_TIER_MAX` | INTEGER |  | The tier maximum for the rate element. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

