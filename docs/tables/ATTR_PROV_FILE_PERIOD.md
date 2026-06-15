# ATTR_PROV_FILE_PERIOD

> Contains a list of changes to a patient's attributed provider over time. The current values are also stored in the ATTRIBUTED_PROVIDER table.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTR_PROV_TYPE_C_NAME` | VARCHAR | org | The type of attributed provider added. |
| 4 | `ATTR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `ATTR_START_DATE` | DATETIME |  | The effective date of the provider attribution period. |
| 6 | `ATTR_END_DATE` | DATETIME |  | The termination date of the provider attribution period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

