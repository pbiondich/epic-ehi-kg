# ORDER_MED_SIG

> The ORDER_MED_SIG table stores the patient instructions for a prescription as entered by the user. The table should be used in conjunction with the ORDER_MED table which contains related medication, patient, and contact identification information you can report on.

**Primary key:** `ORDER_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this medication order. This is an internal unique identifier for ORD master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `SIG_TEXT` | VARCHAR |  | Patient instructions for the prescription as entered by the user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

