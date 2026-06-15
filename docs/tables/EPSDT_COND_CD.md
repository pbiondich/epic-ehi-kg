# EPSDT_COND_CD

> All values associated with a claim are stored in the Claim External Value record. The EPSDT_COND_CD table holds Early & Periodic Screening, Diagnosis, and Treatment (EPSDT) related condition codes.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `EPSDT_COND_IND` | VARCHAR |  | This item holds the condition codes related to Early & Periodic Screening, Diagnosis, and Treatment Services. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

