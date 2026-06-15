# RUN_EXECUTION_SUMMARY

> Keeps track of the agents and their executions.

**Primary key:** `AI_INTRCT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AI_INTRCT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interaction record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `RUN_ID_SUM` | VARCHAR |  | A unique ID that identifies an individual execution of the model or agent. This item holds the source of truth for runs that may be used as a key in other related group tables. |
| 5 | `MODEL_ID` | NUMERIC |  | A pointer to the model that was executed in the run |
| 6 | `MODEL_ID_ACUITY_SYSTEM_NAME` | VARCHAR |  | The name of this HDA record. |
| 7 | `RUN_START_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when this execution occured |
| 8 | `RUN_END_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when this execution finished |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AI_INTRCT_ID` | [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | sole_pk | high |

