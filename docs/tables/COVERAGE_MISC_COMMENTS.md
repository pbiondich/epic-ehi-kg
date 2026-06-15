# COVERAGE_MISC_COMMENTS

> Table to extract comments to Clarity from coverage items. This table should not be extracted unless there are attached comments on CVG-495 or CVG-10005. If those items do contain comments, this table should be extracted for EHI compliance.

**Primary key:** `COVERAGE_ID`  
**Columns:** 3  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the coverage record. |
| 2 | `VERIFY_SOURCE_C_CMT` | VARCHAR | org | Column to extract comments for CVG-495 Verification Source. |
| 3 | `TYPE_OF_COVERAGE_C_CMT` | VARCHAR | org | Column to extract comments from CVG-10005 Type of Coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

