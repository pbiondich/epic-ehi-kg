# INFO_REQUEST_CONTACT

> This table contains a snapshot of information about an individual outreach or response within an Additional Information Request record.

**Primary key:** `INFO_REQ_ID`, `CONTACT_DATE_REAL`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFO_REQ_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the Additional Information Request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `INFO_REQUEST_TX_TYPE_C_NAME` | VARCHAR |  | The Transmission Type of this Additional Information Contact. |
| 4 | `INFO_REQ_TX_DIRECTION_C_NAME` | VARCHAR |  | The Transmission Direction of this Additional Information Contact. |
| 5 | `INFO_REQ_CNCT_SRC_C_NAME` | VARCHAR |  | The Entry Source of this Additional Information Contact. |
| 6 | `CNCT_CREATE_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant this Additional Information Contact was created. |
| 7 | `CNCT_CREATE_DTTM` | DATETIME (Local) |  | The instant this Additional Information Contact was created. |
| 8 | `CNCT_CREATE_USER_ID` | VARCHAR |  | The unique ID of the user who created this Additional Information Contact. |
| 9 | `CNCT_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `INFO_REQUEST_TX_STATUS_C_NAME` | VARCHAR |  | The Transmission Status of this Additional Information Contact. |
| 11 | `GENERATED_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when a notification was generated for this Additional Information Contact. |
| 12 | `GENERATED_DTTM` | DATETIME (Local) |  | The instant when a notification was generated for this Additional Information Contact. |
| 13 | `FILED_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when this Additional Information Contact was filed. |
| 14 | `FILED_DTTM` | DATETIME (Local) |  | The instant when this Additional Information Contact was filed. |
| 15 | `COMM_ID` | VARCHAR | shared | The communication record which documents the communication involved in this Additional Information Contact. |
| 16 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Attached) |  | The UTC instant when this Additional Information Contact was entered. |
| 17 | `INSTANT_OF_ENTRY_UTC_DTTM` | DATETIME (UTC) |  | The instant when this Additional Information Contact was entered. |
| 18 | `IS_CORR_YN` | VARCHAR |  | Indicates if this Additional Information Contact was a correction of a previous contact. |
| 19 | `GUIDELINE_CRITERIA_REVIEW_ID` | NUMERIC |  | The guideline review that was sent to the provider as part of this additional information request, or completed by the provider as part of this additional information response. |
| 20 | `RESPONSE_NEEDED_BY_DATE` | DATETIME |  | Stores the date when the payer is expected to get a response by from the provider. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFO_REQ_ID` | [INFO_REQUEST](INFO_REQUEST.md) | sole_pk | high |

