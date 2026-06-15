# AP_CLAIM_IF_DX_HAC_USAGE

> Indicates if the diagnosis code and present on admission (POA) value combination were used in grouper processing.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `DX_HAC_USAGE` | VARCHAR |  | Indicates if the diagnosis code and present on admission (POA) value combination were used in grouper processing. |
| 5 | `DX_HAC_USAGE_1` | VARCHAR |  | Whether or not the first diagnosis code and POA value combination were used in grouper processing. |
| 6 | `DX_HAC_USAGE_2` | VARCHAR |  | Whether or not the second diagnosis code and POA value combination were used in grouper processing. |
| 7 | `DX_HAC_USAGE_3` | VARCHAR |  | Whether or not the third diagnosis code and POA value combination were used in grouper processing. |
| 8 | `DX_HAC_USAGE_4` | VARCHAR |  | Whether or not the fourth diagnosis code and POA value combination were used in grouper processing. |
| 9 | `DX_HAC_USAGE_5` | VARCHAR |  | Whether or not the fifth diagnosis code and POA value combination were used in grouper processing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

