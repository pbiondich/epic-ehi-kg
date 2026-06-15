# OR_CASE_ALT_REQ_DT_TM

> This stores the surgeons choice of alternate date and time for the surgery.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALTERNATE_REQ_DT` | DATETIME |  | This item contains the surgeon's alternate choice for the date of surgery. |
| 4 | `ALTERNATE_REQ_TM` | DATETIME |  | This item contains the surgeon's alternate choice for the time of surgery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

