# APPEAL_GRV_AUDIT_TRAIL

> This table contains the audit trail of item value changes for an appeal/grievance record.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_TRAIL_TYPE_C_NAME` | VARCHAR |  | The type of change category ID this line in the audit trail is for. |
| 4 | `DOCUMENT_ID` | VARCHAR | shared | The unique ID of the document attachment that was modified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

