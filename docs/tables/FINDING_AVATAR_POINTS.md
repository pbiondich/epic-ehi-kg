# FINDING_AVATAR_POINTS

> Avatar documentation for endoscopy findings records.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FINDING_POINT_AVATAR_C_NAME` | VARCHAR |  | The avatar type category ID for the finding. |
| 4 | `FINDING_POINT_REGION_ID` | NUMERIC |  | The unique ID of the anatomical region (VEL) this point is associated with. |
| 5 | `FINDING_POINT_REGION_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 6 | `FINDING_POINT_LOCATION` | VARCHAR |  | The exact x/y location of the point in the format "x,y", with x and y as decimals. |
| 7 | `FINDING_POINT_LAYER` | VARCHAR |  | The layer on the avatar where this point exists. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

