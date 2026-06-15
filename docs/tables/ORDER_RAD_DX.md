# ORDER_RAD_DX

> This table contains diagnoses attached to an imaging order by the reading physician. The diagnoses are used by billing to drop charges.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier of the corresponding Order (ORD) record in the database. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RIS_DIAGNOSES_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

