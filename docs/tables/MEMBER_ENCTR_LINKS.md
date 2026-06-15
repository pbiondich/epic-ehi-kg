# MEMBER_ENCTR_LINKS

> This table contains links to patient call encounters where member information was updated .

**Primary key:** `BENEFIT_USAGE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BENEFIT_USAGE_ID` | VARCHAR | PK FK→ | The unique ID of the benefit usage record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The date when a benefit was recorded. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date when a membership benefit usage was recorded. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BENEFIT_USAGE_ID` | [MEMBER_INFO](MEMBER_INFO.md) | sole_pk | high |

