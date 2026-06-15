# PPS_SPS_UID

> DICOM Performed Procedure Step Scheduled Procedure Step information.

**Primary key:** `IMY_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier for the modality data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PPS_SPS_UID` | VARCHAR |  | The DICOM Scheduled Procedure Step IDs associated with this Performed Procedure Step. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

