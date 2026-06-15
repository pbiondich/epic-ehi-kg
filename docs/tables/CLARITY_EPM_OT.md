# CLARITY_EPM_OT

> This table contains overtime payer data.

**Primary key:** `PAYOR_ID`, `CONTACT_DATE_REAL`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAYOR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the payor record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `HOME_INFUSION_ENABLE_BFD_YN` | VARCHAR |  | Indicates whether bill for denial is enabled for this payer in Home Infusion workflows. 'Y' indicates bill for denial is enabled. 'N' or NULL indicates it is not enabled. This setting can be overridden at the plan-level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAYOR_ID` | [CLARITY_EPM](CLARITY_EPM.md) | sole_pk | high |

