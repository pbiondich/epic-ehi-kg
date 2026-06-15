# OR_ESU_PSTSKIN_CND

> The OR_ESU_PSTSKIN_CND table stores the condition of the skin after the placement of the ESU grounding pad.

**Primary key:** `LINE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE_ID` | VARCHAR | PK | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GRND_PAD_PSTSKIN_C_NAME` | VARCHAR | org | The category number for skin conditions after placing the ESU grounding pad. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

