# ARPB_TX_RETRO_HX

> Lists the retroadjudication review history.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | Stores whether retroadjudication was accepted or rejected for the transaction. |
| 4 | `ACTION_DATE` | DATETIME |  | Date the charge was accepted or rejected for retroadjudication |
| 5 | `REJECT_REASON_C_NAME` | VARCHAR | org | The reason retroadjudication was rejected for the transaction. |
| 6 | `ACCEPT_REASON_C_NAME` | VARCHAR | org | The reason retroadjudication was automatically accepted for the transaction. |
| 7 | `RETRO_COMMENT` | VARCHAR |  | Free text comment to further describe the retroadjudication event. |
| 8 | `USER_ID` | VARCHAR | FK→ | User responsible for accepting or rejecting retroadjudication |
| 9 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `TRIGGER_DATE` | DATETIME |  | The date when the charge was identified as candidate for retroadjudication. |
| 11 | `TRIGGER_USER_ID` | VARCHAR |  | Stores a reference to the last user to make changes that caused the charge to be a candidate for retroadjudication. |
| 12 | `TRIGGER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `ACTION_TIME` | DATETIME (Local) |  | Time the charge was accepted or rejected for retroadjudication. |
| 14 | `MANUAL_REASON_C_NAME` | VARCHAR | org | The retroadjudication reason category ID selected in account maintenance for the transactions. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

