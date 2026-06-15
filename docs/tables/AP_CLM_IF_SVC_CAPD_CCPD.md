# AP_CLM_IF_SVC_CAPD_CCPD

> Adjustment factor for patients that receive Continuous Ambulatory Peritoneal Dialysis (CAPD) or Continuous Cyclic Perioneal Dialysis (CCPD) at home, received by prospective payment systems (PPS) pricers using the End Stage Renal Disease (ESRD) Pricer. This table extracts the related multiple response item CLM-22279.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `CAPD_CCPD_AT_HOME` | VARCHAR |  | Adjustment factor for patients that receive Continuous Ambulatory Peritoneal Dialysis (CAPD) or Continuous Cyclic Perioneal Dialysis (CCPD) at home. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

