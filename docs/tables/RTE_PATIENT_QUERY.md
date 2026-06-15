# RTE_PATIENT_QUERY

> This table will contain information about Patient Level Coverage Eligibility Queries. Included in the data is the date and time the query was sent, along with the date and time the response was received. Also included is the Note Record (HNO), the Payor the query was sent to, whether the response was eligible or not, and the action taken upon the response.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RTE_SENT_INST` | VARCHAR |  | The instant the patient-level eligibility query was sent. |
| 4 | `RTE_RCVD_INST` | VARCHAR |  | The instant the patient-level eligibility query's response was received. |
| 5 | `RTE_HNO_ID` | VARCHAR |  | The unique ID of the note (HNO) record for this patient-level eligibility query. |
| 6 | `RTE_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 7 | `RTE_HGEN_NUM` | NUMERIC |  | The hSeq index number for this patient-level eligibility query, corresponding to the global ^HGEN("CVG",hSeq) where query information is stored. |
| 8 | `RTE_RESP_STATUS_C_NAME` | VARCHAR |  | The response status category ID for this patient-level eligibility query. |
| 9 | `RTE_ACTION_C_NAME` | VARCHAR |  | The action taken category ID for this patient-level eligibility query. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

