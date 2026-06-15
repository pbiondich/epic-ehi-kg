# PROB_LIST_REVIEWED

> This table shows the current "Mark as Reviewed" data for the patient's problem list.

**Primary key:** `PAT_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting's encryption utility. |
| 2 | `PROB_LIST_REV_DATE` | DATETIME |  | This is the date the problem list was last reviewed. |
| 3 | `PROB_LIST_REV_TIME` | DATETIME (Local) |  | This is the time the problem list was last reviewed. |
| 4 | `PROB_LIST_REVUSR_ID` | VARCHAR |  | This is the user who last reviewed the Problem List. |
| 5 | `PROB_LIST_REVUSR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `PROB_REV_EPT_CSN` | NUMERIC |  | The unique contact serial number for the patient encounter in which the problem list was last reviewed within an encounter context. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

