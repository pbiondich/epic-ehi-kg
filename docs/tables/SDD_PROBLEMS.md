# SDD_PROBLEMS

> This table stores info about problems linked to a patient's Social Driver domains. Each row represents one linked problem, and includes either the internal problem Id or the external problem reference Id.

**Primary key:** `SDOH_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SDOH_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the social driver data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROBLEM_DOM_CONFIG_ID_RECORD_NAME` | VARCHAR |  | The name of the social driver domain configuration record. |
| 4 | `PROBLEM_LIST_ID` | NUMERIC | FK→ | The LPL record that contains a diagnosis related to this Social Drivers of Health domain |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |
| `SDOH_DATA_ID` | [SDD_DATA](SDD_DATA.md) | sole_pk | high |

