# HH_ALERT_INFO

> This table stores information about the Home Health Alerts.

**Primary key:** `ALERT_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier for the alert record. |
| 2 | `ALERT_TYPE_ID` | INTEGER | FK→ | The type of the alert. |
| 3 | `STATE_INFO` | VARCHAR |  | The alert state information. |
| 4 | `SUMMARY_BLOCK_ID` | NUMERIC | shared | The episode of care ID for which the alert was shown |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALERT_TYPE_ID` | [HH_ALERT_TYPE_INFO](HH_ALERT_TYPE_INFO.md) | sole_pk | high |

