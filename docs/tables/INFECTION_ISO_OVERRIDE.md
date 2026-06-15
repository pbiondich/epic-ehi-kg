# INFECTION_ISO_OVERRIDE

> This table contains the current manual override isolations for a given infection.

**Primary key:** `INFECTION_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFECTION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the infection record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVERRIDE_ISOLATION_C_NAME` | VARCHAR | org | The isolation category ID for the manual override of required precautions for the infection. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFECTION_ID` | [INFECTIONS](INFECTIONS.md) | sole_pk | high |

