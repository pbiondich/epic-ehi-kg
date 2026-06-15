# PSYCH_HX_REASON_FOR_TREAT

> Reason for treatment table.

**Primary key:** `TREATMENT_HX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_HX_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the history event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REASON_FOR_TREAT_RFV_ID_REASON_VISIT_NAME` | VARCHAR |  | The name of the Reason for Visit record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TREATMENT_HX_ID` | [PSYCH_TREATMENT_HISTORY](PSYCH_TREATMENT_HISTORY.md) | sole_pk | high |

