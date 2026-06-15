# ORD_MED_PROD_ADMIN

> This table contains product-specific administration instructions. This information is already contained as a part of the table ORD_MED_ADMININSTR so this table does not have to be extracted.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the medication order (prescription) record. NOTE: This is an internal unique identifier for order (ORD) master file records in this table and cannot be used to link to CLARITY_MEDICATION.rd. |
| 2 | `LINE` | INTEGER | PK | The line number for each product-specific administration instruction line. |
| 3 | `MED_PROD_ADMN_INSTR` | VARCHAR |  | Product-specific administration instructions converted to plain text. This item is automatically updated whenever the medication product changes for the given order, either through intelligent medication selection (IMS) for mixtures or by user action. It is automatically appended to item Administration instructions. |
| 4 | `ORDERING_DATE` | DATETIME |  | The date the order was placed in calendar format. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

