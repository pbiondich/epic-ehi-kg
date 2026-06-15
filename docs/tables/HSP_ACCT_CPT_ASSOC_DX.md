# HSP_ACCT_CPT_ASSOC_DX

> This table stores the diagnoses that are linked to a coded Current Procedural Terminology (CPT)/Healthcare Common Procedure Coding System (HCPCS) code on a hospital account.

**Primary key:** `ACCT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the hospital account record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the CPT©/HCPCS code stored on the hospital account to which the diagnoses are linked. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of an associated diagnosis linked to a specific CPT©/HCPCS code on a hospital account. |
| 4 | `CPT_LINKED_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

