# V_EHI_OVS_EMB_LINKED_PATS

> New view for handling filtering anonymous/deidentified genetic contributors EPT IDs.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GEN_CONTRIB_PAT_ID` | VARCHAR | FK→ | Patients who are genetic contributors to the specimen, i.e. have provided the sperm or egg. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GEN_CONTRIB_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

