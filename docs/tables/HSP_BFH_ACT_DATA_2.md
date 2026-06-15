# HSP_BFH_ACT_DATA_2

> This table stores billing activity history action-specific data.

**Overflow of:** [HSP_BFH_ACT_DATA](HSP_BFH_ACT_DATA.md)  
**Primary key:** `BFH_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the activity history record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACT_WAS_FORCED_YN` | VARCHAR |  | Stores whether the action was forced by a user or not. |
| 4 | `ACTION_PREV_GUAR_ACCT_ID` | NUMERIC |  | Stores the guarantor on the account before the action was performed. |
| 5 | `ACTION_CUR_GUAR_ACCT_ID` | NUMERIC |  | Stores the guarantor on the account after the action was performed. |
| 6 | `ACT_LATE_CHG_OPT_C_NAME` | VARCHAR |  | This item holds the late charge selection option chosen for processing late charges. The default is 0-All Prebilled Charges. |
| 7 | `BILL_DT_RNG_SEL_MTHD_C_NAME` | VARCHAR |  | This item holds the date range selection method used to default the date ranges when date range billing. |
| 8 | `ACT_GUARANTOR_TYPE_C_NAME` | VARCHAR | org | The guarantor type used to automatically select the guarantor in a Change Guarantor action |
| 9 | `ACTION_VOICE_NUMBER` | VARCHAR |  | The phone number that was selected for voice when the action was performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

