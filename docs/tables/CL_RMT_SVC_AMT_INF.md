# CL_RMT_SVC_AMT_INF

> This table contains service line amount information for a remittance record.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with related remit claim references. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. (Standard for this column type) |
| 3 | `AMT_SVC_LN` | VARCHAR |  | The service line which this amount information refers to. |
| 4 | `SVC_AMT_QUAL_C_NAME` | VARCHAR |  | The amount qualifier code for the claim supplemental information. This is a standard code that indicates what the monetary amount represents. |
| 5 | `SVC_SUPPL_AMT` | NUMERIC |  | Monetary amount for the supplemental claim information. The specific meaning of this amount is indicated by the associated amount qualifier code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

