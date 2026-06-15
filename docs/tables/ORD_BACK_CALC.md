# ORD_BACK_CALC

> Contains the back-calculated doses for medication orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BACKCALC_DOSE` | VARCHAR |  | This column contains the weight based dose calculated from the entered administration dose and patient weight data. |
| 4 | `BACKCALC_UNIT_C_NAME` | VARCHAR | org | This column stores the dose units for the calculated weight based dose. |
| 5 | `BACKCALC_TYPE_C_NAME` | VARCHAR |  | This column stores the type of weight based dose value used in the calculations for columns BACKCALC_DOSE and BACKCALC_UNIT_C. |
| 6 | `BACKCALC_SIG_LINE` | INTEGER |  | When a medication has differing dosage instructions for specified periods of time this column represents which period the calculated weight based dose applies to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

