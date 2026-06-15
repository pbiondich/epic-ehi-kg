# CHG_TX_EXPECTED_WRT_OFF

> The write-off amounts for pending financial assistance trackers linked to the charge.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FIN_ASST_TRACKER_ID` | NUMERIC | FK→ | Financial assistance tracker used to calculate expected write-off amounts. |
| 4 | `LAST_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | Instant the write-off amounts were updated for this financial assistance tracker. |
| 5 | `EXPECTED_SELF_PAY_WRITE_OFF` | NUMERIC |  | Self-pay write-off amount the financial assistance tracker would be responsible for writing off if it were to be approved. |
| 6 | `EXPECTED_FIN_ASST_WRITE_OFF` | NUMERIC |  | Financial assistance-specific write-off amount the tracker would be responsible for writing off if it were to be approved. |
| 7 | `FPL_PERCENTAGE` | NUMERIC |  | The federal poverty level (FPL) percentage at the time of the write-off calculation. |
| 8 | `WRITE_OFF_SCENARIO` | VARCHAR |  | The discounting scenario from the financial assistance program that was used for the write-off calculation. |
| 9 | `WRITE_OFF_RULE_ID` | VARCHAR |  | The matching rule for the discounting scenario from the financial assistance program that was used for the write-off calculation. |
| 10 | `WRITE_OFF_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 11 | `WRITE_OFF_LPP_ID` | NUMERIC |  | The discounting extension from the financial assistance program that was used for the write-off calculation. |
| 12 | `WRITE_OFF_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

