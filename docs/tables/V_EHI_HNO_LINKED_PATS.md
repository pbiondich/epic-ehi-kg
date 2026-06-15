# V_EHI_HNO_LINKED_PATS

> Placeholder view for HNO EHI data that needs to be marked as both static and dynamic.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_PAT_ID` | VARCHAR | FK→ | The list of patients (EPT) that this HNO is associated with for Electronic Health Information (EHI) Export |
| 4 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LINKED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

