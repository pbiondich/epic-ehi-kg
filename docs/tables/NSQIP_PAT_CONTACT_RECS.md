# NSQIP_PAT_CONTACT_RECS

> This table contains child RDI records for follow-up patient contacts for NSQIP registry data for the surgeries that are selected for NSQIP submission. It is used in conjunction with NSQIP_INFO table.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NSQIP_PAT_CONTACT_RECORD_ID` | NUMERIC |  | The child record associated with the follow-up patient contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

