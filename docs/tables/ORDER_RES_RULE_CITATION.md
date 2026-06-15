# ORDER_RES_RULE_CITATION

> Stores relevant study documentation for a rule-based finding's citation, sourced from either structured reporting or AI-extracted results.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REL_DOC_RULE_FND` | VARCHAR |  | Stores relevant study documentation for a rule-based finding's citation, sourced from either structured reporting or AI-extracted results. |
| 4 | `AI_EXTRACTED_YN` | VARCHAR |  | Indicates whether the associated study documentation was extracted from AI. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

