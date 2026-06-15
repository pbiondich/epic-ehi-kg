# SPOC_COMM_SENT

> This table contains information about communication sent for a plan of care.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMM_SENT_TYPE_C_NAME` | VARCHAR |  | The communication type category ID for the plan of care. |
| 4 | `COMM_SENT_UTC_DTTM` | DATETIME (UTC) |  | Stores the date the communication was sent |
| 5 | `COMM_SENT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `LETTER_SENT_JOB` | VARCHAR |  | Stores the Job ID of the letter communication sent |
| 7 | `LETTER_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number of the patient encounter in which the letter was sent. |
| 8 | `SENT_COMM_CMT` | VARCHAR |  | The comment associated with the communication sent for the plan of care. |
| 9 | `SENT_COMM_USER_ID` | VARCHAR |  | Stores the user who sent the communication. |
| 10 | `SENT_COMM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `COMM_SENT_PAT_RELATIONSHIP_ID` | NUMERIC |  | Stores the patient contact (RLA ID) who received the communication. Not used for the letter type. |
| 12 | `COMM_SENT_MYPT_ID` | VARCHAR |  | Stores the proxy (WPR ID) who received the communication. Not used for the letter type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LETTER_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

