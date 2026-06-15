# BAT_REQ_IN_BATCH

> The requisition IDs that are attached to the batch.

**Primary key:** `BATCH_NUMBER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BATCH_NUMBER_ID` | VARCHAR | PK FK→ | The unique ID of the batch. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REQUISITION_ID` | NUMERIC | shared | The requisition IDs that are included in the batch. |
| 4 | `REQ_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `REQ_RQG_GROUPER_ID` | NUMERIC |  | The unique ID of the requisition grouper patient record for this row. This column is frequently used to link to the RQG_DB_MAIN table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BATCH_NUMBER_ID` | [BAT_DB_MAIN](BAT_DB_MAIN.md) | sole_pk | high |
| `REQ_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

