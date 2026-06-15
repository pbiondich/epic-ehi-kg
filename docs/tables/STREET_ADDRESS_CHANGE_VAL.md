# STREET_ADDRESS_CHANGE_VAL

> This table contains a list of street address lines used to store the street address changes for a patient.

**Primary key:** `PAT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated street address change in this patient record. Together with PAT_ID, this forms the foreign key to the STREET_ADDRESS_CHANGE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple street address lines that are associated with the patient and the address change from the STREET_ADDRESS_CHANGE_HX table. |
| 4 | `STREET_ADDRESS` | VARCHAR |  | Audit trail item used to store the previous street address when a new street address is entered or if the current primary address is edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

