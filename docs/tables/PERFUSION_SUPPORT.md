# PERFUSION_SUPPORT

> Table for the multiple-response Perfusion Mechanical Circulatory Support (I ORG 3110) item.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PERFUSION_SUPPORT_C_NAME` | VARCHAR | org | Indicates the mechanical circulatory support device used to aid perfusion during the transplant surgery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

