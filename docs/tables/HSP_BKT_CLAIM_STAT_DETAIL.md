# HSP_BKT_CLAIM_STAT_DETAIL

> Holds current status reason and additional detail.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the bucket record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAIM_STATUS_RSN_C_NAME` | VARCHAR |  | The current claim status reason associated with the claim status update for the accepted claim on the bucket. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

