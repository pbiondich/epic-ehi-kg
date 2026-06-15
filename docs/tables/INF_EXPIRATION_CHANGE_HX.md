# INF_EXPIRATION_CHANGE_HX

> This table stores changes to the infection expiration date.

**Primary key:** `INFECTION_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFECTION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the infection record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXP_CHANGE_INST_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that a change was made to the infection expiration date. |
| 4 | `EXP_CHANGE_NEW_DATE` | DATETIME |  | The new expiration date set by an expiration date change. |
| 5 | `EXP_CHANGE_TYPE_C_NAME` | VARCHAR |  | The change type category ID for the expiration date change. |
| 6 | `EXP_CHANGE_USER_ID` | VARCHAR |  | The unique ID of the user who changed the expiration date. |
| 7 | `EXP_CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `EXP_CHANGE_ORDER_ID` | NUMERIC |  | The unique ID of the order that changed the expiration date. |
| 9 | `EXP_CHANGE_RULE_ID` | VARCHAR |  | The unique ID of the rule that was evaluated for expiration exceptions that resulted in a change to the expiration date. |
| 10 | `EXP_CHANGE_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 11 | `EXP_CHNG_ALERT_CSN_ID` | NUMERIC |  | The unique alert CSN for the advisory that changed the expiration date. |
| 12 | `EXP_CHANGE_INST_DTTM` | DATETIME (Attached) |  | The local instant that a change was made to the infection expiration date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFECTION_ID` | [INFECTIONS](INFECTIONS.md) | sole_pk | high |

