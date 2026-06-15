# ORD_SPECIAL_DOSING_INFO

> This table contains special dosing information that is stored in the order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPEC_DOSING_PARAM_C_NAME` | VARCHAR |  | This indicates what type of dosing information is represented by the given row. |
| 4 | `SPEC_AMOUNT` | VARCHAR |  | The dosing parameter amount. This is shared between all dosing parameters and may represent a dose or time. |
| 5 | `SPEC_DOSE_UNIT_C_NAME` | VARCHAR | org | The dose unit category value. This will only populate for rows with an appropriate dosing parameter (Time based units are stored in a different item). |
| 6 | `SPEC_TIME_UNIT_C_NAME` | VARCHAR |  | The category list ID of the unit of time used for this dosing value. |
| 7 | `PARAM_CALC_AMT` | VARCHAR |  | The calculated version of the dosing parameter amount. |
| 8 | `PARAM_CALC_UNIT_C_NAME` | VARCHAR |  | The unit of the calculated amount. |
| 9 | `PARAM_CALC_CALC` | VARCHAR |  | The details on how the calculated dosing information was obtained. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

