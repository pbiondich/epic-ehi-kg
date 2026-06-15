# CLM_VALUES_PRESC_PROV_ID

> This table contains information for prescribing provider identifiers.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROV_IDENT_QUAL` | VARCHAR |  | Type of prescribing provider ID. |
| 4 | `PROV_IDENT` | VARCHAR |  | Prescribing provider identifier. This does not necessarily correspond to a Chronicles Provider ID and should not be used to join to the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

