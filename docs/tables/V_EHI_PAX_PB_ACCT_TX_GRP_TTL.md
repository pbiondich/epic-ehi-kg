# V_EHI_PAX_PB_ACCT_TX_GRP_TTL

> This view filters out premium billing transaction data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `TRANSACTION_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_ID` | VARCHAR | PK FK→ | The unique identifier for the account transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EMP_GRP_PAX_GRP_ID` | VARCHAR |  | Specifies the employer groups for premium billing acount transactions group total. |
| 4 | `EMP_GRP_PAX_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 5 | `REM_PAX_GRP_TTL_AMT` | NUMERIC |  | Specifies the remaining premium billing account transactions group total amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSACTION_ID` | [CAP_DTL_TX](CAP_DTL_TX.md) | sole_pk | high |

