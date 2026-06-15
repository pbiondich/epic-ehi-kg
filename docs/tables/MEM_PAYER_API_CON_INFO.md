# MEM_PAYER_API_CON_INFO

> The MEM_PAYER_API_CON_INFO table contains information about a member's consent status and history relating to the Payer-to-Payer Access API.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAYER_API_CONSENT_C_NAME` | VARCHAR |  | This item stores the member's current consent status for the Payer-to-Payer data sharing API. |
| 4 | `CONSENT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the time a change in consent status was recorded for the Payer-to-Payer Access API. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

