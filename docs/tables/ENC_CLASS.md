# ENC_CLASS

> This table contains the classifications for a given encounter. For example, an encounter may be a drug study and restricted at the same time. The category is customer-defined and is multiple response overtime.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 2 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 3 | `LINE` | INTEGER | PK | The line number of the current encounter classification. |
| 4 | `ENC_CLASS_C_NAME` | VARCHAR | org | This item delineates the classifications that describe this encounter. For example, it may be a drug study and restricted. This is a customer-defined multiple response overtime category. |
| 5 | `CONTACT_DATE` | DATETIME |  | The contact date of the encounter associated with this encounter class. Note: There may be multiple encounters on the same calendar date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

