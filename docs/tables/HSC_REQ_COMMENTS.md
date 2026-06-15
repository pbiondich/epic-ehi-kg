# HSC_REQ_COMMENTS

> Holds the specimen requisition comments.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | This column holds the record ID of the specimen record to which the requisition comments belong. |
| 2 | `LINE` | INTEGER | PK | This column holds the line number corresponding to the line of requisition comment. (A requisition comment may be split up into multiple lines depending on the length of the requisition comment). |
| 3 | `REQ_COMMENTS` | VARCHAR |  | This column stores the free text requisition comments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

