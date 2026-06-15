# HH_VO_NOTIFY

> The HH_VO_NOTIFY table contains a list of users that were chosen to be notified of the order. This is used for workflows where the order is transcribed from a faxed order. The user entering the order can enter other users from the patient's care team to be notified via In Basket that there is a new signed order for the patient.

**Primary key:** `VERBAL_ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERBAL_ORDER_ID` | VARCHAR | PK FK→ | The unique identifier for the verbal order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USERS_TO_NOTIFY_ID` | VARCHAR |  | A list of users who are sent a message when the order is signed. |
| 4 | `USERS_TO_NOTIFY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERBAL_ORDER_ID` | [HH_VO_INFO](HH_VO_INFO.md) | sole_pk | high |

