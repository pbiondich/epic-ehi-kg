# IP_PEND_MED_REC

> This table contains Inpatient order reconciliation information for pending orders.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique ID of the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PEND_LINK_TYPE_C_NAME` | VARCHAR |  | Stores the link type of a pended order, for example "AND" if the order is meant to be connected to another specific order. |
| 4 | `PEND_LINK_GROUP` | INTEGER |  | Stores the number of a group of pended orders. This does not link to anything. |
| 5 | `PEND_LINK_GROUP_POS` | INTEGER |  | Stores the number assigned to an order as part of its group. |
| 6 | `PEND_RES_INDI_CMNTS` | VARCHAR |  | Stores the pended comment about indications when a medication is resumed at discharge. |
| 7 | `PEND_DC_NOTE` | VARCHAR |  | Stores the pended note entered by an end user when they mark a medication to be discontinued. |
| 8 | `PEND_ORDER_REC_HOLD_ACTION_C_NAME` | VARCHAR |  | Stores the pended hold or unhold action, if any, for the current line. |
| 9 | `PEND_HOLD_INFO_LINE_NUMBER` | INTEGER |  | The line number in the order record that contains additional hold information for this pended order reconciliation action, if applicable. The values in this column can be linked to the LINE column in the ORDER_HOLD_INFO table. |
| 10 | `ORD_REC_ACT_BUTTON_C_NAME` | VARCHAR |  | The action button category ID for the button used to take this action. This is used to distinguish cases when multiple different buttons can produce the same action in REC_PEND_ACTION_C. Currently, this is only populated for actions taken in Transfer Medication Reconciliation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

