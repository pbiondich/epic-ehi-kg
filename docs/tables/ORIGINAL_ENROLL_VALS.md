# ORIGINAL_ENROLL_VALS

> This table stores the per member original value Tapestry Staging Companion (NSC) records.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORIG_VALS_MEM_ID` | VARCHAR |  | This item stores the member that the original values NSC is associated with. |
| 4 | `ORIG_VALS_NSC_ID` | NUMERIC |  | This item stores the original values staging companion for a member. It represents the values as received and loaded from the enrollment source. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

