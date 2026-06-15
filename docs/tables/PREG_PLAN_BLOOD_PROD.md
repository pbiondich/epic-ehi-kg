# PREG_PLAN_BLOOD_PROD

> Blood products that are acceptable to a patient for use during an emergency in labor and delivery (L&D).

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREG_PLAN_BLOOD_PROD_C_NAME` | VARCHAR |  | This item is intended to indicate the types of blood transfusion products that are acceptable to the patient in the case of an emergency, particularly during labor and delivery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

