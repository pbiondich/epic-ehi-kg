# RX_PHR

> This table contains pharmacy information. Each ADS (such as Pyxis), satellite pharmacy, or main pharmacy should have a record in the table.

**Primary key:** `PHARMACY_ID`  
**Columns:** 3  
**Joined by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PHARMACY_ID` | NUMERIC | PK | The unique ID for this pharmacy. |
| 2 | `PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 3 | `PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (6)

| From | Column | Confidence |
|------|--------|------------|
| [AP_CLM_RX](AP_CLM_RX.md) | `PHARMACY_ID` | high |
| [MED_CVG_DETAILS](MED_CVG_DETAILS.md) | `PHARMACY_ID` | high |
| [MERCHANDISE_ORDER_INFO](MERCHANDISE_ORDER_INFO.md) | `PHARMACY_ID` | high |
| [ORDER_MED](ORDER_MED.md) | `PHARMACY_ID` | high |
| [RX_INTERVENTION](RX_INTERVENTION.md) | `PHARMACY_ID` | high |
| [RX_RXW_CONT_RECV_PHRM](RX_RXW_CONT_RECV_PHRM.md) | `PHARMACY_ID` | high |

