# PAYER_MEM_MATCH

> This table contains rows for each time that a payer has matched this member using the FHIR $member-match or $bulk-member-match operations.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEM_MATCH_CLIENT_IDENT` | VARCHAR |  | The client who performed this member match. |
| 4 | `MEM_MATCH_REQUEST_IDENT` | VARCHAR |  | The Bulk Request ID this member match is part of. |
| 5 | `MEM_MATCH_COVERAGE_ID` | NUMERIC |  | The coverage (CVG) this member match is associated with. |
| 6 | `MEM_MATCH_MATCHED_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant this member match occurred. |
| 7 | `MEM_MATCH_DATA_SENS_C_NAME` | VARCHAR |  | The data sensitivity consent which this member match occurred with. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

