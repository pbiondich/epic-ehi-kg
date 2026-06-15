# MEDS_REV_LAST_LIST

> This table lists the patient's current medications from the last time a user reviewed the patient's medications. Reviewing user and other information about the most recent review of medications is in the PATIENT table in columns MEDS_LAST_REV_TM, MEDS_LST_REV_USR_ID, and MEDS_LAST_REV_CSN. The list of medications current at each review instance is in the MEDS_REV_HX_LIST table. Reviewing user and other information about each medication's review instance is in the MEDS_REV_HX table.

**Primary key:** `PAT_ID`, `LINE_COUNT`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE_COUNT` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEDICATION_ORDER_ID` | NUMERIC |  | The unique ID of one of the patient's current medication orders at the most recent time of review. |
| 4 | `TAKING_YN` | VARCHAR |  | Indicates whether the associated medication order was marked as taking at the most recent time of review. |
| 5 | `TAKING_ACTION_C_NAME` | VARCHAR |  | This virtual item separates out the taking category from item EPT 17224. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

