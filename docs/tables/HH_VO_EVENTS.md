# HH_VO_EVENTS

> Contains Home Health verbal order events information.

**Primary key:** `VERBAL_ORDER_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERBAL_ORDER_ID` | VARCHAR | PK FK→ | The unique identifier for the verbal order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EVENT_TYPE_C_NAME` | VARCHAR | org | Verbal order event type. Types are: submit, received signature, sent to physician, replied with changes. Links to category table ZC_LVO_EVENT_TYPES. |
| 4 | `EVENT_DATE` | DATETIME (Local) |  | Verbal order event date. |
| 5 | `EVENT_USER_ID` | VARCHAR |  | User ID of user who created verbal order event. Links to table CLARITY_EMP. |
| 6 | `EVENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `EVENT_COMMENT` | VARCHAR |  | Text of the verbal order event comment entered by the user. |
| 8 | `EVENT_PROVIDER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `EVENTS_ORDER_HX` | VARCHAR |  | This item contains the order history for the verbal order. |
| 10 | `EVENT_STATUS_C_NAME` | VARCHAR |  | This item stores the status that this order was changed to when this event occurred. |
| 11 | `EVENT_RCV_SIGN_DATE` | DATETIME |  | Date on which signature was received from the provider. |
| 12 | `EVENT_NOTE_CSN_ID` | NUMERIC |  | The unique contact serial number of the note contact that is associated with the verbal order event. |
| 13 | `EVENT_DOCUMENT_ID` | VARCHAR |  | The document that was linked or unlinked in this event. The document contains information pertaining to this Home Care Order. A document can be linked to a signed order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERBAL_ORDER_ID` | [HH_VO_INFO](HH_VO_INFO.md) | sole_pk | high |

