# IP_ORDER_REC

> This table contains Inpatient order reconciliation information.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique ID of the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TAKING_BEF_ADM_C_NAME` | VARCHAR |  | Indicates whether a medication was taken within 24 hours of admission. |
| 4 | `ORDREC_SORT_POC_C_NAME` | VARCHAR | org | This is the Phase of Care that indicates when this action should take place. |
| 5 | `IP_ORDREC_REV_HRS` | FLOAT |  | The number of hours after a completed transfer event that the review not needed status for One Step Order Reconciliation orders is valid. |
| 6 | `IP_ORDREC_REV_EXP_DTTM` | DATETIME (UTC) |  | The time at which the review not needed status for One Step Order Reconciliation orders expires. |
| 7 | `DISCONTINUE_NOTE` | VARCHAR |  | If the reconciliation action (I IEV 1020) indicates a discontinue, this item indicates the note for discontinuation (if one was specified by the user). |
| 8 | `ORDER_REC_HOLD_ACTION_C_NAME` | VARCHAR |  | The provider hold action (hold or unhold) for this action line, if applicable. |
| 9 | `HOLD_INFO_LINE_NUMBER` | INTEGER |  | The line number in the order record that contains additional hold information for this order reconciliation action, if applicable. The values in this column can be linked to the LINE column in the ORDER_HOLD_INFO table. |
| 10 | `ORD_REC_ACT_BUTTON_C_NAME` | VARCHAR |  | The action button category ID for the button used to take this action. This is used to distinguish cases when multiple different buttons can produce the same action in REC_ACTION_C. Currently, this is only populated for actions taken in Transfer Medication Reconciliation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

