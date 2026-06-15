# BED_DAYS_MATCH

> The BED_DAYS_MATCH table contains bed day information for claims. Different bed day types can have different weights which are applied to the quantity of bed day services to get a converted number of bed days for a referral.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the bed types associated with this claim. Multiple bed types can be associated with this claim. |
| 3 | `BED_DAY_TYPE_ID` | NUMERIC | FK→ | This item stores the ID of the bed day type |
| 4 | `BED_DAY_TYPE_ID_BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |
| 5 | `REL_WT_BED_DAY` | NUMERIC |  | This item stores the relative weight of the bed day type |
| 6 | `BED_DAY_WT` | NUMERIC |  | This item stores the total weight of the bed day type |
| 7 | `BED_DAY_QTY` | NUMERIC |  | This is used to store the quantity of the bed day type services |
| 8 | `BED_DAY_CONV_RFL` | NUMERIC |  | Converted bed days for the bed day type on the referral |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BED_DAY_TYPE_ID` | [CLARITY_BED_DAY](CLARITY_BED_DAY.md) | sole_pk | high |
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

