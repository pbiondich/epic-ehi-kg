# DENTAL_RES_DX_HX_RM

> This table extracts the related multiple response Dental: Associated Diagnoses History (I RES 17519) item.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the dental procedure record. Together with FINDING_ID, this forms the foreign key to the DENTAL_RES_DX_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple diagnoses associated with the procedure and the historical instant from the DENTAL_RES_DX_HX table |
| 4 | `DENTAL_DX_HX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

