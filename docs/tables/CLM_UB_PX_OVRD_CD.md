# CLM_UB_PX_OVRD_CD

> The UB procedures to override the principal and other procedures (free text) and their corresponding dates on the UB claim form. This is used by professional billing only.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique ID for the claim information record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UB_PRC_PX_OVRD_CD` | VARCHAR |  | The International Classification of Diseases (ICD) procedures to populate the principal and other ICD procedure fields on institutional claims. |
| 4 | `UB_PRC_PX_OVRD_DT` | DATETIME |  | The International Classification of Diseases (ICD) procedure dates to populate the principal and other ICD procedure fields on institutional claims. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

