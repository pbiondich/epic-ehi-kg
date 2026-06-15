# ORDER_MED_8

> This table enables you to report on medications ordered. This table should be used with ORDER_MED.

**Overflow of:** [ORDER_MED](ORDER_MED.md)  
**Primary key:** `ORDER_MED_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK | The unique identifier (.1 item) for the order record. |
| 2 | `PA_PRIORITY_C_NAME` | VARCHAR |  | The prior authorization priority category ID for the prior authorization request of medication prescription order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ORDER_MED](ORDER_MED.md).

