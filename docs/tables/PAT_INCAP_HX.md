# PAT_INCAP_HX

> This table holds the history of patient capacity status changes. The row with the largest LINE value is the most recently documented status for the associated patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_INCAP_STATUS_C_NAME` | VARCHAR |  | Stores the patient's incapacity status and a history of previous incapacity statuses. |
| 4 | `PAT_INCAP_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant when a user documented the patient's incapacity status. This column also stores a history of previous UTC instants when prior statuses were documented. |
| 5 | `PAT_INCAP_CMT` | VARCHAR |  | Stores the free text comment documented on the patient's incapacity status and a history of previous comments documented on prior statuses. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

