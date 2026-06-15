# LESION_STENOSIS

> The stenosis values of a lesion.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STENOSIS_BRANCH_ID` | INTEGER |  | Stores the lesion branch that the stenosis belongs to. |
| 4 | `PRE_STENOSIS` | INTEGER |  | Stores the pre-intervention stenosis value. |
| 5 | `POST_STENOSIS` | INTEGER |  | Stores the post-intervention stenosis value. |
| 6 | `PRE_STENOSIS_C_NAME` | VARCHAR | org | Stores the pre-intervention stenosis grade. |
| 7 | `POST_STENOSIS_C_NAME` | VARCHAR |  | Stores the post-intervention stenosis grade. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

