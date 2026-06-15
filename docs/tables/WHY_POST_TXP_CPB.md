# WHY_POST_TXP_CPB

> Indicates the reason why the transplant recipient needed to return to cardiopulmonary bypass support after the cardiothoracic transplant surgery.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WHY_POST_TXP_CPB_C_NAME` | VARCHAR | org | Indicates the reason why the transplant recipient needed to return to cardiopulmonary bypass support after the cardiothoracic transplant surgery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

