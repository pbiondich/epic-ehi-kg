# AP_CLAIM_ICD_PROC

> The AP_CLAIM_ICD_PROC table contains the ICD-9 Procedure information on an accounts payable claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `LINE` | INTEGER | PK | Line counter of the ICD-9 procedure code on the claim. |
| 3 | `ICD_PX_ID` | VARCHAR | FK→ | The unique ID of the ICD-9 procedure code on the claim. |
| 4 | `ICD_PX_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 5 | `ICD_PX_DT` | DATETIME |  | The date of the ICD-9 procedure code. |
| 6 | `ICD_PX_RANK` | INTEGER |  | The rank of this International Classification of Diseases (ICD) procedure compared to the other ICD procedures on the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `ICD_PX_ID` | [CL_ICD_PX](CL_ICD_PX.md) | sole_pk | high |

