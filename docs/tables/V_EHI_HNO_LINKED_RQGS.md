# V_EHI_HNO_LINKED_RQGS

> Placeholder view for HNO EHI data that needs to be marked as both static and dynamic.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RQG_GROUPER_ID` | NUMERIC | FK→ | The unique ID of the requisition grouper associated with the note. |
| 4 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RQG_GROUPER_ID` | [RQG_DB_MAIN](RQG_DB_MAIN.md) | sole_pk | high |

