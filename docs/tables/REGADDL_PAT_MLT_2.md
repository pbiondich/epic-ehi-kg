# REGADDL_PAT_MLT_2

> The additional registration items are used to store organization specific patient data which is captured during Prelude or ADT workflows. The REGADDL_PAT_MLT_2 table contains the second of three patient level items where a user may enter multiple values.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REGADDL_PAT_MLT_2_C_NAME` | VARCHAR | org | The category number for the second of three additional registration patient level category columns where the user may enter multiple values. The usage of this data element is defined by your organization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

