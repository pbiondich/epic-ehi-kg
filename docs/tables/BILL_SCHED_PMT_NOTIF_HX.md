# BILL_SCHED_PMT_NOTIF_HX

> This table contains the notification history information from the Billing Scheduled Payment (BSP) master file.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIF_HX_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant when the scheduled payment notification was sent to the guarantor. |
| 4 | `NOTIF_HX_DEST_TYPE_C_NAME` | VARCHAR |  | Stores the destination type to which the scheduled payment notification was sent. |
| 5 | `NOTIF_HX_DESTINATION` | VARCHAR |  | Stores the destination to which the scheduled payment notification was sent. It will store the email address or phone number based on the destination type. |
| 6 | `NOTIF_HX_AMT` | NUMERIC |  | Stores the amount for which the notification was sent. |
| 7 | `NOTIF_HX_DTTM` | DATETIME (Local) |  | This column stores the local date and time when the scheduled payment notification was sent to the guarantor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

