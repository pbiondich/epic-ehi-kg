# PYR_MEAS_OUTCOMES_HX

> This table stores the historical payer calculated outcomes for quality measures that are received from payers.

**Primary key:** `REGISTRY_DATA_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `PROPORTION_OF_DAYS_COVERED_HX` | NUMERIC |  | The historical Proportion of Days Covered (PDC) |
| 5 | `IS_IMPACTABLE_HX_YN` | VARCHAR |  | Indicates if there are enough days left in the measurement year that a fill today could move the patient to meet the adherence threshold. |
| 6 | `IS_FIRST_FILL_HX_YN` | VARCHAR |  | Is this outcome in the First Fill status? This status is where the patient has filled the medication once, but has not filled it a second time. For some measures during this timeframe the patient is not technically in the denominator yet, but once they pick up that second fill they will be. |
| 7 | `INDEX_RX_HX_START_DATE` | DATETIME |  | The prescription start date during the measurement period for a medication adherence measure. This is the start date to use when calculating a Proportion of Days Covered (PDC) value. |
| 8 | `LAST_IMPACTABLE_HX_DATE` | DATETIME |  | The historical last impactable date. After the last impactable date has passed, there are not enough days remaining in the performance period for the patient to meet the measure's proportion of days covered (PDC) goal. |
| 9 | `HYB_SRC_QUALITY_MEAS_OUTCOME_C_NAME` | VARCHAR |  | The category number for the hybrid source outcome. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 10 | `ADMSN_HX_DATE` | DATETIME |  | The admission date for a given encounter-level outcome (currently only used for TRC) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

