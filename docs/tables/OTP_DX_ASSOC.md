# OTP_DX_ASSOC

> The diagnoses associated with an order template. Note that if an order template is unreleased and it has no diagnoses then it will use the plan diagnoses stored in the ASSOCIATED_DX table.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each diagnosis associated with the order template in this row. |
| 3 | `ASSOC_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `ASSOC_DX_DESC` | VARCHAR |  | The description of a diagnosis associated with the order template in this row. |
| 5 | `ASSOC_DX_COMMENT` | VARCHAR |  | The comment for a diagnosis associated with the order template in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

