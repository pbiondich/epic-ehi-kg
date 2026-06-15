# ADT_SPLIT_ACCT_INTERP_HX

> The ADT_SPLIT_ACCT_INTERP_HX table extracts the history of the reporting interpretations of the Encounter Series billing items for ADT events. This table contains a foreign key to the CLARITY_ADT table for linking to other ADT tables.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `START_INSTANT_DTTM` | DATETIME (UTC) |  | The starting instant for this interpretation. |
| 4 | `END_INSTANT_DTTM` | DATETIME (UTC) |  | The ending instant for this interpretation. |
| 5 | `OUTGOING_FIN_CLASS_EVENT_TYP_C_NAME` | VARCHAR | org | The event type interpretation category for outgoing events for financial class. |
| 6 | `INCOMING_FIN_CLASS_EVENT_TYP_C_NAME` | VARCHAR |  | The event type interpretation category for incoming events for financial class. |
| 7 | `FROM_FINANCIAL_CLASS_C_NAME` | VARCHAR | org | The category number of the financial class that the patient had prior to the event. |
| 8 | `TO_FINANCIAL_CLASS_C_NAME` | VARCHAR |  | The category number of the financial class that the patient had after the event. |
| 9 | `OUTGOING_PAYER_EVENT_TYP_C_NAME` | VARCHAR |  | The event type interpretation category for outgoing events for the payer. |
| 10 | `INCOMING_PAYER_EVENT_TYP_C_NAME` | VARCHAR |  | The event type interpretation category for incoming events for the payer. |
| 11 | `FROM_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 12 | `TO_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 13 | `OUTGOING_PLAN_EVENT_TYP_C_NAME` | VARCHAR |  | The event type interpretation category for outgoing events for the plan. |
| 14 | `INCOMING_PLAN_EVENT_TYP_C_NAME` | VARCHAR |  | The event type interpretation category for incoming events for the plan. |
| 15 | `FROM_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 16 | `TO_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 17 | `PREVIOUS_ENC_EVENT_ID` | NUMERIC |  | This column stores the unique identifier for the event prior to this line's event ID. |
| 18 | `SPLIT_ACCT_HSP_ACCOUNT_ID` | NUMERIC |  | This column stores the unique identifier for the hospital account that was active during this line in the interpretation history. This column is frequently used to link to the HSP_ACCOUNT table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

