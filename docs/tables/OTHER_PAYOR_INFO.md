# OTHER_PAYOR_INFO

> Information of other payors who paid the claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OTH_PAY_INFO_TY_C_NAME` | VARCHAR |  | This is the type of information of other payors. |
| 4 | `OTH_PAY_INFO_VAL` | VARCHAR |  | This is the value of the information of type mentioned in the corresponding line of Claim Information item 1120 (CLM 1120). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

