# FAMILY_PATS_STATUS_DATES

> The FAMILY_PATS_STATUS_DATES table contains information about the status change dates for a particular family member within a family.

**Primary key:** `FAMILY_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FAMILY_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the family record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the patient in the family. Together with FAMILY_ID, this forms the foreign key to the FAMILY_PATS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple status dates associated with the family and the patient from the FAMILY_PATS table. |
| 4 | `STATUS_DATE` | DATETIME |  | The date when the family member's status changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAMILY_ID` | [FAMILY](FAMILY.md) | sole_pk | high |

