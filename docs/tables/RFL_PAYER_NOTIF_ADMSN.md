# RFL_PAYER_NOTIF_ADMSN

> This table contains information about notifications of admissions associated with an encounter.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTF_MSG_TYPE_C_NAME` | VARCHAR |  | The type of admission notification sent to the payer organization. |
| 4 | `NOTIF_MSG_SENT_UTC_DTTM` | DATETIME (UTC) |  | The sent instant (in UTC) for the specified payer notification message. |
| 5 | `NOTIF_MSG_REC_UTC_DTTM` | DATETIME (UTC) |  | The instant (in UTC) for the notification response received from the payer notification message that was previously sent. |
| 6 | `NOTF_MSG_STATU_C_NAME` | VARCHAR |  | The status for the payer notification message, including Sent, Processed, Error, Manually Resolved, etc. |
| 7 | `NOTIF_REF_NUM` | VARCHAR |  | The reference number associated to the payer notification message. |
| 8 | `NOTIF_ADT_SOURCE_C_NAME` | VARCHAR |  | The source of how Notice of Admission filed utilization management data into the referral. |
| 9 | `NOTIF_ADT_SOURCE_ORG_ID` | NUMERIC |  | The source organization of the Notice of Admission notification. |
| 10 | `NOTIF_ADT_SOURCE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

