# CX_PAT_TRANSITION_TRACKER

> This table contains data for a patient's claims that is tracked for Claims Exchange transition purposes. Each row stores the earliest claim service start date that a patient receives through Claims Exchange for an organization and/or program.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CX_ORGANIZATION_ID` | NUMERIC |  | The payer source organization (DXO) transitioning to Claims Exchange |
| 4 | `CX_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 5 | `CX_PROGRAM_ID` | NUMERIC |  | The contract (VBP) of the payer source organization (DXO) that is transitioning to Claims Exchange. |
| 6 | `CX_PROGRAM_ID_RECORD_NAME` | VARCHAR |  | The name of the program record. |
| 7 | `CX_EARLY_CLAIM_DATE` | DATETIME |  | Earliest claim service start date received for a patient through Claims Exchange from a payer source organization (DXO). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

