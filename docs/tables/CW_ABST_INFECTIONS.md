# CW_ABST_INFECTIONS

> Infection information from abstractions with clinical information reported to CROWNWeb, the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INFECTION_ID` | VARCHAR | FK→ | The dialysis patient's infection ID. |
| 4 | `INFECTION_REQ_HOSP_YN` | VARCHAR |  | Shows whether a dialysis patient's infections required hospitalization. |
| 5 | `INFECTION_REQ_HOSP_NA_YN` | VARCHAR |  | Shows whether a dialysis patient's infection hospitalization information is available. |
| 6 | `INFECTION_HOSP_DATE` | DATETIME |  | The dialysis patient's infection hospitalization date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFECTION_ID` | [INFECTIONS](INFECTIONS.md) | sole_pk | high |

