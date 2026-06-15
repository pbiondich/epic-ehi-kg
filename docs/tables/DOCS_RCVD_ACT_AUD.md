# DOCS_RCVD_ACT_AUD

> This table contains data on actions that a user took on a direct message. For example, information about linking messages to patients, routing and creating referrals are all discretely audited in this table.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MSG_ACT_C_NAME` | VARCHAR |  | Contains granular actions that were performed on a Provide and Register message (or incoming group of external documents). Such actions may include how the patient was linked to the message, routing, and referral creation that occurred. These actions are shown to the user on an audit trail on the Incoming Messages Report or the International Review Report. |
| 6 | `MSG_ACT_CMT` | VARCHAR |  | Contains comments for actions that were performed on a Provide and Register message (or incoming group of external documents). Such actions may include how the patient was linked to the message, routing, and referral creation that occurred. These actions are shown to the user on an audit trail on the Incoming Messages Report or the International Review Report. Comments can be user entered or hard coded. |
| 7 | `MSG_ACT_UTC_DTTM` | DATETIME (UTC) |  | Contains the time of actions that were performed on a Provide and Register message (or incoming group of external documents). Such actions may include how the patient was linked to the message, routing, and referral creation that occurred. These actions are shown to the user on an audit trail on the Incoming Messages Report or the International Review Report. |
| 8 | `MSG_ACT_EXTERNAL_ORDER_UID` | VARCHAR |  | This item contains the identifier of an external order associated with an event such as receiving an interface message to place an order, to update an order, or to cancel an order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

