# DICOM_AFFECTED_INS

> Table to contain instance-related information when the Modality Performed Procedure Step (MPPS) sends a procedure begin status update.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AFFECTED_INST` | VARCHAR |  | ID of the affected DICOM instance. This is set when the Modality Performed Procedure Step (MPPS) sends a procedure begin status update. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

