# BLOOD_REQTS_VALS_AUDIT

> This table extracts the related multiple response Blood Special Requirements - Audit Trail (I EPT 18017) item, which stores the audit trail of blood special requirements for the patient. It contains the current values as well as all previous values for this patient.

**Primary key:** `PAT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated instance of editing blood special requirements in the patient's record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of multiple edited pieces of information associated with the patient and the editing instance. |
| 4 | `BLOOD_SPECIAL_REQTS_C_NAME` | VARCHAR | org | Stores all previously recorded values for special requirements that should be applied to blood orders for this patient |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

