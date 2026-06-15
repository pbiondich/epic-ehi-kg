# ORGAN_DONOR_RISK_CRITERIA

> The list of criteria that caused the organ donor to be considered an increased risk for blood-borne disease transmission.

**Primary key:** `DONOR_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DONOR_ID` | NUMERIC | PK FK→ | The organ donor's record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DNR_RISK_CRITERIA_C_NAME` | VARCHAR | org | A criterion that caused the donor to be considered an increased risk for blood-borne disease transmission. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DONOR_ID` | [TXP_ORGAN_DONOR](TXP_ORGAN_DONOR.md) | sole_pk | high |

