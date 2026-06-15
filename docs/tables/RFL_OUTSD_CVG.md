# RFL_OUTSD_CVG

> This table extracts information about coverages received from an outside organization for a referral.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the referral update received from an outside organization. Multiple updates, each containing information about multiple coverages, can be received for a referral. |
| 3 | `OUT_CVG_VALID_INST_DTTM` | DATETIME (UTC) |  | The date and time as of which outside coverages received in a referral update from an outside organization are valid. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

