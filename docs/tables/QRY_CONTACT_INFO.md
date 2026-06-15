# QRY_CONTACT_INFO

> The QRY_CONTACT_INFO table contains information about the overtime single response data for query records (records in the QRY master file). Each row in the table represents an individual contact for a query record, and each query record itself represents a single query.

**Primary key:** `QUERY_CSN_ID`  
**Columns:** 20  
**Joined by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUERY_ID` | NUMERIC | FK→ | The unique identifier for the query record. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `QUERY_CSN_ID` | NUMERIC | PK | The contact serial number (CSN) of the contact. |
| 4 | `CONTACT_NUM` | INTEGER |  | Contact number to identify the contact in the sequence of contacts. |
| 5 | `PRIM_RECIPIENT_USER_ID` | VARCHAR |  | The unique ID of the user primarily responsible for the query. |
| 6 | `PRIM_RECIPIENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `SENDER_USER_ID` | VARCHAR |  | The sender of this query. |
| 8 | `SENDER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `RESPONDING_USER_ID` | VARCHAR |  | The unique ID of the user that responded to the query. |
| 10 | `RESPONDING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `NLP_STATUS_C_NAME` | VARCHAR |  | The category ID of the user's response to the query. |
| 12 | `NLP_STATUS_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant when the Natural Language Processing (NLP) status changes in UTC. |
| 13 | `EXTERNAL_EVIDENCE` | VARCHAR |  | The external evidence reference resource URL of the query. |
| 14 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Attached) |  | The instant a query record was edited. |
| 15 | `RESOLVE_NOTE_CSN_ID` | NUMERIC |  | The note contact serial number (CSN) that resolves this query. |
| 16 | `RESOLVE_ATTEST_NOTE_CSN_ID` | NUMERIC |  | The attestation line (if any) of the note that resolved the query. |
| 17 | `INSTANT_OF_ENTRY_LOC_DTTM` | DATETIME (Attached) |  | The instant a contact was created in the patient's local time. |
| 18 | `QUERY_SUBJECT` | VARCHAR |  | This item stores the subject line of a query. |
| 19 | `QRY_CONTACT_TYPE_C_NAME` | VARCHAR |  | The type of update to the query. Not currently populated. |
| 20 | `USR_WRKFLW_C_NAME` | VARCHAR |  | This item describes what workflow the user responded to the QRY in. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QUERY_ID` | [QRY_RECORD_INFO](QRY_RECORD_INFO.md) | sole_pk | high |

## Joined in — referenced by (7)

| From | Column | Confidence |
|------|--------|------------|
| [QRY_ADDL_RECIPIENTS](QRY_ADDL_RECIPIENTS.md) | `QUERY_CSN_ID` | high |
| [QRY_ADDL_RESPONSE](QRY_ADDL_RESPONSE.md) | `QUERY_CSN_ID` | high |
| [QRY_EVIDENCE](QRY_EVIDENCE.md) | `QUERY_CSN_ID` | high |
| [QRY_EVIDENCE_NOTE_CSN_ID](QRY_EVIDENCE_NOTE_CSN_ID.md) | `QUERY_CSN_ID` | high |
| [QRY_EVIDENCE_NOTE_IDS](QRY_EVIDENCE_NOTE_IDS.md) | `QUERY_CSN_ID` | high |
| [QRY_SUGGESTION_INFO](QRY_SUGGESTION_INFO.md) | `QUERY_CSN_ID` | high |
| [QUERY_TEXT](QUERY_TEXT.md) | `QUERY_CSN_ID` | high |

