# IP_POST_MED_REC_ORDERS

> This table stores inpatient medication orders that were signed and/or released after discharge medication reconciliation was already complete for that admission, along with information about whether and why the signing user was shown the Reconciliation on the Fly prompt and how they responded to it.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `POST_REC_ORDER_ID` | NUMERIC |  | The unique ID of the order that was signed after discharge order reconciliation had been completed. |
| 4 | `OTF_EVENT_LINE_NUM` | INTEGER |  | The line number of the event that was filed when this order was signed. Together with EVENT_ID, this forms the foreign key to the ED_IEV_EVENT_INFO table. |
| 5 | `PROMPT_SHOWN_C_NAME` | VARCHAR |  | The category ID indicating whether the user was prompted to reconcile the order for discharge prior to signing it, and what options, if any, were present in that prompt. |
| 6 | `PROMPT_REASON_C_NAME` | VARCHAR |  | The category ID for the reason why the user wasn't shown the full prompt to reconcile this order for discharge. This is NULL if the user saw the full prompt. |
| 7 | `PROMPT_RESPONSE_C_NAME` | VARCHAR |  | The category ID for the action, if any, that the user took on the prompt to reconcile this order for discharge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

