# COMM_TRACE_EMAIL_RECPNTS

> This table stores information about addresses that an email was sent to as well as the person records associated with that address.

**Primary key:** `OUTREACH_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `COMM_CONTACT_ID` | NUMERIC |  | The unique identifier for the communication contact record associated with the external email addresses that an email will be sent to. |
| 5 | `EMAIL_ADDR_RECPNT_TYP_C_NAME` | VARCHAR |  | The recipient type for a specific email address receiving the email. |
| 6 | `PAT_ID` | VARCHAR | FK→ | The unique identifier for the patient associated with a person receiving an email. |
| 7 | `MYPT_ID` | VARCHAR | shared | The unique identifier for the MyChart user associated with the person receiving the email. |
| 8 | `ACCT_ID` | NUMERIC | shared | The unique identifier for the guarantor associated with the person receiving the email. |
| 9 | `PAT_RELATIONSHIP_ID` | NUMERIC | FK→ | The unique identifier for the patient relationship associated with the person receiving the email. |
| 10 | `USER_ID` | VARCHAR | FK→ | The unique identifier for the user associated with the person receiving the email. |
| 11 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `COMM_ACTION_STATUS_C_NAME` | VARCHAR |  | The status of the email for this recipient. |
| 13 | `NUM_TEMP_FAILURES` | INTEGER |  | The number of times an email temporarily failed to deliver before reaching a final status. |
| 14 | `MARKED_SPAM_YN` | VARCHAR |  | Whether this recipient marked the email as spam. |
| 15 | `STATUS_UTC_DTTM` | DATETIME (UTC) |  | UTC instant the status event (I RCH 85617) occurred for this recipient. |
| 16 | `STATUS_LOCAL_DTTM` | DATETIME (Local) |  | Local instant the status event (I RCH 85617) occurred for this recipient. |
| 17 | `EMAIL_ADDR_LEGACY_EXT` | VARCHAR |  | This item stores the external email address of the recipient when we bridge to legacy email sending via the SMTP server. This item will not be populated on traces sent via Hello World Email. For email recipient information on Hello World traces, see COMM_TRACE_EMAIL_RECPNTS.COMM_CONTACT_ID (links to CCR record). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OUTREACH_ID` | [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

