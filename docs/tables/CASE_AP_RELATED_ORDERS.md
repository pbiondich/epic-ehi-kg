# CASE_AP_RELATED_ORDERS

> The CASE_AP_RELATED_ORDERS table contains information about other orders related to the Anatomic Pathology case. This information is only populated for legacy data. Newer data is populated in the ORD_LAB_LINKED_ORD table.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_ID` | NUMERIC | discont. shared | The unique ID of an order related to the anatomic pathology case. This information is only populated for legacy data. Newer data is populated in the LAB_LINKED_ORD_ID column of the ORD_LAB_LINKED_ORD table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

