# ORDER_SUPPLY

> This table stores information about the supplies and drugs associated with an order.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of supplies & drugs associated with an order. |
| 3 | `CHARGE_WASTED_YN` | VARCHAR |  | Indicates whether to charge for wasted supplies associated with this order. 'Y' indicates wasted supplies should be charged. |
| 4 | `DRUG_DOSE` | NUMERIC |  | The dose value (a number) of drugs used in imaging procedure. |
| 5 | `DRUG_DOSE_UNIT_C_NAME` | VARCHAR | org | The dose unit category number for drugs used in imaging procedures. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

