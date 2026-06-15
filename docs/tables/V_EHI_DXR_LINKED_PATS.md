# V_EHI_DXR_LINKED_PATS

> Placeholder view for DXR EHI data that needs to be marked as both static and dynamic.

**Primary key:** `DOCUMENT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient for this received document. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | Logical Owner Item |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

