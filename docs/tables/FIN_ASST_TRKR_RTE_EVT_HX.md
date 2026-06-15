# FIN_ASST_TRKR_RTE_EVT_HX

> This table contains a history of RTE integration for a tracker.

**Primary key:** `FIN_ASST_TRACKER_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_TRACKER_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the program tracker record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EVT_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant an event was logged in UTC |
| 4 | `EVT_TYP_C_NAME` | VARCHAR | org | Event type being logged |
| 5 | `EVT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 6 | `EVT_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 7 | `EVT_RULE_ID` | VARCHAR |  | Program rule that matched when the tracker query was attempted |
| 8 | `EVT_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 9 | `EVT_ADDL_INFO` | VARCHAR |  | Additional info regarding RTE error codes |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

