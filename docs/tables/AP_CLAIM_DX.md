# AP_CLAIM_DX

> The AP_CLAIM_DX table contains one record for each diagnosis on an accounts payable claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record for this diagnosis. |
| 2 | `LINE` | INTEGER | PK | The line number of the diagnosis for this claim record. For example, if a claim has two associated diagnoses, two AP_CLAIM_DX records will be generated: one with a line number of 1, the other with a line number of 2. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `AP_DX_NUM` | INTEGER |  | The number of the diagnosis associated with this record. |
| 5 | `AP_DX_QUALIFIER_C_NAME` | VARCHAR | org | The qualifier related to the diagnosis associated with this record. |
| 6 | `AP_DX_POA_C_NAME` | VARCHAR |  | Present on Admission (POA) for the diagnosis code. |
| 7 | `AP_DX_RANK` | INTEGER |  | The rank of this diagnosis compared to the other diagnoses on the claim. |
| 8 | `CLAIM_DX_FROM_HEADER_YN` | VARCHAR |  | Indicates whether the diagnosis was received at the header level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

