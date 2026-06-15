# ORD_LAB_CC

> This table includes additional CC List information for recipients from Orders (ORD) items from related group 51105. The Free Text Address (I ORD 51110) and Routing Methods (I ORD 51131) items are included in the tables ORD_LAB_ADDRESS_CC and ORD_LAB_CC_ROUT_METHODS respectively.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CC_COUNTRY_C_NAME` | VARCHAR | org | Country of the address where CCs are sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

