# RAD_THERAPY_ASSOC_COURSE

> Lists external radiation courses linked to orders.

**Primary key:** `ORDER_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `RAD_THERAPY_COURSE_SRC_SYS_C_NAME` | VARCHAR |  | This item is for orders representing treatments from courses of radiation documented in third-party software systems. The source system is specified in this item, and the ID of the course is specified in the counterpart Radiation Therapy Course ID (I ORD 77805). |
| 3 | `RAD_THERAPY_COURSE_IDENT` | VARCHAR |  | This item is for orders representing treatments from courses of radiation documented in third-party software systems. The ID of the course is specified in this item, and the source system is specified in counterpart Radiation Therapy Course Source System (I ORD 77800). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

