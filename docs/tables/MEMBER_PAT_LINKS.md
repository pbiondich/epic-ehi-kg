# MEMBER_PAT_LINKS

> This table contains link(s) to patient record(s) associated with member.

**Primary key:** `BENEFIT_USAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BENEFIT_USAGE_ID` | VARCHAR | PK FK→ | The unique ID of the benefit usage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique patient ID for the member associated with the benefit usage. |
| 4 | `CARD_ISSUED_DATE` | DATETIME |  | The date of the most recent time a card was issued to a member for this benefit usage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BENEFIT_USAGE_ID` | [MEMBER_INFO](MEMBER_INFO.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

