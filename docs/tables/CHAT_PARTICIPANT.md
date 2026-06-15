# CHAT_PARTICIPANT

> Table containing Secure Chat conversation participants.

**Primary key:** `CONVERSATION_ID`, `LINE`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USER_ID` | VARCHAR | FK→ | The user ID of a user participating in the conversation. |
| 4 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `USER_MYPT_ID` | VARCHAR |  | The patient access account ID of a patient or proxy in the conversation. |
| 6 | `USER_ACTIVE_C_NAME` | VARCHAR |  | This indicates if the participant is considered active in the conversation or not |
| 7 | `LST_READ_UTC_DTTM` | DATETIME (UTC) |  | The time the participant last read a message in the conversation. The time is used to generate read receipts whenever a user opens up the conversation. |
| 8 | `UPDATE_INSTANT_DTTM` | DATETIME (UTC) |  | This indicates the time of the last update that the user would be concerned with. |
| 9 | `LST_READ_MSG_LN` | INTEGER |  | The line number of the message last read by the participant. |
| 10 | `LST_READ_MSG_DAT` | NUMERIC |  | The DAT of the message last read by the participant. |
| 11 | `READ_ALL_MSG_YN` | VARCHAR |  | Flag needed to index conversations with new messages. |
| 12 | `ADDED_FROM_GROUP_YN` | VARCHAR |  | Item used to determine whether or not a user was included in the conversation part of a group instead of being added normally. |
| 13 | `UNREAD_MESSAGE_CNT` | INTEGER |  | The number of unread messages in the conversation for this user. Used to cache unread message counts. |
| 14 | `LAST_IMPORTANT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the last unread important message instant; when a message with a higher than normal priority is sent we set this to the time that the message was sent. |
| 15 | `USER_PRIORITY_C_NAME` | VARCHAR |  | This item stores the priority of the message to display for the user in the Secure Chat conversation list. |
| 16 | `LST_REACTION_LN` | INTEGER |  | Line (of TLK 3500 superitem) of last reaction a user has received for one of their messages. |
| 17 | `LST_REACT_CONTACT_DATE` | DATETIME |  | DAT of last reaction a user has received for one of their messages. |
| 18 | `LST_REACTION_UTC_DTTM` | DATETIME (UTC) |  | Instant of last reaction a user has received for one of their messages. |
| 19 | `LATEST_REACTION_SEEN_UTC_DTTM` | DATETIME (UTC) |  | Instant of latest reaction (by anyone to any message) seen by user |
| 20 | `SHOW_IN_UNREAD_YN` | VARCHAR |  | Indicates whether this conversation should count towards the user in this row of superitem 2000's unread counts. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

