# CVG_MEM_RISK_ADJ_FACT

> This table holds member level risk adjustment factor.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The member that the risk adjustment factor applies to. |
| 4 | `EFF_DATE` | DATETIME |  | The effective date of the risk adjustment factor. |
| 5 | `TERM_DATE` | DATETIME |  | The termination date of the risk adjustment factor. |
| 6 | `RISK_ADJ_FACT_MODEL_C_NAME` | VARCHAR | org | The model of the risk adjustment factor. |
| 7 | `RISK_ADJ_FACT_TYPE_C_NAME` | VARCHAR | org | The type of the risk adjustment factor. |
| 8 | `RISK_ADJ_FACTOR` | NUMERIC |  | The risk adjustment factor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

