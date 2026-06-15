# OR_LOG_LN_SCD

> This table contains the line IDs (ORM) for the SCD Information of the Surgical Log (ORL).

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log record for this row. This column is frequently used to link to the SURGICAL LOG table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCD_ID` | VARCHAR | FK→ | List of line record IDs, each of which stores the information for a single procedure and its related diagnoses. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCD_ID` | [CL_SCD_SCHED_CODE](CL_SCD_SCHED_CODE.md) | sole_pk | high |

