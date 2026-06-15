# CASE_ICD_PROC

> The CASE_ICD_PROC table contains information about ICD procedures associated with case records.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ICD_PX_ID` | VARCHAR | FK→ | Specifies the ICD procedure. |
| 4 | `ICD_PX_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ICD_PX_ID` | [CL_ICD_PX](CL_ICD_PX.md) | sole_pk | high |

