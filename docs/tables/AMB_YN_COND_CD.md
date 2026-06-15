# AMB_YN_COND_CD

> This table holds the yes/no condition or response codes for claim level ambulance data.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AMB_COND_CD_YN` | VARCHAR |  | This item holds the yes/no condition or response code (CRC02) for claim level ambulance certifications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

