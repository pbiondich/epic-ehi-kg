# ORDER_HOLD_INFO

> This table contains hold related information for orders that were held/unheld.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 24  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | The hold information category ID for an order record, which indicates a type of change to an order's hold status. Holding an order indicates that a medication should not have any doses administered for a specific or indefinite period of time. |
| 4 | `SOURCE_C_NAME` | VARCHAR |  | The order source category ID, indicating where in the EHR the order was held or unheld. |
| 5 | `MAR_SCHD_TIME_SOURCE_C_NAME` | VARCHAR |  | The scheduled time source category ID for the order record that was used when the order was held or unheld. |
| 6 | `MAR_ACTION_C_NAME` | VARCHAR | org | The result category ID for the order record, indicating the action shown in the medication administration record when holding or unholding the order. |
| 7 | `USER_ID` | VARCHAR | FK→ | The unique identifier of the user specified when holding (marking doses that should temporarily not be administered) or this order. |
| 8 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `RECORDED_INSTANT_DTTM` | DATETIME (Local) |  | This column stores the current local instant when the order was held (marking doses that should temporarily not be administered)/unheld. |
| 10 | `HOLD_DURATION` | INTEGER |  | The numeric amount of the duration specified for holding an order. |
| 11 | `HOLD_DURATION_UNIT_C_NAME` | VARCHAR |  | The hold duration unit category ID for the order record. |
| 12 | `REASON_C_NAME` | VARCHAR | org | This column stores the reason specified when holding (marking doses that should temporarily not be administered)/unholding an order. |
| 13 | `COMMENTS` | VARCHAR |  | The comments entered when holding or unholding an order. |
| 14 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 15 | `ORDER_SIGN_ACTION_C_NAME` | VARCHAR |  | The sign action category ID for the order. |
| 16 | `HOLD_START_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant at which this holding action should start. |
| 17 | `HOLD_END_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant at which this holding action should end. |
| 18 | `STOP_TAKING_DATE` | DATETIME |  | The date on which the patient should temporarily stop taking this med - that is, the date of the first dose to skip. |
| 19 | `STOP_TAKING_TIME_OF_DAY_C_NAME` | VARCHAR | org | The category ID for the time of day (morning, bedtime, etc.) when the patient should temporarily stop taking this med - that is, the time of the first dose to skip. |
| 20 | `RESTART_TAKING_DATE` | DATETIME |  | The date on which the patient should restart taking this med - that is, the date of the first dose to take after the pause. |
| 21 | `RESTART_TAKING_TIME_OF_DAY_C_NAME` | VARCHAR |  | The category ID for the time of day (morning, bedtime, etc.) when the patient should restart taking this med - that is, the time of the first dose to take after the pause. |
| 22 | `PAT_COMMENTS` | VARCHAR |  | Comments directed to the patient about an instruction to pause taking this medication. |
| 23 | `HOLD_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This stores the CSN of the encounter where this hold action was taken. |
| 24 | `HOLD_START_STATUS_C_NAME` | VARCHAR |  | Determines how the hold start instant should be interpreted. If this is blank or set to 0 then HOLD_START_UTC_DTTM should be interpreted as is. If this is anything else, HOLD_START_UTC_DTTM will be interpreted differently. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HOLD_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

