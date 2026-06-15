# PATIENT_OTH_ADDCOM

> Contains comments that relate to a patient's other address, which can be used by pharmacies to determine where to mail prescriptions. The other address is in addition to the patient's home, temporary, and confidential addresses. Related tables with more other address information are PATIENT_2 and PATIENT_OTH_STADDR.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OTH_ADDR_COMMENTS` | VARCHAR |  | Comments that relate to a patient's other address. This address can be used by pharmacies to determine where to mail prescriptions. The other address is in addition to the patient's home, temporary, and confidential addresses. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

