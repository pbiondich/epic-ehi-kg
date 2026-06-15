# CLM_VALUES_PAT_IDENT

> This table contains information for patient identifiers.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_IDENT_QUAL` | VARCHAR |  | The type of patient ID being reported. |
| 4 | `PAT_IDENT` | VARCHAR |  | Patient identifier. This does not necessarily correspond to a Chronicles Patient ID and should not be used to join to the PATIENT table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

