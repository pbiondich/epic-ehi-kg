# SPEC_MARKER_INFO

> This table stores information about markers used on specimens.

**Primary key:** `HSC_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSC_ID` | NUMERIC | PK | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPECIMEN_MARKER_LENGTH_C_NAME` | VARCHAR | org | This item is used to document the length of a marker used on a specimen |
| 4 | `SPECIMEN_MARKER_TYPE_C_NAME` | VARCHAR | org | This item stores the type of marker used on a specimen. |
| 5 | `SPECIMEN_MARKER_LOCATION_C_NAME` | VARCHAR | org | This item stores the location on a specimen where a marker was used. |
| 6 | `SPECIMEN_MARKER_ORIENTATION_C_NAME` | VARCHAR | org | This item stores the orientation of a marker used on a specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

