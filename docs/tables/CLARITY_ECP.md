# CLARITY_ECP

> The CLARITY_ECP table contains summary information about the pricing contracts billing system uses to adjudicate the price of a charge.

**Primary key:** `CONTRACT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the pricing contract. |
| 2 | `CONTRACT_NAME` | VARCHAR |  | The name of the pricing contract. |
| 3 | `SELFPAY_WO_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

