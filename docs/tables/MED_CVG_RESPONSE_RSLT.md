# MED_CVG_RESPONSE_RSLT

> This table holds information about medication coverage responses.

**Primary key:** `MED_ESTIMATE_ID`, `CONTACT_DATE_REAL`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_ESTIMATE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the medication estimate record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | Stores contact number. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `RESP_RESULT_C_NAME` | VARCHAR |  | Category value indicating the coverage response result. |
| 8 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Attached) |  | Stores the instant of entry when a record is edited. |
| 9 | `TRIG_UTC_DTTM` | DATETIME (UTC) |  | Holds the instant when the interface message was triggered. |
| 10 | `RESP_UTC_DTTM` | DATETIME (UTC) |  | Holds the instant an interface response was received. |
| 11 | `STATUS_C_NAME` | VARCHAR |  | Holds the category value indicating the interface message status. |
| 12 | `RESP_MSG_ID` | VARCHAR |  | Holds the message ID of the response interface message. |
| 13 | `RESP_EXACT_MATCH_YN` | VARCHAR |  | This item records if the payer sent back coverage information that exactly matched the order details that were sent in the Real-Time Prescription Benefit request. |
| 14 | `ORIG_MED_PA_REQ_C_NAME` | VARCHAR |  | This item holds a category value indicating if prior authorization is required for the medication that was originally ordered. It is calculated when a response is filed based on data stored in the LME 300 group. The value stored here is calculated after considering any PA flag overrides configured for the medication. |
| 15 | `PA_REQ_ACCURACY_C_NAME` | VARCHAR |  | This item tracks the accuracy of the prior authorization flag (I LME 203). Accuracy is determined by looking at the prior authorization status on the linked order. This item will not be populated if Medication Prior Authorization is not enabled for the encounter department (I DEP 17260) or system (I LSD 6670). This item will not be updated for orders if the PA request is started more than 30 days after signing, since the information stored in this record may no longer be accurate. In that case, this item will be set to 3-Unknown. The accuracy flag is calculated using the line where I LME 319-Primary Coverage is set to 1-Yes, and does not consider any PA overrides configured for the medication. |
| 16 | `SIGN_QUERY_TIMEOUT_YN` | VARCHAR |  | If a query was initiated during signing of this order, but results came back after the signing timeout (I LPR 58025 - Patient Estimate Query Signing Timeout), this item will be set to 1-Yes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_ESTIMATE_ID` | [MED_CVG_INFO](MED_CVG_INFO.md) | sole_pk | high |

