# PAT_FHIR_MERGE_UNMERGE_HX

> This table contains history of merge/unmerge info received via FHIR from another organization.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RCVD_UTC_DTTM` | DATETIME (UTC) |  | The instant of update when merge/unmerge info is received. |
| 4 | `ORG_IDENTIFIER` | VARCHAR |  | The unique identifier for an organization that sent merge/unmerge information for the patient. |
| 5 | `SRC_PAT_FHIR_IDENTIFIER` | VARCHAR |  | Other organization's original source patient FHIR ID. |
| 6 | `MERGE_UNMERGE_UTC_DTTM` | DATETIME (UTC) |  | Other organization's merge/unmerge event instant for this patient. |
| 7 | `MERGE_ACTION_TYPE_C_NAME` | VARCHAR |  | Other organization's merge/unmerge action type for this patient. |
| 8 | `RVCD_DTTM` | DATETIME (Local) |  | The instant of update when merge/unmerge info is received in the local time. |
| 9 | `MERGE_UNMERGE_DTTM` | DATETIME (Local) |  | Other organization's merge/unmerge event instant for this patient in the local time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

