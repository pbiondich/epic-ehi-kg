# AP_CLAIM_IF_PX_HAC_USE

> The diagnosis hospital-acquired condition (HAC) categories.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PX_HAC_USAGE` | VARCHAR |  | Indicates how the procedure code was used in satisfying a hospital-acquired condition category. |
| 5 | `PX_HAC_USAGE_1` | VARCHAR |  | Indicates how the first procedure code was used in satisfying a hospital-acquired condition category. |
| 6 | `PX_HAC_USAGE_2` | VARCHAR |  | Indicates how the second procedure code was used in satisfying a hospital-acquired condition category. |
| 7 | `PX_HAC_USAGE_3` | VARCHAR |  | Indicates how the third procedure code was used in satisfying a hospital-acquired condition category. |
| 8 | `PX_HAC_USAGE_4` | VARCHAR |  | Indicates how the fourth procedure code was used in satisfying a hospital-acquired condition category. |
| 9 | `PX_HAC_USAGE_5` | VARCHAR |  | Indicates how the fifth procedure code was used in satisfying a hospital-acquired condition category. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

