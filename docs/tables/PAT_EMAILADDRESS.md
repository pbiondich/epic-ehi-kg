# PAT_EMAILADDRESS

> This table stores the patient's email addresses.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | Internal ID of the patient (.1 record ID) |
| 2 | `LINE` | INTEGER | PK | The Line Count. Each line stores one of the patient's e-mail addresses. |
| 3 | `EMAIL_ADDRESS` | VARCHAR |  | Email address for this patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

