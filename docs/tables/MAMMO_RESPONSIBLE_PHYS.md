# MAMMO_RESPONSIBLE_PHYS

> This table stores information regarding physicians responsible for breast imaging outcomes.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MAMMO_RESP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `PHYS_ASMT_C_NAME` | VARCHAR | org | The overall assessment category ID for the order made by the responsible physician. |
| 5 | `PHYS_RIGHT_ASMT_C_NAME` | VARCHAR |  | The right assessment category ID for the order made by a responsible physician. |
| 6 | `PHYS_LEFT_ASMT_C_NAME` | VARCHAR |  | The left assessment category ID for the order made by a responsible physician. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

