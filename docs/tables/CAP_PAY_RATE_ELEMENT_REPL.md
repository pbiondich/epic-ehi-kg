# CAP_PAY_RATE_ELEMENT_REPL

> This table stores rate element information used in a capitation transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FRM_TBL_GRP_TYPE_C_NAME` | VARCHAR |  | The group type of the rate elements. |
| 4 | `LOOKUP_TABLE_ID` | VARCHAR |  | The lookup table which was used to retrieve the rate element's values. |
| 5 | `LOOKUP_TABLE_ID_RATE_TABLE_NAME` | VARCHAR |  | Name of the capitation rate table. |
| 6 | `MATCHED_CVG_ATTR_C_NAME` | VARCHAR | org | This column will be deprecated. To continue accessing this data, use the MATCHED_CVG_ATTR_C column from the CAP_PAY_EL_DETAILS table. The coverage attribute used to select the rate group from the lookup table. |
| 7 | `PREMIUM_BUCKET_ID` | NUMERIC |  | The capitation bucket which was the source of capitation RR subcomponent amounts used in the formula. |
| 8 | `MEM_LIST_ROW_KEY` | INTEGER |  | The row number of the member in the member list (TML) to which each row in related group 3510 corresponds for a specialty capitation transaction. |
| 9 | `MATCHED_RIDER_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 10 | `MATCHED_RULE_ID` | VARCHAR |  | This column will be deprecated. To continue accessing this data, use the MATCHED_RULE_ID column from the CAP_PAY_EL_DETAILS table. The rule that passed when selecting the rate group for the lookup table. |
| 11 | `MATCHED_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 12 | `REFINEMENT_LOOKUP_TABLE_ID` | VARCHAR |  | This column will be deprecated. To continue accessing this data, use the REFINEMENT_LOOKUP_TABLE_ID column from the CAP_PAY_EL_DETAILS table. The additional refinement rate table used to look up a member's rate. |
| 13 | `REFINEMENT_LOOKUP_TABLE_ID_RATE_TABLE_NAME` | VARCHAR |  | Name of the capitation rate table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

