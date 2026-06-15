# EPA_PAYER

> Stores payer information associated with electronic prior authorization (ePA) status lines. Each row represents a unique payer information including the payer's source identifier, name, BIN, PCN, and group ID.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EPA_PAYER_ID_LINE` | INTEGER |  | The line number for the payer information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `EPA_PAYER_SRC_IDENT` | VARCHAR |  | The identifier indicating who provided the payer for this row. |
| 5 | `EPA_PAYER_NAME` | VARCHAR |  | The name of the payer associated with this row. |
| 6 | `EPA_PAYER_BIN` | VARCHAR |  | The payer BIN number for this row. |
| 7 | `EPA_PAYER_PCN` | VARCHAR |  | The plan network ID (PCN) for this row. |
| 8 | `EPA_PAYER_GRP_IDENT` | VARCHAR |  | The group ID for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

