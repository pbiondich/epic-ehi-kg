# HSP_BDC_CPT_CODE

> This table contains user-entered Current Procedural Terminology (CPT) code overrides for follow-up records (that is, denials).

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CPT_CODE` | VARCHAR |  | This item stores the user overridden CPT(R) code for the denial. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

