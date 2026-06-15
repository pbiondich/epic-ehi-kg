# PB_INVOICE_NOTIF_HX

> Stores information related to PB Invoice Notification History.

**Primary key:** `PB_INVC_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_INVC_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the invoice record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STMT_NOTIF_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant when a MyChart/non-MyChart invoice notification was sent to the subscriber. |
| 4 | `STMT_NOTIF_DEST_TYPE_C_NAME` | VARCHAR |  | Stores the destination type to which the invoice notification was sent. |
| 5 | `STMT_NOTIF_DEST` | VARCHAR |  | Stores the destination to which the invoice notification was sent. |
| 6 | `STMT_NOTIF_SETTING_ID` | NUMERIC |  | Stores the pointer to the HST that indicates the type of notification that was sent. |
| 7 | `STMT_NOTIF_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 8 | `STMT_NOTIF_GROUP_SETTING_ID` | NUMERIC |  | Stores the pointer to the parent HST record which represents the type of notification that was sent. |
| 9 | `STMT_NOTIF_GROUP_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |

