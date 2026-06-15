# ORDER_RAD_ASMT

> This table stores mammography assessment-related information for an order.

**Primary key:** `ORDER_PROC_ID`, `CONTACT_DATE_REAL`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the order record associated with this procedure order. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `ASSESSMENT_C_NAME` | VARCHAR | org | The mammography assessment category number for the order. |
| 4 | `RIGHT_ASMT_C_NAME` | VARCHAR |  | The mammography right assessment category number for the order. |
| 5 | `LEFT_ASMT_C_NAME` | VARCHAR |  | The mammography left assessment category number for the order. |
| 6 | `MAM_OV_ASMT_CALC_YN` | VARCHAR |  | A Boolean value that indicates whether overall assessment is auto-calculated. |
| 7 | `MAM_LT_ASMT_CALC_YN` | VARCHAR |  | A Boolean value that indicates whether left assessment is auto-calculated. |
| 8 | `MAM_RT_ASMT_CALC_YN` | VARCHAR |  | A Boolean value that indicates whether right assessment is auto-calculated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

