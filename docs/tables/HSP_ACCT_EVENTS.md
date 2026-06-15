# HSP_ACCT_EVENTS

> This table contains hospital account events information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The ID number of a hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Since multiple procedure events can be stored in a hospital account, each event will have a unique line number. |
| 3 | `EVENT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `EVENT_DATE` | DATETIME |  | The procedure event date stored in a hospital account. |
| 5 | `EVENT_COMMENT` | VARCHAR |  | A comment associated with a procedure event stored in a hospital account. |
| 6 | `ASA_CLASS` | INTEGER |  | An American Society of Anesthesiologists (ASA) class (numeric) associated with a procedure event stored in a hospital account. |
| 7 | `ANESTH_TYPE_HA_C_NAME` | VARCHAR | org | The anesthesia type associated with a procedure event stored in a hospital account. |
| 8 | `ANESTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `ICU_HOURS` | INTEGER |  | The number of ICU hours associated with the procedure event. |
| 10 | `CCU_HOURS` | INTEGER |  | The number of CCU hours associated with the procedure event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

