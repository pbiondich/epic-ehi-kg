# PAT_PERM_CMTS

> This table stores any permanent comments associated with a patient record. Permanent comments appear during appointment entry and on scheduled reports. Each line represents one line of permanent comments text.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique system identifier of the patient record. (EPT dot one) |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PERM_CMT` | VARCHAR |  | This column contains permanent comments about the patient. These comments appear during appointment entry and on scheduling reports. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

