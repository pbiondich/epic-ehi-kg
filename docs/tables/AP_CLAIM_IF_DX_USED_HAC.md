# AP_CLAIM_IF_DX_USED_HAC

> This table extracts the related multiple response Interface Info - Grouper - Dx Used for HAC Processing (I CLM 21856) item.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `DX_USED_HAC_PROCESS` | VARCHAR |  | Diagnosis codes that were used during hospital-acquired condition (HAC)-adjusted diagnosis related group (DRG) processing. |
| 5 | `DX_USED_HAC_PROCESS_1` | VARCHAR |  | The first diagnosis code that was used during HAC adjusted DRG processing. |
| 6 | `DX_USED_HAC_PROCESS_2` | VARCHAR |  | The second diagnosis code that was used during HAC adjusted DRG processing. |
| 7 | `DX_USED_HAC_PROCESS_3` | VARCHAR |  | The third diagnosis code that was used during HAC adjusted DRG processing. |
| 8 | `DX_USED_HAC_PROCESS_4` | VARCHAR |  | The fourth diagnosis code that was used during HAC adjusted DRG processing. |
| 9 | `DX_USED_HAC_PROCESS_5` | VARCHAR |  | The fifth diagnosis code that was used during HAC adjusted DRG processing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

