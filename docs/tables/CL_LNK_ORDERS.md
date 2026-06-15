# CL_LNK_ORDERS

> The CL_LNK_ORDERS table contains the noadd information about the linked group.

**Primary key:** `LNK_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LNK_ID` | NUMERIC | PK | The unique identifier for the linked order group record. |
| 2 | `PAT_CSN` | NUMERIC | FK→ | This item stores the contact serial number (CSN) of the patient visit associated with this linked order group record. |
| 3 | `LINK_TYPE_C_NAME` | VARCHAR |  | This is the link type of the linked order group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [CL_LNK_CONTACT](CL_LNK_CONTACT.md) | `LNK_ID` | high |
| [CL_LNK_ORDER_IDS](CL_LNK_ORDER_IDS.md) | `LNK_ID` | high |

