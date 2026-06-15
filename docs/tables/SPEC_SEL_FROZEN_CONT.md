# SPEC_SEL_FROZEN_CONT

> This table contains information about the containers selected for frozen resulting during intra-operative consultation for a specimen.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `CONTAINER_ID` | VARCHAR | FK→ | The unique ID of the container selected for resulting for the specimen's frozen section intra-operative consultation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CONTAINER_ID` | [OVC_DB_MAIN](OVC_DB_MAIN.md) | sole_pk | high |

