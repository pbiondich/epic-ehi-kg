# AP_CLAIM_IF_PX_USED_HAC

> This table extracts the related multiple response Interface Info - Grouper Px - Used for HAC Processing (I CLM 21874) item.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PX_USED_HAC_PROC` | VARCHAR |  | Procedure codes that were used during hospital-acquired condition adjusted diagnosis related group processing. |
| 5 | `PX_USED_HAC_PROC_1` | VARCHAR |  | The first procedure code that was used during hospital-acquired condition adjusted diagnosis related group processing. |
| 6 | `PX_USED_HAC_PROC_2` | VARCHAR |  | The second procedure code that was used during hospital-acquired condition adjusted diagnosis related group processing. |
| 7 | `PX_USED_HAC_PROC_3` | VARCHAR |  | The third procedure code that was used during hospital-acquired condition adjusted diagnosis related group processing. |
| 8 | `PX_USED_HAC_PROC_4` | VARCHAR |  | The fourth procedure code that was used during hospital-acquired condition adjusted diagnosis related group processing. |
| 9 | `PX_USED_HAC_PROC_5` | VARCHAR |  | The fifth procedure code that was used during hospital-acquired condition adjusted diagnosis related group processing. |
| 10 | `PX_USED_HAC_PROC_6` | VARCHAR |  | The sixth procedure code that was used during hospital-acquired condition adjusted diagnosis related group processing. |
| 11 | `PX_USED_HAC_PROC_7` | VARCHAR |  | The seventh procedure code that was used during hospital-acquired condition adjusted diagnosis related group processing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

