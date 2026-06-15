# MYC_PLAN_SELF_SIGNUP_STAT

> Status for all MyChart users that are viewing an episode-related MyChart self-signup care plan.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MYC_PLAN_SIGNUP_MYPT_ID` | VARCHAR |  | MyChart User ID (WPR ID) to be associated with current line for self-signup care plan. |
| 4 | `MYC_PLAN_STATUS_C_NAME` | VARCHAR |  | Current status of the self-signup plan for MyChart User. |
| 5 | `MYC_PLAN_CAREPLAN_ID` | VARCHAR |  | Care plan ID for the MyChart self-signup plan |
| 6 | `LAST_GEST_AGE_DISMISSED_DAYS` | INTEGER |  | Day number of gestation age when MyChart pregnancy progress health feed card was last dismissed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

