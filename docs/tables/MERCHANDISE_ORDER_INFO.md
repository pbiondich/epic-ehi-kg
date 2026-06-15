# MERCHANDISE_ORDER_INFO

> This table contains the order level information of merchandise orders.

**Primary key:** `ORDER_ID`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `MERCH_SUPPLY_ID` | VARCHAR |  | The unique identifier for the merchandise record for the merchandise order. |
| 3 | `MERCH_SUPPLY_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 4 | `MERCH_ORIG_UNIT_PR` | NUMERIC |  | This column contains the original unit price from the merchandise record when the it was sold from the outpatient pharmacy. |
| 5 | `ELIGIBLE_HEALTHCARE_EXPENSE_YN` | VARCHAR |  | Indicates whether merchandise item sold was an eligible healthcare expense at the time of sale, which qualifies it to be paid for with a healthcare expense account such as an FSA, HSA, or HRA. This is applicable only to retail merchandise sales. 'N' or NULL indicate that the merchandise is not considered an eligible healthcare expense. 'Y' indicates that the merchandise is considered an eligible healthcare expense. |
| 6 | `DISPLAY_NAME` | VARCHAR |  | This column contains the display name for the merchandise order. |
| 7 | `PHARMACY_ID` | NUMERIC | FK→ | The unique identifier for the pharmacy record where the merchandise was sold. |
| 8 | `PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 9 | `FEE_TYPE_C_NAME` | VARCHAR | org | For pharmacy fee orders, this is the fee type category ID for the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PHARMACY_ID` | [RX_PHR](RX_PHR.md) | sole_pk | high |

