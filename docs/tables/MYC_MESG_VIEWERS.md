# MYC_MESG_VIEWERS

> This table contains the viewers that may see a message, as well as information about the message as it pertains to each viewer, such as the location, like Inbox or Sent, and status, like read or unread. Viewers are defined by Patient Access Accounts (WPR) records.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique ID used to identify a web-based chart system message record. A new record is created each time a patient sends a message from a web-based chart system to a system user and each time a system user sends a message to a web-based chart system patient. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VIEWER_WPR_ID` | VARCHAR |  | This is the ID of the MyChart user who may view the message |
| 4 | `MSG_LOCATION_C_NAME` | VARCHAR |  | This indicates the location of the message for the particular viewer |
| 5 | `MSG_STATUS_C_NAME` | VARCHAR |  | This indicates the status of the message for a particular viewer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

