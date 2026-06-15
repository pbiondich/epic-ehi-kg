# CLM_VALUES_SVC_PROV_ID

> This table contains information for service provider identifiers

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SVC_PROV_IDENT_QUAL` | VARCHAR |  | Type of service provider ID. |
| 4 | `SVC_PROV_IDENT` | VARCHAR |  | Identifier for the service provider/pharmacy. |
| 5 | `SVC_PROV_TAXONOMY` | VARCHAR |  | Stores the taxonomy code of the pharmacy. |
| 6 | `SVC_PROV_FROM_LINE_YN` | VARCHAR |  | This item is set to 1-Yes if the provider is populated by rolling line level provider data up to the header level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

