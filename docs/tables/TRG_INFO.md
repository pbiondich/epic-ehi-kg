# TRG_INFO

> This table stores treatment day or pathway step information that is contact-independent, such as the treatment day/pathway step status, the reason for canceling or deferring the day/step, the ID of the treatment plan (TPL) record that contains this treatment day or the ID of the pathway (TPL) record that contains this step, etc.

**Primary key:** `REGIMEN_ID`  
**Columns:** 14  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The treatment day ID. |
| 2 | `REGIMEN_NAME` | VARCHAR |  | The name of the treatment day in this row. |
| 3 | `DEFER_DAY_RSN_C_NAME` | VARCHAR | org | The reason for deferring the treatment day in this row. |
| 4 | `CANCEL_DAY_RSN_C_NAME` | VARCHAR | org | The reason for canceling the treatment day in this row. |
| 5 | `STATUS_COMMENTS` | VARCHAR |  | The status change comments for the treatment day in this row. |
| 6 | `TRG_STATUS_C_NAME` | VARCHAR |  | Stores the status of the treatment day. |
| 7 | `REC_TYPE_C_NAME` | VARCHAR |  | The record type associated with this record. |
| 8 | `SG_PATHWAY_ID` | NUMERIC |  | The ID of the pathway (TPL) containing the smart group in this record. |
| 9 | `GIVEN_EXTER_RSN_C_NAME` | VARCHAR | org | This item stores the category value for marking a day as having been given externally to Epic. |
| 10 | `REC_EVENT_ID` | VARCHAR |  | This item contains the ID of the event used to track reconciliation actions for this day |
| 11 | `NEEDS_REC_YN` | VARCHAR |  | This item contains whether or not the day needs reconciliation |
| 12 | `IS_TREATMENT_DAY_DELETED_YN` | VARCHAR |  | Whether a treatment day (TRG) has been deleted or not for EHI export purposes. A treatment day is considered deleted if it's associated with a deleted treatment plan (VI TPL 10120), it's associated with a deleted treatment cycle (I TPL 1020), it's deleted through a normal workflow (I TPL 5050), it's no longer associated with a treatment plan, or it was soft-deleted by system administrator (I TRG 14). If it's a BMT treatment and at least one of the treatment plans associated with it is not deleted, the treatment is not deleted. |
| 13 | `IS_TRT_DAY_DEL_BY_PLAN_CONV_YN` | VARCHAR |  | Virtual item that determines if a treatment day (TRG) has been deleted by treatment plan conversion or not. A treatment day is deleted by treatment plan conversion if it was replaced or discarded in a conversion (I TPL 5052, 5053), or if it's in a snapshot cycle (I TPL 1020). |
| 14 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with this treatment plan, therapy plan, dental plan, BMT plan, or pathway. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

