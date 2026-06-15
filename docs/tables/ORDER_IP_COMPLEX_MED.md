# ORDER_IP_COMPLEX_MED

> This table contains the data related to Inpatient complex medications that were ordered from Outpatient complex medications.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FROM_OP_CMPLX_MED_TYPE_C_NAME` | VARCHAR |  | This item tracks what type of complex med an IP order was ordered from. This will be blank if it wasn't ordered from one and it is copied forward on reorders/modify. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

