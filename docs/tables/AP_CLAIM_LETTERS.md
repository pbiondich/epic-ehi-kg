# AP_CLAIM_LETTERS

> This table holds letters generated for AP claims.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique ID of the claim |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LTRS_GENERATED_ID` | VARCHAR |  | Stores the letters generated for this claim. |
| 4 | `LTRS_GENERATED_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 5 | `LTRS_GENERATED_DATE` | DATETIME |  | The date on which the letter was generated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

