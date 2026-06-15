# OR_LOG_ABSTR_INFO

> This table stores information related to documentation where abstraction elements were identified during procedure documentation.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ABSTRACT_ELEM_C_NAME` | VARCHAR | org | Related group 9700 is used to document where an abstracting user found information pertaining to particular data points for a quality initiative (e.g. SCIP). They are for informational use only and are not extracted as part of any quality measures. This item is used to indicate a specific data point. |
| 4 | `ABSTRACT_COMMENTS` | VARCHAR |  | Related group 9700 is used to document where an abstracting user found information pertaining to particular data points for a quality initiative (eg. SCIP). They are for informational use only and are not extracted as part of any quality measures. This item is used to indicate additional information about a specific data point. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

