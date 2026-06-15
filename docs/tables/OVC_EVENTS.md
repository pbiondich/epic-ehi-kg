# OVC_EVENTS

> This table contains information about specimen events. This includes information about what the event was, where it occurred, and more. This table was originally used to store submitter information. When looking at the SQL for this table you will see some columns still have "submitter" in their name even though this table now holds container information.

**Primary key:** `CONTAINER_ID`, `EFFECTIVE_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTAINER_ID` | VARCHAR | PK FK→ | The unique ID of the container record. |
| 2 | `EFFECTIVE_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `EVENT_COMMENTS` | VARCHAR |  | The unique ID of the comment that is associated with this event. |
| 5 | `REF_COMM_LOG_ID` | NUMERIC |  | The unique ID of the communication log that is associated with this event. |
| 6 | `EVENT_RESOURCE_ID` | NUMERIC |  | The unique ID of the event resource associated with this event. |
| 7 | `EVENT_RESOURCE_ID_RECORD_NAME` | VARCHAR |  | The name of the node record. |
| 8 | `EVENT_DEST_USER_ID` | VARCHAR |  | The unique ID of the destination user associated with the event. This is not the user who tracked the event. For example, for a "Delivered to Pathologist" event, this would be the pathologist the container was delivered to not the user who delivered the container. |
| 9 | `EVENT_DEST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `EVENT_INSTRUMENT_ID` | VARCHAR |  | The unique ID of the instrument associated with this event. |
| 11 | `EVENT_INSTRUMENT_ID_METHOD_NAME` | VARCHAR |  | The name of the instrument interface, method, method grouper, or middle tier interface record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CONTAINER_ID` | [OVC_DB_MAIN](OVC_DB_MAIN.md) | sole_pk | high |

