# CVG_RTE_QUERY

> Table for Eligibility coverage queries.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier of the coverage (CVG) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SENT_INST` | VARCHAR |  | The time an eligibility response was sent. |
| 4 | `RCVD_INST` | VARCHAR |  | The time an eligibility response was received. |
| 5 | `RESP_ID` | VARCHAR |  | The ID of the linked note (HNO) record for the response text. |
| 6 | `RESP_FILED_YN` | VARCHAR |  | This item flags if the response data was filed. |
| 7 | `HGEN_INX` | NUMERIC |  | Index to HGEN global for message info. Packed version of CVG 8550 HGEN INDEX |
| 8 | `PAT_ID` | VARCHAR | FK→ | Record the patient ID of the member for the particular response message. |
| 9 | `QUERY_DATE` | DATETIME |  | A record of the service date queried. |
| 10 | `SENT_TRUE_INST_DTTM` | DATETIME (UTC) |  | The time an eligibility response was sent, in instance format. |
| 11 | `RESPONSE_REG_STATUS_C_NAME` | VARCHAR | org | This contains the verification status associated with a specific RTE (real-time eligibility) Response. |
| 12 | `REALTIME_TX_ID` | NUMERIC |  | Transaction record that stores the coverage level query request and response. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

