# LCA_RECORD_STATUS

> Table for communication job record status.

**Primary key:** `COMMUNICATION_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | LCA routing record id |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | status of the record (hidden, deleted,....) |
| 3 | `PAT_ID` | VARCHAR | FK→ | Stores the patient record associated with this communication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

