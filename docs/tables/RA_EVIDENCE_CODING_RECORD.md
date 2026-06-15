# RA_EVIDENCE_CODING_RECORD

> This table contains data about the evidence linked to coding records for Health Plan Risk Adjustment.

**Primary key:** `CODING_RECORD_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the coding record. |
| 2 | `LINKED_EVIDENCE_C_NAME` | VARCHAR |  | The type of evidence linked to this coding record. |
| 3 | `ASSOC_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The member contact with information on the internal encounter whose diagnosis coding is tracked by this record. |
| 4 | `ASSOC_CLAIM_ID` | NUMERIC |  | The claim record whose diagnosis coding is tracked by this record. |
| 5 | `EVIDENCE_SERVICE_DATE` | DATETIME |  | The date the associated claim or encounter occurred on. |
| 6 | `LAST_TASK_COMPLETION_DATE` | DATETIME |  | The date the latest task associated with this coding record was completed. |
| 7 | `ASSOC_ENC_EVENT_IDENT` | VARCHAR |  | The received document event ID for the external encounter whose diagnosis coding is tracked by this record. |
| 8 | `ASSOC_ATTACHMENT_DOCUMENT_ID` | VARCHAR |  | The attachment whose diagnosis coding is tracked by this record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASSOC_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

