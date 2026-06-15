# CLARITY_MOD

> This table contains masterfile information on billing modifiers.

**Primary key:** `MODIFIER_ID`  
**Columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MODIFIER_ID` | VARCHAR | PK | The unique id of the modifier record |
| 2 | `MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 3 | `MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [CLM_TX_HX_MODIFIERS](CLM_TX_HX_MODIFIERS.md) | `MODIFIER_ID` | high |
| [HSP_BDC_LINE_MODIFIERS](HSP_BDC_LINE_MODIFIERS.md) | `MODIFIER_ID` | high |
| [ORDER_RAD_MODS](ORDER_RAD_MODS.md) | `MODIFIER_ID` | high |
| [UNIV_CHG_LN_MOD](UNIV_CHG_LN_MOD.md) | `MODIFIER_ID` | high |

