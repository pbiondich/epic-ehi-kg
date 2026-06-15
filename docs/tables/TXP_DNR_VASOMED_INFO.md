# TXP_DNR_VASOMED_INFO

> This table contains the vasomed administration information for the organ donor.

**Primary key:** `DONOR_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DONOR_ID` | NUMERIC | PK FK→ | The organ donor record id. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DNR_VASOMED_NAME_C_NAME` | VARCHAR | org | The vasomed administered to the donor. |
| 4 | `DNR_VASOMED_AMOUNT` | VARCHAR |  | The amount of vasomed administered to the donor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DONOR_ID` | [TXP_ORGAN_DONOR](TXP_ORGAN_DONOR.md) | sole_pk | high |

