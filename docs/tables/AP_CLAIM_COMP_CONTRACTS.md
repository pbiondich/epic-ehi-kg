# AP_CLAIM_COMP_CONTRACTS

> This table contains information about contract comparisons performed for a claim. This includes the contract, prospective payment systems (PPS) pricer, and claim-level contractual allowed amount for each contract evaluated for the claim. Each row in the table represents one contract that was evaluated for a claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTRACT_ID` | NUMERIC | shared | Each contract that was evaluated for the claim for contract comparison. |
| 4 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 5 | `CONTRACT_CONTACT_DATE` | DATETIME |  | The contact date used for each contract evaluated for the claim for contract comparison. |
| 6 | `ALLOWED_AMT` | NUMERIC |  | The total claim allowed amount calculated using each contract for contract comparison. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

