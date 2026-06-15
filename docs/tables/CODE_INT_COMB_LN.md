# CODE_INT_COMB_LN

> This table holds the combined service lines created by code integration.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hosp acct record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CODE_INT_REV_CODE_ID` | NUMERIC |  | This column stores the unique identifier for the revenue code for the combined service line. |
| 4 | `CODE_INT_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 5 | `CODE_INT_CPT` | VARCHAR |  | This item holds the CPT(R)/HCPCS code for the combined service line. |
| 6 | `CODE_INT_MOD_1_ID` | VARCHAR |  | This column stores the unique identifier for the first modifier for the combined service line. |
| 7 | `CODE_INT_MOD_1_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 8 | `CODE_INT_MOD_2_ID` | VARCHAR |  | This column stores the unique identifier for the second modifier for the combined service line. |
| 9 | `CODE_INT_MOD_2_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 10 | `CODE_INT_MOD_3_ID` | VARCHAR |  | This column stores the unique identifier for the third modifier for the combined service line. |
| 11 | `CODE_INT_MOD_3_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 12 | `CODE_INT_MOD_4_ID` | VARCHAR |  | This column stores the unique identifier for the fourth modifier for the combined service line. |
| 13 | `CODE_INT_MOD_4_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 14 | `CODE_INT_RATE` | NUMERIC |  | This item holds the daily rate for the combined service line. The rate is only set for accommodation (room charge) revenue codes. |
| 15 | `CODE_INT_DATE` | DATETIME |  | This item holds the service date for the combined service line. |
| 16 | `CODE_INT_QTY` | INTEGER |  | This item holds the quantity (number of units) for the combined service line. |
| 17 | `CODE_INT_AMT` | NUMERIC |  | This item holds the full charge amount for the combined service line. The value includes any non-covered amount for the line. |
| 18 | `CODE_INT_NONCVRD` | NUMERIC |  | This item holds the non-covered amount for the combined service line. |
| 19 | `CODE_INT_LN_SRC_C_NAME` | VARCHAR |  | This item holds the source for the CPT(R)/HCPCS code and modifiers for the combined service line. |
| 20 | `CODE_INT_UNUSED_YN` | VARCHAR |  | This item identifies lines that are not true service lines but represent coded CPT(R)/HCPCS codes that cannot be used to create actual service lines. |
| 21 | `CODE_INT_CHRG_CNT` | INTEGER |  | This item holds the number of charges associated with the combined service line. |
| 22 | `CODE_INT_RSN_C_NAME` | VARCHAR |  | This item identifies the reason the coded CPT(R)/HCPCS code could not be used in an actual service line. This item is only set when the unused coded CPT(R)/HCPCS flag (CODE_INT_UNUSED_YN) is Yes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

