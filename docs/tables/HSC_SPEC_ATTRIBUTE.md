# HSC_SPEC_ATTRIBUTE

> This table contains attributes for specimens.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTRIBUTES_C_NAME` | VARCHAR | org | Select attributes of a specimen such as fresh, preserved or gross etc. User can select more than one categories for one specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

