# QRY_TARGET_INFO

> QRY Table that contains all target code and code sets.

**Primary key:** `QUERY_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUERY_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the query record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QRY_TRGT_GEN_CODESYSTEM_C_NAME` | VARCHAR | org | This item stores the generic code system that, along with QRY 67, determine which condition the QRY is referencing as a documentation suggestion. |
| 4 | `QRY_TARGET_EDG_CODE_SET_C_NAME` | VARCHAR | org | This item stores the diagnosis code set that, along with QRY 67, determine which condition the QRY is referencing as a documentation suggestion. |
| 5 | `QRY_TARGET_CODE` | VARCHAR |  | This item stores the diagnosis code which, along with QRY 65/66, determine which condition the QRY is referencing as a documentation suggestion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QUERY_ID` | [QRY_RECORD_INFO](QRY_RECORD_INFO.md) | sole_pk | high |

