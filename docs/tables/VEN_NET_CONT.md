# VEN_NET_CONT

> The VEN_NET_CONT table contains basic information about your Vendor-Network Contracts used primarily to price referrals and AP Claims. This table also contains information about your reimbursement contracts used in billing system to compare revenue you received from a payor to what you expected to receive.

**Primary key:** `CONTRACT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTRACT_ID` | NUMERIC | PK shared | The unique ID of the contract record. |
| 2 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 3 | `CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

