# PRESC_PA_REORD_ACT

> This table holds the history of actions taken after the medication being authorized was reordered.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REORD_ACT_C_NAME` | VARCHAR |  | This item holds the history of decisions made about continuing with this prior authorization after a reorder of the associated order occurred. |
| 4 | `REORD_ACT_USER_ID` | VARCHAR |  | This item holds the ID of the user who made the decision about the reorder status. |
| 5 | `REORD_ACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `REORD_ACT_UTC_DTTM` | DATETIME (UTC) |  | This item holds the instant the decision was made about the reorder status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

