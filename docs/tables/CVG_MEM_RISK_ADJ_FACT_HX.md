# CVG_MEM_RISK_ADJ_FACT_HX

> The historical values of the CVG_MEM_RISK_ADJ_FACT table over time.

**Primary key:** `CVG_ID`, `LINE`, `CVG_ITM_HX_REL_ACT_GUID`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The member that the risk adjustment factor applies to. |
| 4 | `EFF_DATE` | DATETIME |  | The effective date of the risk adjustment factor. |
| 5 | `TERM_DATE` | DATETIME |  | The termination date of the risk adjustment factor. |
| 6 | `RISK_ADJ_FACT_MODEL_C_NAME` | VARCHAR | org | The model of the risk adjustment factor. |
| 7 | `RISK_ADJ_FACT_TYPE_C_NAME` | VARCHAR | org | The type of the risk adjustment factor. |
| 8 | `RSK_ADJ_FACTOR` | NUMERIC |  | The risk adjustment factor. |
| 9 | `ITM_HX_START_LOCAL_DTTM` | DATETIME (Local) |  | The start instant of when the coverage/line combination is valid in local time. |
| 10 | `ITM_HX_START_UTC_DTTM` | DATETIME (UTC) |  | The start instant of when the coverage/line combination is valid in UTC. |
| 11 | `ITM_HX_END_LOCAL_DTTM` | DATETIME (Local) |  | The end instant of when the coverage/line combination is valid in local time. |
| 12 | `ITM_HX_END_UTC_DTTM` | DATETIME (UTC) |  | The end instant of when the coverage/line combination is valid in UTC. |
| 13 | `CVG_ITM_HX_REL_ACT_GUID` | VARCHAR | PK | This ID links this audit batch to one or more actions in the coverage action history table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

