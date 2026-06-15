# AP_CLAIM_IF_PX_USE

> The procedure code that was used during processing; may be the entered or the mapped code.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PX_USED` | VARCHAR |  | The procedure code that was used during processing; may be the entered or the mapped code. |
| 5 | `PX_USED_1` | VARCHAR |  | First procedure code used. |
| 6 | `PX_USED_2` | VARCHAR |  | Second procedure code used. |
| 7 | `PX_USED_3` | VARCHAR |  | Third procedure code used. |
| 8 | `PX_USED_4` | VARCHAR |  | Fourth procedure code used. |
| 9 | `PX_USED_5` | VARCHAR |  | Fifth procedure code used. |
| 10 | `PX_USED_6` | VARCHAR |  | Sixth procedure code used. |
| 11 | `PX_USED_7` | VARCHAR |  | Seventh procedure code used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

