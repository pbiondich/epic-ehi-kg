# MED_ADMIN_RESPONSIBILITY

> This table contains rows for each medication administration responsibility assigned for an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESPONSIBILITY_VALUE_C_NAME` | VARCHAR | org | This column stores the medication administration responsibility value set in an encounter that is valid for a given time range. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | This column stores the encounter in which a medication administration responsibility value was set for a given time range. |
| 5 | `DOCUMENTING_UTC_DTTM` | DATETIME (UTC) |  | This column stores the UTC instant at which a medication administration responsibility value was set for a given time range. |
| 6 | `DOCUMENTING_USER_ID` | VARCHAR |  | This column stores the user ID who documented a medication administration responsibility value for a given time range. |
| 7 | `DOCUMENTING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `START_UTC_DTTM` | DATETIME (UTC) |  | This column stores the start instant for a medication administration responsibility value set on an encounter. |
| 9 | `END_UTC_DTTM` | DATETIME (UTC) |  | This column stores the end instant for a medication administration responsibility value set on an encounter. If this is not set, then the responsibility does not have an end instant. |
| 10 | `MAPPED_RESPONSIBILITY_C_NAME` | VARCHAR |  | The medication's mapped administration responsibility for a given time in an encounter. The mapped responsibility is the value that exists in the responsibility mapping configuration at the time the custom responsibilty is set for the order. |
| 11 | `MED_ADMIN_RESP_UPDATE_EVENT_C_NAME` | VARCHAR |  | This column stores the event that saved a medication administration responsibility value set on an encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

