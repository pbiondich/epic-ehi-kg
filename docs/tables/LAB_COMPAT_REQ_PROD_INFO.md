# LAB_COMPAT_REQ_PROD_INFO

> Each row in this table contains information about a blood product that was requested for a patient.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REQ_PROD_FINDING_ID` | NUMERIC |  | One row represents a result finding record for blood products to be consumed by BPAM matching that need to be associated with a blood product specimen, based on the number of units/volume of blood requested in the prepare order. |
| 4 | `INTENDED_PRODUCT_SPECIMEN_ID` | VARCHAR |  | Each row represents a blood product intended to be assigned to a patient. Details from this blood product should be copied to the result finding record in this row for use in BPAM. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

