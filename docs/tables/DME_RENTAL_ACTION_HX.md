# DME_RENTAL_ACTION_HX

> This table contains durable medical equipment (DME) rental record action history information, such as what action was taken, when, and by whom.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the rental record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_HX_INSTANT_DTTM` | DATETIME (Local) |  | The instant of the action in local time zone. |
| 4 | `ACTION_HX_ACTION_C_NAME` | VARCHAR |  | The action taken. |
| 5 | `ACTION_HX_USER_ID` | VARCHAR |  | The ID of the user performing the action. |
| 6 | `ACTION_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `OLD_VALUE` | VARCHAR |  | Value before it was modified by an action. |
| 8 | `NEW_VALUE` | VARCHAR |  | Value after it was modified by an action. |
| 9 | `ACTION_HX_COMMENT` | VARCHAR |  | Comment for action taken. |
| 10 | `CLAIM_ID` | NUMERIC | FK→ | Stores claim record ID for claim actions. |
| 11 | `ACTION_HX_UTC_DTTM` | DATETIME (UTC) |  | The instant of the action in UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

