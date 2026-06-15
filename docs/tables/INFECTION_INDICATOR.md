# INFECTION_INDICATOR

> The INFECTION_INDICATOR table contains detailed information about the auto-infection and rule-out infection rules that were used to add or indicate infections.

**Primary key:** `INFECTION_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFECTION_ID` | NUMERIC | PK FK→ | The unique identifier for the infection record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INF_INDICATOR_TYPE_C_NAME` | VARCHAR |  | The indicator type category ID describing the method by which the infection was indicated. |
| 4 | `INDICATED_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when the infection was indicated. |
| 5 | `INDICATING_ORDER_ID` | NUMERIC |  | The unique ID of the order that indicated the infection. |
| 6 | `INDICATING_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `INDICATING_COMPONENT_ID` | NUMERIC |  | The unique ID of the component specified in the auto-infection rule. |
| 8 | `INDICATING_COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 9 | `INDICATING_ORGANISM_ID` | NUMERIC |  | The unique ID of the organism where the auto-infection or rule-out infection rule that indicated the infection is specified. |
| 10 | `INDICATING_ORGANISM_ID_NAME` | VARCHAR |  | The name of the organism. |
| 11 | `INDICATING_ANTIBIOTIC_C_NAME` | VARCHAR | org | The antibiotic category ID matching the antibiotic specified in the auto-infection rule. |
| 12 | `INDICATING_SUSCEPT_C_NAME` | VARCHAR | org | The susceptibility category ID specified in the auto-infection rule. |
| 13 | `INDICATING_LRD_ID_RECORD_NAME` | VARCHAR |  | The record name for the Lab Result Definition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFECTION_ID` | [INFECTIONS](INFECTIONS.md) | sole_pk | high |

