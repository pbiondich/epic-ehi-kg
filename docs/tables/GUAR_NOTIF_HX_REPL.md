# GUAR_NOTIF_HX_REPL

> This table stores notifications sent to guarantors.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PP_PROPOSED_MONTHLY_AMT` | NUMERIC |  | If the guarantor meets the restrictions for setting up payment plans from MyChart, this column will store the proposed monthly amount that will be shown if they were to sign up for a payment plan. |
| 4 | `PP_PROPOSED_NUM_PMTS` | NUMERIC |  | If the guarantor meets the restrictions for setting up payment plans from MyChart, this column will store the proposed number of payments that will be shown if they were to sign up for a payment plan. |
| 5 | `NOTIF_MYPT_ID` | VARCHAR |  | The unique ID of the MyChart record that the notification was sent to. |
| 6 | `INITIATING_USER_ID` | VARCHAR |  | The user who initiated the notification. |
| 7 | `INITIATING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `AUTHORIZED_INVITEE_NAME` | VARCHAR |  | Stores the authorized user invitee if invitee was invited from self service workflows. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

