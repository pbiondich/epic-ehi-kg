# COMM_TRACE_INFO

> This table contains information about communication traces.

**Overflow family:** [COMM_TRACE_INFO_2](COMM_TRACE_INFO_2.md)  
**Primary key:** `COMM_TRACE_ID`, `CONTACT_DATE_REAL`, `CONTACT_SERIAL_NUM`  
**Columns:** 62

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_TRACE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_SERIAL_NUM` | NUMERIC | PK shared | The contact serial number (CSN) of the contact. |
| 3 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `TEMPLATE_SETTING_ID` | NUMERIC |  | Contains the base template that was sent for this trace. |
| 5 | `TEMPLATE_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 6 | `ROOT_TEMPLATE_SETTING_ID` | NUMERIC |  | Contains the root base template sent to start the conversation this trace is a part of. |
| 7 | `ROOT_TEMPLATE_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 8 | `COMM_DIRECTION_C_NAME` | VARCHAR |  | The direction of this trace. |
| 9 | `SENDER_SETTING_ID` | NUMERIC |  | The sender record used to send this trace. |
| 10 | `SENDER_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 11 | `SEGMENT_COUNT` | INTEGER |  | The number of individual messages that the underlying gateway actually sent for this one message. |
| 12 | `COMM_STATUS_C_NAME` | VARCHAR |  | The status of this trace. |
| 13 | `LEGACY_CONTENT_YN` | VARCHAR |  | If the content of this trace came from legacy content that was passed into the cache API, this flag should be set to indicate that this content DID NOT come from ECS build. |
| 14 | `LANGUAGE_ID` | NUMERIC | FK→ | Contains the language that was requested for this trace. |
| 15 | `LANGUAGE_ID_LANGUAGE_NAME` | VARCHAR |  | The language name. If the language is written and uses more than one script to represent it, the name will contain the script in parentheses after the language name. |
| 16 | `RECV_PAT_ID` | VARCHAR | FK→ | If the recipient for the trace has an EPT, this should point to it. |
| 17 | `RECV_ACCOUNT_ID` | NUMERIC |  | If the recipient for the trace has an EAR, this should point to it. |
| 18 | `RECV_PAT_RELATION_ID` | NUMERIC |  | If the recipient for the trace has a RLA, this should point to it. |
| 19 | `RECV_MYPT_ID` | VARCHAR |  | If the recipient for the trace has a WPR, this should point to it. |
| 20 | `ABOUT_PAT_ID` | VARCHAR | FK→ | If this trace was about a specific patient, then this item should point to that patient. Note that the patient need not necessarily be a recipient. |
| 21 | `ABOUT_ACCOUNT_ID` | NUMERIC |  | If this trace was about a specific guarantor, then this item should point to that guarantor. Note that the guarantor need not necessarily be a recipient. |
| 22 | `COMM_CREATE_UTC_DTTM` | DATETIME (UTC) |  | UTC that this trace was created in the database. |
| 23 | `SEND_REQ_UTC_DTTM` | DATETIME (UTC) |  | UTC that this trace was requested be sent. |
| 24 | `TO_CLOUD_UTC_DTTM` | DATETIME (UTC) |  | UTC that this trace was actually sent. |
| 25 | `SEND_EXP_UTC_DTTM` | DATETIME (UTC) |  | UTC time after which this message should NOT be sent. |
| 26 | `DELIVERY_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that that the message was delivered (or as close as we can detect it). |
| 27 | `CLOUD_RECV_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that cloud reports having received this message. |
| 28 | `DB_RECV_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that cache received this message. |
| 29 | `COMM_EXT_NUMBER` | VARCHAR |  | The external number associated with this trace. Data should be stored in E.164 format. The external number is the "to" number when sending from Epic, and the "from" number when receiving a mobile-originated message. |
| 30 | `COMM_INT_NUMBER` | VARCHAR |  | The internal number associated with this trace. Data should be stored in E.164 format. The internal number is the "from" number when sending from Epic, and the "to" number when receiving a mobile-originated message. |
| 31 | `CONTENT_UTF_TEXT` | VARCHAR |  | The content for the trace. This string should be UTF-8 encoded. The cloud foundation API limits characters to 1500. While not a perfect comparison using server logic, this item also uses 1500. A pure W1252 message is capped at 1500. With UTF8 characers taking various numbers of bytes, a UTF8 message may a lower limit, but that would be based on the characters used. |
| 32 | `CLOUD_MSG_IDENT` | VARCHAR |  | The message ID for this trace that was assigned from the cloud/gateway. |
| 33 | `FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 34 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 35 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 36 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 37 | `BUS_SEG_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 38 | `PRIORITY` | INTEGER |  | The priority for this trace. A value from 1-99 (inclusive) where 1 is high and 99 is low. Code should not set arbitrary values, code should use one of the predefined priority buckets using constants, eg: $$ecsConstPriorityMedium(). |
| 39 | `PRE_COMM_WIN_SEND_REQ_UTC_DTTM` | DATETIME (UTC) |  | UTC instant that this trace was requested to be sent before applying communication window restrictions. |
| 40 | `TO_VENDOR_UTC_DTTM` | DATETIME (UTC) |  | UTC instant the status of this trace was updated to PENDING, indicating the message has been passed from cloud to the vendor. |
| 41 | `TO_NETWORK_UTC_DTTM` | DATETIME (UTC) |  | UTC instant the status of this trace was updated to Sent, indicating the message has been passed on to the network. |
| 42 | `FAILURE_UTC_DTTM` | DATETIME (UTC) |  | UTC instant the status of this trace was updated to Failed, indicating the message delivery has failed. |
| 43 | `SORT_INST_UTC_DTTM` | DATETIME (UTC) |  | UTC instant that represents when the message was sent or received. |
| 44 | `RECV_USER_ID` | VARCHAR |  | If the recipient for the trace has an EMP, this should point to it. |
| 45 | `RECV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 46 | `ROOT_WORKFLOW_SETTING_ID` | NUMERIC |  | Contains the root base workflow associated with the template sent to start the conversation this trace is a part of. |
| 47 | `ROOT_WORKFLOW_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 48 | `INT_EMAIL` | VARCHAR |  | The email address used to send a specific email trace: the "from" email address when sending email from Epic. |
| 49 | `COMPUTED_LANGUAGE_ID` | NUMERIC |  | Contains the language that was computed for this trace. |
| 50 | `COMPUTED_LANGUAGE_ID_LANGUAGE_NAME` | VARCHAR |  | The language name. If the language is written and uses more than one script to represent it, the name will contain the script in parentheses after the language name. |
| 51 | `USED_LANGUAGE_ID` | NUMERIC |  | Contains the language that was actually used for this trace. |
| 52 | `USED_LANGUAGE_ID_LANGUAGE_NAME` | VARCHAR |  | The language name. If the language is written and uses more than one script to represent it, the name will contain the script in parentheses after the language name. |
| 53 | `COMM_CHANNEL_C_NAME` | VARCHAR |  | Communication channel used to send this trace. |
| 54 | `VOICE_EVENT_TYPE_C_NAME` | VARCHAR |  | Type of event for a voice call. |
| 55 | `SESS_SUMMARY_STAT_C_NAME` | VARCHAR |  | Summary of the end state of a session. This item will only be populated on the first trace of a session. |
| 56 | `VOICE_CONVERSATION_UID` | VARCHAR |  | Unique ID specifically for the entire conversation. This is different from the call leg ID. |
| 57 | `VOICE_KEYPAD_INPUT` | VARCHAR |  | DTMF (keypad) input from the voice call. |
| 58 | `SESSION_START_UTC_DTTM` | DATETIME (UTC) |  | Stores the time in UTC that a session started. For AI Agent, this item is only populated on the first trace for a conversation. |
| 59 | `CHAT_MESSAGE_CNT` | INTEGER |  | Stores the number of back and forth interactions with the AI Agent. This will only be populated on the initial trace that holds session-related data. |
| 60 | `CLOUD_CHAT_STORAGE_SESSID` | VARCHAR |  | The chat session ID associated with this trace used for retrieving data stored in the chat storage cloud service. |
| 61 | `OVERRIDE_TEMPLATE_SETTING_ID` | NUMERIC |  | Contains the override template record used to send this trace. |
| 62 | `OVERRIDE_TEMPLATE_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ABOUT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `LANGUAGE_ID` | [LANGUAGE](LANGUAGE.md) | sole_pk | high |
| `RECV_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

