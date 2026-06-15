# ORDER_VER_TPN_INFO

> This table contains the calculated information about Total Parenteral Nutrition (TPN) after verification.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The Line Count |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date for the order, This should be the date for the verification contact. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | Owner of the verification contact for the order. |
| 6 | `VER_TPN_COMP_C_NAME` | VARCHAR |  | Component for data stored after verification |
| 7 | `VER_TPN_AMOUNT` | NUMERIC |  | Calculated amount for component after verification |
| 8 | `VER_TPN_BASE_UNIT_C_NAME` | VARCHAR | org | Unit for calculated amount after verification |
| 9 | `VER_TPN_AMOUNT_MAX` | NUMERIC |  | If the component has a ranged value, this will be the upper bound |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

