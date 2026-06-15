# HH_OASIS_DATA

> Contains information for Home Health Outcome and Assessment Information Set (OASIS) data sets.

**Primary key:** `OASIS_SET_ID`, `CONTACT_DATE_REAL`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK FK→ | Unique identifier for the OASIS data set. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | Unique identifier for this contact for this patient. |
| 3 | `MASKED_PAT_FNAME` | VARCHAR |  | Masked OASIS patient first name. |
| 4 | `MASKED_PAT_LNAME` | VARCHAR |  | Masked OASIS patient last name. |
| 5 | `MASK_MEDICARE_NUM` | VARCHAR |  | Masked OASIS Medicare number. |
| 6 | `MASK_MEDICAID_NUM` | VARCHAR |  | Masked OASIS Medicaid number. |
| 7 | `HH_PPS_EPSD_RATE` | NUMERIC |  | This item stores the assessment-based Prospective Payment System (PPS) episode payment rate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OASIS_SET_ID` | [HH_OASIS_INFO](HH_OASIS_INFO.md) | sole_pk | high |

