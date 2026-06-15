# HSP_TX_DIAG_ALT

> This table holds diagnosis codes and qualifiers for a charge that are not from the primary code set configured in the system.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALT_DIAG_CODE_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `ALT_DIAG_QUAL_C_NAME` | VARCHAR | org | The diagnosis code qualifiers that are not from the primary diagnosis code set configured for your facility. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

