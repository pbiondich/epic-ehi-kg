# HL_REQ_SKILLS

> The skills associated with a Logistics Request.

**Primary key:** `HLR_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLR_ID` | NUMERIC | PK shared | The unique identifier for the request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HL_REQ_SKILL_C_NAME` | VARCHAR | org | The skills associated with this Logistics Request. |
| 4 | `HL_SKILL_IS_REQUIRED_YN` | VARCHAR |  | Indicates if the skills associated with this Logistics Request are required. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

