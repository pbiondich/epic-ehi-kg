# SPEC_IMAGE_MARKING_COUNT

> This stores the type of marker used for specimen collection.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMAGE_MARKING_TYPE_C_NAME` | VARCHAR | org | This stores the type of marker used for specimen collection. |
| 4 | `IMAGE_MARKING_CNT` | INTEGER |  | This stores the number of markers used for a specific marker type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

