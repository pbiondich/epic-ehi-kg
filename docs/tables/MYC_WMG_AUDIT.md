# MYC_WMG_AUDIT

> This table contains audit trail items that store information about a message related to the message viewers functionality.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique ID used to identify a web-based chart system message record. A new record is created each time a patient sends a message from a web-based chart system to a system user and each time a system user sends a message to a web-based chart system patient. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WMG_AUD_EVENT_INST` | DATETIME (Attached) |  | Contains the instant of the audit trail entry in local time. |
| 4 | `WMG_AUD_VIEWER_ID` | VARCHAR |  | MyChart ID of the person associated with this audit item |
| 5 | `WMG_AUD_LOCATION_C_NAME` | VARCHAR |  | This is the new location of the message |
| 6 | `WMG_AUD_STATUS_C_NAME` | VARCHAR |  | This is the status (ie: read, unread) of the message |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

