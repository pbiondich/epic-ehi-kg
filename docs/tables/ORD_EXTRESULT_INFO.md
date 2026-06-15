# ORD_EXTRESULT_INFO

> This table contains information about external ultrasound results that were entered through external result or transcribe workflows.

**Primary key:** `ORDER_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID assigned to the order (ORD .1). |
| 2 | `EXT_RES_EMP_ID` | VARCHAR |  | This column contains the unique ID of the user who has entered the external result for the ultrasound order. Notice that this column may be filled out for ultrasound results without an external order class - that is, orders that were placed internally but resulted by someone who is not charging in Epic using the transcribe workflow. |
| 3 | `EXT_RES_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

