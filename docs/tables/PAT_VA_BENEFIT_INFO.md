# PAT_VA_BENEFIT_INFO

> This table stores information about a patient's veteran status and benefits as reported by the VA.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QUERY_DATE` | DATETIME |  | The date on which we sent a query to the VA for a patient's veteran status. The other items in the 82400 related group will hold the results of that query, if any. |
| 4 | `VA_VETERAN_STATUS_YN` | VARCHAR |  | Whether or not the patient is considered a Title 38 Veteran according to the VA. |
| 5 | `RSN_NOT_CONFIRMED` | VARCHAR |  | The reason a patient is not considered a Title 38 Veteran. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

