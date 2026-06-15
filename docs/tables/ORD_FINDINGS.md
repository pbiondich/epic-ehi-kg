# ORD_FINDINGS

> This table contains a list of all of the cardiovascular findings associated with the result for this order.

**Primary key:** `ORDER_PROC_ID`, `ORD_DATE_REAL`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique identifier for the order record. |
| 2 | `ORD_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CV_FINDINGS_TYPE_C_NAME` | VARCHAR | org | The findings type category ID of the study finding. |
| 6 | `CV_FINDING_ID` | NUMERIC | FK→ | The unique ID of the study findings associated with this contact. |
| 7 | `ORD_END_DATE_REAL` | FLOAT |  | This is a numeric representation of the end date for each order in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CV_FINDING_ID` | [ORD_CV_FINDING](ORD_CV_FINDING.md) | sole_pk | high |
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

