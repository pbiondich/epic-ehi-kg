# ORGAN_DNR_CITIZENSHIP

> This table contains the organ donor's citizenship information.

**Primary key:** `DONOR_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DONOR_ID` | NUMERIC | PK FK→ | The organ donor record id. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DNR_CITIZENSHIP_C_NAME` | VARCHAR | org | Specifies the donor's citizenship. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DONOR_ID` | [TXP_ORGAN_DONOR](TXP_ORGAN_DONOR.md) | sole_pk | high |

