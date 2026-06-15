# MEDS_REV_HX

> This table lists all of the times that a user reviewed a patient's medication list. The list of medications current at each review instance is in the MEDS_REV_HX_LIST table. Reviewing user and other information about the most recent review of medications is in the PATIENT table in columns MEDS_LAST_REV_TM, MEDS_LST_REV_USR_ID, and MEDS_LAST_REV_CSN. The list of medications at the most recent review instance is in the MEDS_REV_LAST_LIST table.

**Primary key:** `PAT_ID`, `LINE_COUNT`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. |
| 2 | `LINE_COUNT` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEDS_HX_REV_INSTANT` | DATETIME (Local) |  | The date and time that the patient's medication list was marked as reviewed. |
| 4 | `MEDS_HX_REV_USER_ID` | VARCHAR |  | The unique ID associated with the user that marked the patient's medication list as reviewed. |
| 5 | `MEDS_HX_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `MEDS_HX_REV_CSN` | NUMERIC |  | The unique contact serial number of the contact in which the patient's medication list was reviewed. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 7 | `MEDS_HX_REV_COUNT` | INTEGER |  | Count of how many meds are found in the medication history review list (I EPT 17229). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

