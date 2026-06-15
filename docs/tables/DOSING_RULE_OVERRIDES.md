# DOSING_RULE_OVERRIDES

> The overrides that were applied to dosing rules attached to this order.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RULE_OVRD_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant a user overrode dosing rule data |
| 4 | `RULE_OVRD_USER_ID` | VARCHAR |  | The ID of the user that last overrode the dosing rule. |
| 5 | `RULE_OVRD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RULE_OVRD_REASON_C_NAME` | VARCHAR | org | The reason the user provided for overriding the dosing rule. |
| 7 | `RULE_OVRD_RULE_ID_LOCATOR_NAME` | VARCHAR |  | The name of the Locator record. |
| 8 | `RULE_OVRD_RULE_DAT` | NUMERIC |  | The contact date (DAT) of the rule contact that was overridden |
| 9 | `RULE_OVRD_RULE_LINE` | INTEGER |  | The line in the rule that was overridden |
| 10 | `RULE_OVRD_DOSE_VAL` | VARCHAR |  | The dose value at the time of the override |
| 11 | `RULE_OVRD_DS_UNIT_C_NAME` | VARCHAR | org | The dose unit at the time of the override |
| 12 | `RULE_OVRD_FREQ_ID` | VARCHAR |  | The frequency at the time of the override |
| 13 | `RULE_OVRD_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 14 | `RULE_OVRD_FREQ_CNT` | INTEGER |  | The frequency count at the time of the override |
| 15 | `RULE_OVRD_FCNT_C_NAME` | VARCHAR |  | The frequency count type at the time of the override |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

