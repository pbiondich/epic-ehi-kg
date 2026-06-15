# RXFILL

> RxFill and adherence information.

**Primary key:** `MED_PRBLM_LIST_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_PRBLM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RXFILL_STATUS_C_NAME` | VARCHAR |  | Stores the status received from the pharmacy's RxFill message. |
| 4 | `RXFILL_DATE` | DATETIME |  | This item stores the date when the RxFill message was generated/received. |
| 5 | `RXFILL_DAYS_DISP` | INTEGER |  | This item stores the number of days for which the medication was dispensed, according to the RxFill message (if the message status is Dispensed) |
| 6 | `RXFILL_ORDER_ID` | NUMERIC |  | Stores a link to the original order for which the RxFill message was sent. |
| 7 | `RXFILL_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 8 | `REFERENCE_NUMBER` | VARCHAR |  | Stores a reference number that uniquely identifies this dispense. |
| 9 | `RXFILL_PHARMACY_ID` | NUMERIC |  | Stores the ID of the pharmacy that sent the RxFill message. |
| 10 | `RXFILL_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_PRBLM_LIST_ID` | [MDL_MD_PRBLM_LIST](MDL_MD_PRBLM_LIST.md) | sole_pk | high |

