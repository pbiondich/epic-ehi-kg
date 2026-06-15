# BAT_REL_GRP

> The container types and specimens that are associated with each batch.

**Primary key:** `BATCH_NUMBER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BATCH_NUMBER_ID` | VARCHAR | PK FK→ | The ID of the batch. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `RQG_GROUPER_ID` | NUMERIC | FK→ | The unique ID of the requisition grouper patient record for this row. This column is frequently used to link to the RQG_DB_MAIN table. |
| 5 | `PROD_REQUEST_FINDING_ID` | NUMERIC |  | Product request (RES) record that the specimen/container is fulfilling. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BATCH_NUMBER_ID` | [BAT_DB_MAIN](BAT_DB_MAIN.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `RQG_GROUPER_ID` | [RQG_DB_MAIN](RQG_DB_MAIN.md) | sole_pk | high |

