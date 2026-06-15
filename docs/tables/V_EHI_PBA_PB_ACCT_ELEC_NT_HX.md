# V_EHI_PBA_PB_ACCT_ELEC_NT_HX

> This table stores the history of electronic notifications for the premium billing account.

**Primary key:** `PB_ACCT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACCT_ID` | VARCHAR | PK FK→ | The unique identifier for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIF_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant when the notification was sent about the premium billing account. |
| 4 | `NOTIF_DEST_TYPE_C_NAME` | VARCHAR |  | Stores the destination type to which the notification was sent. |
| 5 | `NOTIF_DEST` | VARCHAR |  | Stores the destination to which the notification was sent. |
| 6 | `NOTIF_SETTING_ID` | NUMERIC |  | Stores the type of the generic settings notification that was sent. |
| 7 | `NOTIF_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 8 | `NOTIF_GROUP_SETTING_ID` | NUMERIC |  | Stores the unique id of the parent generic settings record which represents the type of notification that was sent. |
| 9 | `NOTIF_GROUP_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

