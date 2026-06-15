# INFO_REQUEST

> This table contains information about Additional Information Request records. This includes links to the patient, referrals, communications, and documents.

**Primary key:** `INFO_REQ_ID`  
**Columns:** 17  
**Joined by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFO_REQ_ID` | NUMERIC | PK | The unique identifier (.1 item) for the Additional Information Request record. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | The record status of this Additional Information Request (hidden, soft-deleted, etc...) |
| 3 | `EXTERNAL_IDENTIFIER` | VARCHAR |  | The Additional Information Request's external ID number. |
| 4 | `INFO_REQUEST_CONTEXT_C_NAME` | VARCHAR |  | The request context category ID for the Additional Information Request record. |
| 5 | `INFO_REQ_ACTV_USE_STAT_C_NAME` | VARCHAR |  | The active use status category ID for the Additional Information Request record. |
| 6 | `CREATION_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant this Additional Information Request was created. |
| 7 | `CREATION_DTTM` | DATETIME (Local) |  | The instant this Additional Information Request was created. |
| 8 | `LAST_UPD_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant this Additional Information Request was last updated. |
| 9 | `LAST_UPD_DTTM` | DATETIME (Local) |  | The instant this Additional Information Request was last updated. |
| 10 | `COMPLETION_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant this Additional Information Request record was finalized or canceled. |
| 11 | `COMPLETION_DTTM` | DATETIME (Local) |  | The instant this Additional Information Request record was finalized or canceled. |
| 12 | `COMPLETION_USER_ID` | VARCHAR |  | The ID of user who finalized or canceled this Additional Information Request. |
| 13 | `COMPLETION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `INFO_REQ_ORG_ROLE_C_NAME` | VARCHAR |  | The organization role for your organization in this Additional Information Request. |
| 15 | `PAT_ID` | VARCHAR | FK→ | The patient or member around whom all communication in this Additional Information Request is based. |
| 16 | `PA_REFERRAL_ID` | NUMERIC |  | The prior authorization referral record ID which this Additional Information Request belongs to. |
| 17 | `PA_AUTH_REQUEST_ID` | NUMERIC |  | The authorization request ID of the prior authorization which this Additional Information Request belongs to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (7)

| From | Column | Confidence |
|------|--------|------------|
| [INFO_REQUEST_CNCT_DTR](INFO_REQUEST_CNCT_DTR.md) | `INFO_REQ_ID` | high |
| [INFO_REQUEST_CNCT_ERROR](INFO_REQUEST_CNCT_ERROR.md) | `INFO_REQ_ID` | high |
| [INFO_REQUEST_CNCT_NOTES](INFO_REQUEST_CNCT_NOTES.md) | `INFO_REQ_ID` | high |
| [INFO_REQUEST_CONTACT](INFO_REQUEST_CONTACT.md) | `INFO_REQ_ID` | high |
| [INFO_REQUEST_CONTACT_DOCS](INFO_REQUEST_CONTACT_DOCS.md) | `INFO_REQ_ID` | high |
| [INFO_REQ_CNCT_INFO_TYPES](INFO_REQ_CNCT_INFO_TYPES.md) | `INFO_REQ_ID` | high |
| [INFO_REQ_CNCT_REF_NUMS](INFO_REQ_CNCT_REF_NUMS.md) | `INFO_REQ_ID` | high |

