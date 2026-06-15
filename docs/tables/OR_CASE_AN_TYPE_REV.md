# OR_CASE_AN_TYPE_REV

> This table contains anesthesia type review documentation that has been stored on the case. You can use it to link out to ZC_OR_CASE_AN_TYPE_REV for the category value.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AN_TYPE_REV_C_NAME` | VARCHAR | org | The discrete anesthesia type review information that was documented on the surgical case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

