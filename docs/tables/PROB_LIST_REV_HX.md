# PROB_LIST_REV_HX

> This table contains all the historical entries (dates/times/users/related contacts) for when the patient's problem list was marked as reviewed.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting's encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROB_LIST_REV_HX_DT` | DATETIME |  | All the historical dates the patient's problem list was reviewed |
| 4 | `PROB_LIST_REV_HX_TM` | DATETIME (Local) |  | All the historical times the patient's problem list was reviewed |
| 5 | `PRBLST_REVUSRHX_ID` | VARCHAR |  | All the users that have reviewed the patient's Problem List. |
| 6 | `PRBLST_REVUSRHX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PROB_LIST_REV_CSNHX` | NUMERIC |  | The unique contact serial number for the patient encounter in which the problem list was reviewed within an encounter context. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

