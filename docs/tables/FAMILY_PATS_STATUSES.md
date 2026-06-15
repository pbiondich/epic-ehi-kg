# FAMILY_PATS_STATUSES

> The FAMILY_PATS_STATUSES table contains information about the status and status history for a particular family member within a family.

**Primary key:** `FAMILY_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FAMILY_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the family record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the patient in the family. Together with FAMILY_ID, this forms the foreign key to the FAMILY_PATS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple statuses associated with the family and the patient from the FAMILY_PATS table. |
| 4 | `FAMILY_PAT_STATUS_C_NAME` | VARCHAR |  | The family member status category ID for the family patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAMILY_ID` | [FAMILY](FAMILY.md) | sole_pk | high |

