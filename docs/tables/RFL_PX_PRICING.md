# RFL_PX_PRICING

> The RFL_PX_PRICING table contains information about the pricing procedures such as total price and patient portion in the referral database.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRICING_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `PRICING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `PRICING_UNITS` | INTEGER |  | Specifies the pricing units. |
| 6 | `PRICING_TOTAL_PRC` | NUMERIC |  | Specifies the pricing total price. |
| 7 | `PRICING_PAT_PORTION` | NUMERIC |  | Specifies the pricing patient portion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

