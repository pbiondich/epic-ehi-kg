# INFO_REQUEST_CNCT_DTR

> Information related to a DTR request.

**Primary key:** `INFO_REQ_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFO_REQ_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the additional information request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `QUESTIONNAIRE_ANSWER_ID` | VARCHAR |  | Stores the questionnaire response record of the questions that were requested or received for this Additional Information Contact. |
| 5 | `AUTHORIZER_CONTEXT_IDENTIFIER` | VARCHAR |  | The DTR Context ID received from the Authorizer responsible for the Auth Request. |
| 6 | `REMAPPED_CONTEXT_IDENTIFIER` | VARCHAR |  | The remapped DTR Context ID sent to the requester of the Auth Request. |
| 7 | `ASSOCIATED_SERVICE_AUTH_ID` | NUMERIC |  | A Service associated with a given DTR Request. If empty, the DTR Request is assumed to apply to all associated Services. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFO_REQ_ID` | [INFO_REQUEST](INFO_REQUEST.md) | sole_pk | high |

