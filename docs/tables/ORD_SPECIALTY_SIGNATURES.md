# ORD_SPECIALTY_SIGNATURES

> This table stores information about the required specialties for an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NUM_SIG_REQ_BY_SPECIALTY` | INTEGER |  | This column stores the number of signatures required by a given specialty. |
| 4 | `BILLING_SPECIALTY_YN` | VARCHAR |  | Indicates if providers of the given specialty can also be the billing provider. 'Y' indicates that the provider can also be the billing provider, 'N' or NULL indicates that they can not. |
| 5 | `REQ_SPECIALTIES_C_NAME` | VARCHAR | org | The Reading Physician Roles category ID for the specialties required for resulting the study. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

