# CLARITY_NETWORK

> CLARITY_NETWORK contains basic data on the records in your Network master file. Networks are used to define populations of patients in terms of the benefit plans or payors listed on their coverage records.

**Primary key:** `NETWORK_ID`  
**Columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NETWORK_ID` | VARCHAR | PK | The unique ID assigned to network record. |
| 2 | `NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 3 | `NETWORK_NAME` | VARCHAR |  | The name of the network. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [AP_CLAIM](AP_CLAIM.md) | `NETWORK_ID` | high |
| [CAP_PAYMENT](CAP_PAYMENT.md) | `NETWORK_ID` | high |
| [CAP_PAY_REPL](CAP_PAY_REPL.md) | `NETWORK_ID` | high |
| [MEM_LIST_REPL](MEM_LIST_REPL.md) | `NETWORK_ID` | high |

