# MEDS_REV_HX_LIST

> This table lists the patient's current medications from each time a user reviewed the patient's medications. Reviewing user and other information about each instance of medication review is in the MEDS_REV_HX table. The list of medications at the most recent review instance is in the MEDS_REV_LAST_LIST table. Reviewing user and other information about the most recent review of medications is in the PATIENT table in columns MEDS_LAST_REV_TM, MEDS_LST_REV_USR_ID, and MEDS_LAST_REV_CSN.

**Primary key:** `PAT_ID`, `CONTACT_SERIAL_NUM`, `LINE_COUNT`, `VALUE_COUNT`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `CONTACT_SERIAL_NUM` | NUMERIC | PK shared | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 3 | `LINE_COUNT` | INTEGER | PK | The line number of the associated instance of medication review in the patient's record. Together with PAT_ID, this forms the foreign key to the MEDS_REV_HX table. |
| 4 | `VALUE_COUNT` | INTEGER | PK | The line number of one of the multiple medication orders that are associated with the patient and the instance of medication review from the MEDS_REV_HX table. |
| 5 | `MEDICATION_ORDER_ID` | NUMERIC |  | The unique ID of one of the patient's current medication orders at the time of review. |
| 6 | `TAKING_YN` | VARCHAR |  | Indicates whether the associated medication order was marked as taking at the time of review. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

