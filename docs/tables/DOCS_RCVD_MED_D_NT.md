# DOCS_RCVD_MED_D_NT

> This table stores external medication dispense history received from outside sources.

**Primary key:** `DOCUMENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `GROUP_LINE` | INTEGER | PK | The Line Count |
| 3 | `VALUE_LINE` | INTEGER | PK | The Value Count |
| 4 | `MED_DISP_NOTES` | VARCHAR |  | This item stores the medication dispense notes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

