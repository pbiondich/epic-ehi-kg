# VALUE_BASED_PROGRAM

> This table stores definitions and settings for value-based programs or contracts.

**Primary key:** `PROGRAM_ID`  
**Columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROGRAM_ID` | NUMERIC | PK | The unique identifier for the program record. |
| 2 | `PROGRAM_ID_RECORD_NAME` | VARCHAR |  | The name of the program record. |
| 3 | `RECORD_NAME` | VARCHAR |  | The name of the program record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [AP_CLAIM_PROGRAM_INFO](AP_CLAIM_PROGRAM_INFO.md) | `PROGRAM_ID` | high |
| [AP_CLM_RX_PROGRAM_INFO](AP_CLM_RX_PROGRAM_INFO.md) | `PROGRAM_ID` | high |
| [ARPB_TX_FIN_ASST](ARPB_TX_FIN_ASST.md) | `PROGRAM_ID` | high |
| [LCI_CONTACT_DATA](LCI_CONTACT_DATA.md) | `PROGRAM_ID` | high |

