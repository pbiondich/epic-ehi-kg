# V_EHI_OVR_LINKED_RQGS

> Placeholder view for OVR EHI data that needs to be marked as both static and dynamic.

**Primary key:** `RESULT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `GROUPER_ID` | NUMERIC | FK→ | The unique ID of the non-participating submitter's patient (RQG) associated with the result record. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GROUPER_ID` | [SCHEDULING_GROUPER_INFO](SCHEDULING_GROUPER_INFO.md) | sole_pk | high |

