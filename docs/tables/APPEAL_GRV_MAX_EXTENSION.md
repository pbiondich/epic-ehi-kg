# APPEAL_GRV_MAX_EXTENSION

> This table contains information about the maximum extensions that can be taken for an appeal or grievance.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXTENSION_TAT_TIME_STANDARD_C_NAME` | VARCHAR | org | Which timeliness standard this line in the related group corresponds to. |
| 4 | `MAX_EXTENSION_DAYS` | NUMERIC |  | The maximum number of days the timeframe can be extended. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

