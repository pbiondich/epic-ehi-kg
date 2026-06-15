# OR_CASE_REQ_DOCS

> The OR_CASE_REQ_DOCS table contains OR management system case required documents.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of required document information in the case. |
| 3 | `REQ_DOC_COLL_DATE` | DATETIME |  | This column contains the date the required documents were collected. |
| 4 | `REQ_DOC_COLL_TIME` | DATETIME (Local) |  | This column contains the time the required documents were collected. |
| 5 | `REQUIRED_DOCS_ATTRIBUTE_C_NAME` | VARCHAR | org | This item stores the required documents attribute. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

