# CLARITY_FSC

> This table contains basic information about the fee schedules billing system uses to adjudicate the price of a charge and manage care system AP Claims and Referrals used to price procedures based on the composition of the vendor-network contracts.

**Primary key:** `FEE_SCHEDULE_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FEE_SCHEDULE_ID` | NUMERIC | PK | This column stores the unique identifier for the fee schedule record. |
| 2 | `FEE_SCHEDULE_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 3 | `FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [ARPB_TX_FIN_ASST](ARPB_TX_FIN_ASST.md) | `FEE_SCHEDULE_ID` | high |

