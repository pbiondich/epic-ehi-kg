# INTERV_SMARTTEXT

> This table displays the SmartTexts that are associated with intervention (LPI) records.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | The unique identifier for the intervention record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SMARTTEXTS_ID` | VARCHAR |  | Smarttext template for intervention documentation. |
| 4 | `SMARTTEXTS_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 5 | `IP_INV_LDS_ID` | VARCHAR |  | Inpatient intervention discipline associated with this SmartText. |
| 6 | `IP_INV_LDS_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |
| 7 | `HH_INT_DISC_C_NAME` | VARCHAR | org | Home Health discipline for intervention |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

