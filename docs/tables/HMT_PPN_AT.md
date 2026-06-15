# HMT_PPN_AT

> This table contains information stored in the Health Maintenance Postpone audit trail.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HMT_PPN_TOPIC_ID` | NUMERIC |  | The unique ID of the health maintenance topic that is postponed. |
| 4 | `HMT_PPN_TOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 5 | `HMT_PPN_USR_ID` | VARCHAR |  | The unique ID of the user that postponed a health maintenance topic. |
| 6 | `HMT_PPN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `HMT_PPN_DTTM` | DATETIME (Local) |  | The instant at which a health maintenance topic was postponed. |
| 8 | `HMT_PPN_UNTL_AT_DT` | DATETIME |  | The date until which a health maintenance topic is postponed. |
| 9 | `HMT_PPN_RSN_AT_C_NAME` | VARCHAR | org | The postpone reason category number for the health maintenance topic which was postponed. |
| 10 | `HM_PPN_CMT_AT` | VARCHAR |  | This item stores a free-text comment associated with a Health Maintenance postponement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

