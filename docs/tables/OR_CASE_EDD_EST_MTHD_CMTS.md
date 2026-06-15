# OR_CASE_EDD_EST_MTHD_CMTS

> The OR_CASE_EDD_EST_MTHD_CMTS table contains free text associated with the methods and criteria used to determine the estimated date of delivery (EDD).

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EDD_ESTIMATION_METHOD_CMTS` | VARCHAR |  | This item stores free text associated with the methods and criteria used to determine the estimated date of delivery (EDD). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

