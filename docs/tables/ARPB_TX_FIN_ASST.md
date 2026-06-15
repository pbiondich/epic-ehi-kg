# ARPB_TX_FIN_ASST

> Financial Assistance Related Items for Transactions. This table has information that is populated by financial assistance workflows.

**Primary key:** `TX_ID`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `PROGRAM_ID` | NUMERIC | FK→ | The financial assistance program applied on this charge line. |
| 3 | `PROGRAM_ID_PROGRAM_NAME` | VARCHAR |  | The name of the financial assistance program record. |
| 4 | `DISCOUNT_PCT` | NUMERIC |  | The discount percentage applied to this charge line from financial assistance. |
| 5 | `FLAT_FEE_AMT` | NUMERIC |  | The applied flat fee for this charge line from financial assistance. |
| 6 | `MIN_FEE_AMT` | NUMERIC |  | The applied minimum fee on this charge line from financial assistance. |
| 7 | `FEE_SCHEDULE_ID` | NUMERIC | FK→ | The fee schedule on this charge line used to determine the financial assistance discount amount. |
| 8 | `FEE_SCHEDULE_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 9 | `DISCOUNT_AMT` | NUMERIC |  | The discount amount from financial assistance calculations. |
| 10 | `FPL_PCT` | NUMERIC |  | The Federal Poverty Level (FPL) percentage used in financial assistance calculations. |
| 11 | `FIN_ASST_TRACKER_ID` | NUMERIC | FK→ | The unique identifier of the financial assistance tracker that discounted this transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FEE_SCHEDULE_ID` | [CLARITY_FSC](CLARITY_FSC.md) | sole_pk | high |
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |
| `PROGRAM_ID` | [VALUE_BASED_PROGRAM](VALUE_BASED_PROGRAM.md) | sole_pk | high |

