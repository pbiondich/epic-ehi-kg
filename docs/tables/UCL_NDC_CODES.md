# UCL_NDC_CODES

> The UCL_NDC_CODES table contains information about NDC codes for universal charge records.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID associated with the charge record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NDC_CODE_ID` | VARCHAR |  | The medication national drug codes associated with the charge. |
| 4 | `NDC_CODE_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 5 | `NDC_CODE_ADMIN_AMT` | NUMERIC |  | Administered amount for associated national drug code. |
| 6 | `NDC_CODE_UNIT_C_NAME` | VARCHAR |  | Unit associated with NDC administered amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

