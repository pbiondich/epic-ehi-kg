# DENTAL_CLASS_AUDIT

> Audit trail information for the dental classification items.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENT_AUDIT_INS_DTTM` | DATETIME (Local) |  | This item tracks changes to the last edited instant of the dental classification of a patient. |
| 4 | `DENT_AUDIT_COMMENT` | VARCHAR |  | Audit trail of dental class comment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

