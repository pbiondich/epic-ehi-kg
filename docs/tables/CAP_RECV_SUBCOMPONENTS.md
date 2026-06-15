# CAP_RECV_SUBCOMPONENTS

> Stores capitation payment subcomponents that were used to calcuate the total payment amount.

**Primary key:** `TRANSACTION_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the detail transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CAP_SUBCOMP_TYP_C_NAME` | VARCHAR |  | Stores the type of one component part used to calculate the total amount of a capitation payment. |
| 4 | `CAP_SUBCOMP_VALUE` | NUMERIC |  | Stores the value of one component part used to calculate the total amount of a capitation payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSACTION_ID` | [CAP_DTL_TX](CAP_DTL_TX.md) | sole_pk | high |

