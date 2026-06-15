# OR_SPLY

> The OR_SPLY table contains inventory item records.

**Primary key:** `SUPPLY_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUPPLY_ID` | VARCHAR | PK | The internal ID of the inventory item. |
| 2 | `SUPPLY_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 3 | `SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [ARPB_TX_MODERATE](ARPB_TX_MODERATE.md) | `SUPPLY_ID` | high |
| [PRE_AR_CHG](PRE_AR_CHG.md) | `SUPPLY_ID` | high |

