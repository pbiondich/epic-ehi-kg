# PATIENT_OTH_STADDR

> Contains the Other street address from the patient's Other Address, which can be used by pharmacy to determine where to mail prescriptions. This address is in addition to the patient's home address, the patient's temporary address, and the patient's confidential address. The items in this table are related to the other address items in PATIENT_2 table. Another related table would be the PATIENT_OTH_ADDCOM table which contains the comments that relate to a patient's Other Address.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OTH_STREET_ADDR` | VARCHAR |  | Contains the street address from the patient's prescription Address, which can be used by pharmacy to determine where to mail prescriptions. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

