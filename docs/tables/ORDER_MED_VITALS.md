# ORDER_MED_VITALS

> This table stores historical patient vitals information for each medication order at the time the order was released. It should only be used for reporting on whether or not vitals information had been entered at that point in time.

**Primary key:** `ORDER_ID`  
**Columns:** 7  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `WEIGHT_AT_RELEASE` | NUMERIC |  | The patient's recorded weight in kilograms at the time the order was released. |
| 3 | `WEIGHT_REL_SOURCE_C_NAME` | VARCHAR | org | The source category ID for the patient's recorded weight at the time the order was released. |
| 4 | `HEIGHT_AT_RELEASE` | NUMERIC |  | The patient's recorded height in centimeters at the time the order was released. |
| 5 | `HEIGHT_REL_SOURCE_C_NAME` | VARCHAR | org | The source category ID for the patient's recorded height at the time the order was released. |
| 6 | `BSA_AT_RELEASE` | NUMERIC |  | The patient's calculated body surface area (BSA) in meters squared at the time the order was released. |
| 7 | `BSA_REL_SOURCE_C_NAME` | VARCHAR | org | The source category ID for the patient's recorded body surface area (BSA) at the time the order was released. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

