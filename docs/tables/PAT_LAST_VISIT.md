# PAT_LAST_VISIT

> This stores the appointment serial numbers for the last time a patient was seen for a given visit type group.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VISIT_TYPE_GROUP_C_NAME` | VARCHAR | org | The visit type group category ID associated with this patient. Used in conjunction with the LAST_VISIT_ASN column to find information about the last visit a patient had for a given type of appointment. |
| 4 | `LAST_VISIT_ASN` | NUMERIC |  | The Appointment Serial Number (ASN) of the most recent visit of a particular group. Use this to link to PAT_ENC.APPT_SERIAL_NO for information about this contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

