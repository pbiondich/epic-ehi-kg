# IMM_HM_SEQ_NUM

> This table contains information about an immunization administration's health maintenance sequence number. The records included in this table are Problem List (LPL) records that satisfied a Health Maintenance topic for the patient.

**Primary key:** `IMMUNE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMMUNE_ID` | NUMERIC | PK FK→ | The unique ID of the immunization administration record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMM_HM_TOPIC_ID` | NUMERIC |  | The unique ID of the health maintenance topic that is satisfied by this immunization administration. |
| 4 | `IMM_HM_TOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 5 | `IMM_HM_SEQ` | INTEGER |  | The health maintenance topic's sequence number of the immunization administration. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `IMMUNE_ID` | [IMMUNE](IMMUNE.md) | sole_pk | high |

