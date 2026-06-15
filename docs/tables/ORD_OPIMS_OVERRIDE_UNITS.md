# ORD_OPIMS_OVERRIDE_UNITS

> This group of tables stores information about the override that a clinician entered when they chose to not use the products chosen by outpatient Intelligent Medication Selection (IMS). This table stores IMS suggested dose units of the products that were overridden, found in the OPIMS Overridden Suggested Dose Units (I ORD 11605) item.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `COMPONENT_UNITS_C_NAME` | VARCHAR | org | Stores the dose units of the product that the Intelligent Medication Selection (IMS) suggested |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

