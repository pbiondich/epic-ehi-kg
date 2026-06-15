# CV_CHILD_RES

> Table to contain child results for any parent result. Each result can have multiple child results. For example, documentation on main vessel will create parent result record while documenting on lesion or collateral will create child result record for that parent result.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHILD_RES_ID` | NUMERIC |  | Indicates the result ID. Each result could have multiple child result records. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

