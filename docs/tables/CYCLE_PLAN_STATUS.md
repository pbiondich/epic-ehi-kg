# CYCLE_PLAN_STATUS

> This table contains data for what cycle plans have been finalized and by whom.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PLAN_CARD_C_NAME` | VARCHAR | org | The cycle plan card. This item is the key for each line. |
| 4 | `PLAN_STATE_C_NAME` | VARCHAR |  | The state of the plan, whether it has been finalized or amended |
| 5 | `PLAN_UPDATE_USER_ID` | VARCHAR |  | The user that signed or amended the plan |
| 6 | `PLAN_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PLAN_UPDATE_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant a plan was signed/amended |
| 8 | `AMENDMENT_REASON_C_NAME` | VARCHAR | org | The reason the user is amending the plan |
| 9 | `AMENDMENT_REASON_COMMENT` | VARCHAR |  | The free-text reason for amending the plan |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |

