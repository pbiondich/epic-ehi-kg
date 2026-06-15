# AP_CLAIM_IF_DX_HAC_CAT

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
| 4 | `DX_HAC_CAT` | VARCHAR |  | Indicates the HAC category for the diagnosis when all HAC criteria are met. |
| 5 | `DX_HAC_CAT_1` | VARCHAR |  | The first HAC category for the diagnosis line. |
| 6 | `DX_HAC_CAT_2` | VARCHAR |  | The second HAC category for the diagnosis line. |
| 7 | `DX_HAC_CAT_3` | VARCHAR |  | The third HAC category for the diagnosis line. |
| 8 | `DX_HAC_CAT_4` | VARCHAR |  | The fourth HAC category for the diagnosis line. |
| 9 | `DX_HAC_CAT_5` | VARCHAR |  | The fifth HAC category for the diagnosis line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

