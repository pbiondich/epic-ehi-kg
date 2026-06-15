# CLARITY_CARRIER

> The CLARITY_CARRIER table contains information about the carriers who sponsor your networks and benefit plans.

**Primary key:** `CARRIER_ID`  
**Columns:** 3  
**Joined by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CARRIER_ID` | VARCHAR | PK | The unique ID assigned to the carrier record. |
| 2 | `CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 3 | `CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (7)

| From | Column | Confidence |
|------|--------|------------|
| [CAP_PAYMENT](CAP_PAYMENT.md) | `CARRIER_ID` | high |
| [CAP_PAY_REPL](CAP_PAY_REPL.md) | `CARRIER_ID` | high |
| [CASE_MGMT](CASE_MGMT.md) | `CARRIER_ID` | high |
| [LCI_CONTACT_DATA](LCI_CONTACT_DATA.md) | `CARRIER_ID` | high |
| [MEM_LIST_REPL](MEM_LIST_REPL.md) | `CARRIER_ID` | high |
| [PAT_PER_CARR_ADDR](PAT_PER_CARR_ADDR.md) | `CARRIER_ID` | high |
| [REFERRAL](REFERRAL.md) | `CARRIER_ID` | high |

